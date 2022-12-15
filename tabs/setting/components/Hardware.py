from colour import UIColour
import wx
from components.ToggleButton import ToggleButton
from components.Header import CustomHeader
from components.VideoFrame import VideoFrame
from components.Form import Form
from device.camera import CameraControl
import numpy as np

class Hardware():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.camera_status = False
        self.__ui_colour = UIColour()

        self.content_panel = wx.Panel(self.parent)
        self.content_panel.SetBackgroundColour(self.__ui_colour.WHITE)
        # ------------ HARDWARE CHECK------------

        #  different layout to create background for robot_tab
        self.robot_tab_background = wx.Panel(self.content_panel)
        self.robot_tab_background.SetBackgroundColour(self.__ui_colour.GRAY_DARK)
        robot_tab_background_layout = wx.BoxSizer(wx.HORIZONTAL)
        
        self.robot_tab = wx.Panel(self.robot_tab_background)
        self.robot_tab.SetBackgroundColour(self.__ui_colour.WHITE)
        
        robot_tab_background_layout.Add(self.robot_tab, 1 , wx.EXPAND|wx.ALL, 1)
        self.robot_tab_background.SetSizer(robot_tab_background_layout)
        self.robot_tab_background.Layout()

        # self.camera_tab = wx.Panel(self.content_panel)

        self.camera_tab_background = wx.Panel(self.content_panel)
        self.camera_tab_background.SetBackgroundColour(self.__ui_colour.GRAY_DARK)
        camera_tab_background_layout = wx.BoxSizer(wx.VERTICAL)
        
        self.camera_tab = wx.Panel(self.camera_tab_background)
        self.camera_tab.SetBackgroundColour(self.__ui_colour.WHITE)
        
        camera_tab_background_layout.Add(self.camera_tab, 1 , wx.EXPAND|wx.ALL, 1)
        self.camera_tab_background.SetSizer(camera_tab_background_layout)
        self.camera_tab_background.Layout()



        self.robot_header = CustomHeader(self.robot_tab, "Robot", self.__ui_colour.BLACK, self.__ui_colour.WHITE).GetObject()
        self.robot_connection_status = CustomHeader(self.robot_tab, "Robot connection: OK", self.__ui_colour.WHITE, self.__ui_colour.BLUE_MAIN).GetObject()
        self.robot_connection_button = ToggleButton(self.robot_tab, Title= "Connect to robot", SubTitle= "Disconnect to robot" , BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=14).GetObject()
        self.white_space =wx.Panel(self.robot_tab)
        self.init_position_robot_button = ToggleButton(self.robot_tab, Title= "GO HOME", BackGround= self.__ui_colour.GREEN_MAIN, SubBackGround= self.__ui_colour.GREEN_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()
        self.position_setup_header = CustomHeader(self.robot_tab, "Move to point: ", self.__ui_colour.WHITE, self.__ui_colour.GREEN_MAIN).GetObject()

        #Form
        self.x_form = Form(self.robot_tab, "X: ", self.__ui_colour.BLACK, "x_value").GetObject()
        self.y_form = Form(self.robot_tab, "Y: ", self.__ui_colour.BLACK, "y_value").GetObject()
        self.z_form = Form(self.robot_tab, "Z: ", self.__ui_colour.BLACK, "z_value").GetObject()


        self.execute_button = ToggleButton(self.robot_tab, Title= "Execute", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.BLUE_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()

        self.camera_header = CustomHeader(self.camera_tab, "Camera", self.__ui_colour.BLACK, self.__ui_colour.WHITE).GetObject()

        self.camera_control = wx.Panel(self.camera_tab)
        self.camera_connection_button = ToggleButton(self.camera_control, Title= "Connect to camera", SubTitle="Disconnect to camera" , BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16)
        self.camera_connection_status = CustomHeader(self.camera_control, "Camera connection: " + str(self.camera_status), self.__ui_colour.WHITE, self.__ui_colour.BLUE_MAIN)
        self.camera_connection_button.GetObject().Bind(wx.EVT_BUTTON, self.toggle_camera)

        camera_control_layout = wx.BoxSizer(wx.HORIZONTAL)
        camera_control_layout.Add(self.camera_connection_button.GetObject(), 2 , wx.EXPAND | wx.LEFT, 70)
        camera_control_layout.Add(self.camera_connection_status.GetObject(), 4 , wx.EXPAND | wx.LEFT, 90) 
        self.camera_control.SetSizer(camera_control_layout)
        self.camera_control.Layout()

        #camera
        self.camera_logitech = CameraControl()

        self.video_box = wx.Panel(self.camera_tab)
        self.video_box.SetBackgroundColour(self.__ui_colour.WHITE)

        self.stream_video = VideoFrame(self.video_box)

        

        self.timer = wx.Timer(self.stream_video.GetObject())
        self.timer.Start(int(1000.0 / 30.0))
        self.stream_video.GetObject().Bind(wx.EVT_TIMER, self.NextFrame)

        frame = np.zeros([self.stream_video.frame_height, self.stream_video.frame_width], dtype=int)        
        self.bmp = wx.Bitmap.FromBuffer(self.stream_video.frame_width, self.stream_video.frame_height, frame)

        self.stream_video.GetObject().Bind(wx.EVT_PAINT, self.OnPaint)

        video_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        video_box_layout_sub = wx.BoxSizer(wx.VERTICAL)

        video_box_layout.Add(self.stream_video.GetObject(), 1, wx.EXPAND|wx.TOP|wx.BOTTOM,0)
        video_box_layout_sub.Add(video_box_layout, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 70)
        self.video_box.SetSizer(video_box_layout_sub)
        self.video_box.Layout()

        # Layout for robot side
        robot_tab_layout = wx.BoxSizer(wx.VERTICAL)
        robot_tab_layout.Add(self.robot_header, 3, wx.EXPAND|wx.TOP, 0)
        robot_tab_layout.Add(self.robot_connection_status, 4, wx.EXPAND|wx.ALL, 0)
        robot_tab_layout.Add(self.robot_connection_button, 6,  wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        robot_tab_layout.Add(self.white_space, 1, wx.EXPAND)
        robot_tab_layout.Add(self.init_position_robot_button, 6, wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        robot_tab_layout.Add(self.position_setup_header, 4, wx.EXPAND|wx.TOP, 10)
        robot_tab_layout.Add(self.x_form, 4, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 5)
        robot_tab_layout.Add(self.y_form, 4, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 5)
        robot_tab_layout.Add(self.z_form, 4, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 5)
        robot_tab_layout.Add(self.execute_button, 6, wx.EXPAND|wx.ALL, 10)
        self.robot_tab.SetSizer(robot_tab_layout)
        self.robot_tab.Layout()

        # Layout for Camera side
        camera_tab_layout = wx.BoxSizer(wx.VERTICAL)
        camera_tab_layout.Add(self.camera_header, 1, wx.EXPAND|wx.TOP, 0)
        camera_tab_layout.Add(self.camera_control, 2, wx.EXPAND|wx.TOP, 20)
        camera_tab_layout.Add(self.video_box, 10, wx.EXPAND|wx.TOP, 20)
       
        self.camera_tab.SetSizer(camera_tab_layout)
        self.camera_tab.Layout()





        # Combine Robot + Camera box into Content box
        content_panel_layout = wx.BoxSizer(wx.HORIZONTAL)
        content_panel_layout.Add(self.robot_tab_background, 1, wx.EXPAND|wx.ALL, 10)
        content_panel_layout.Add(self.camera_tab_background, 3, wx.EXPAND|wx.ALL, 10)   
        self.content_panel.SetSizer(content_panel_layout)
        self.content_panel.Layout()

    def GetObject(self):
        return self.content_panel
    def toggle_camera(self, evt):
        print("Toggle button")
        if(self.camera_logitech.is_available() == False):
            self.camera_connection_button.onDisable(None)
            self.camera_logitech.open_connection()
            # self.camera_status = True
        else:
            self.camera_connection_button.onSelect(None)
            self.camera_logitech.close_connection()
            # self.camera_status = False
        self.camera_status = self.camera_logitech.is_available()
        self.camera_connection_status.Set_Label("Camera connection: " + str(self.camera_status))
        print("Status: ",self.camera_logitech.is_available())

    def NextFrame(self, event):

        if self.camera_status == True:
            frame = self.camera_logitech.get_frame()
            frame = self.camera_logitech.flip_frame(frame)
            print("Frameeee:",frame)
            # buffer = self.stream_video.GetBuffer()

            self.bmp.CopyFromBuffer(frame)
            self.stream_video.GetObject().Refresh()
            self.content_panel.Layout()

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self.stream_video.GetObject())
        dc.DrawBitmap(self.bmp, 0, 0)

        

