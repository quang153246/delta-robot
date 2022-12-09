from colour import UIColour
import wx
from components.ToggleButton import ToggleButton
from components.Header import CustomHeader
from components.SettingNav import SettingNav
from components.VideoFrame import VideoFrame
from components.Form import Form


class SettingTab():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.panel = wx.Panel(self.parent)
        self.body_panel = wx.Panel(self.parent)
        self.body_panel.SetBackgroundColour(self.__ui_colour.WHITE)

        # Create header mode.
        self.mode_header = CustomHeader(self.body_panel, "Settings", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 20).GetObject()
        self.tab_header = SettingNav(self.body_panel).GetObject()
        self.content_panel = wx.Panel(self.body_panel)
        self.content_panel.SetBackgroundColour(self.__ui_colour.WHITE)

        # ------------ HARDWARE CHECK------------
        self.robot_tab_background = wx.Panel(self.content_panel)
        self.robot_tab_background.SetBackgroundColour(self.__ui_colour.GRAY_DARK)
        robot_tab_background_layout = wx.BoxSizer(wx.VERTICAL)
        
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
        self.robot_connection_status = CustomHeader(self.robot_tab, "Robot connection: ", self.__ui_colour.WHITE, self.__ui_colour.BLUE_MAIN).GetObject()
        self.robot_connection_button = ToggleButton(self.robot_tab, Title= "Connect to robot", SubTitle= "Disconnect to robot" , BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()
        self.white_space = CustomHeader(self.robot_tab, " ", self.__ui_colour.WHITE, self.__ui_colour.BLUE_MAIN).GetObject()
        self.init_position_robot_button = ToggleButton(self.robot_tab, Title= "GO HOME", BackGround= self.__ui_colour.GREEN_MAIN, SubBackGround= self.__ui_colour.GREEN_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()
        self.position_setup_header = CustomHeader(self.robot_tab, "Move to point: ", self.__ui_colour.WHITE, self.__ui_colour.GREEN_MAIN).GetObject()

        #Form
        self.x_form = Form(self.robot_tab, "X: ", self.__ui_colour.BLACK, "x_value").GetObject()
        self.y_form = Form(self.robot_tab, "Y: ", self.__ui_colour.BLACK, "y_value").GetObject()
        self.z_form = Form(self.robot_tab, "Z: ", self.__ui_colour.BLACK, "z_value").GetObject()


        self.execute_button = ToggleButton(self.robot_tab, Title= "Execute", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.BLUE_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()

        self.camera_header = CustomHeader(self.camera_tab, "Camera", self.__ui_colour.BLACK, self.__ui_colour.WHITE).GetObject()

        self.camera_control = wx.Panel(self.camera_tab)
        self.camera_connection_button = ToggleButton(self.camera_control, Title= "Connect to camera", SubTitle="Disconnect to camera" , BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=16).GetObject()
        self.camera_connection_status = CustomHeader(self.camera_control, "Camera connection: ", self.__ui_colour.WHITE, self.__ui_colour.BLUE_MAIN).GetObject()
        camera_control_layout = wx.BoxSizer(wx.HORIZONTAL)
        camera_control_layout.Add(self.camera_connection_button, 2 , wx.EXPAND | wx.TOP, 20)
        camera_control_layout.Add(self.camera_connection_status, 4 , wx.EXPAND | wx.TOP, 20)
        self.camera_control.SetSizer(camera_control_layout)
        self.camera_control.Layout()

        #camera
        self.video_box = wx.Panel(self.camera_tab)
        self.video_box.SetBackgroundColour(self.__ui_colour.GRAY_LIGHT)

        video_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        video_box_layout_sub = wx.BoxSizer(wx.VERTICAL)

        self.stream_video = VideoFrame(self.video_box, 30).GetObject()

        video_box_layout.Add(self.stream_video, 1, wx.EXPAND|wx.TOP|wx.BOTTOM,32)
        video_box_layout_sub.Add(video_box_layout, 1, wx.EXPAND|wx.LEFT|wx.RIGHT,360 )
        self.video_box.SetSizer(video_box_layout_sub)
        self.video_box.Layout()




        #-----------------------------------
        robot_tab_layout = wx.BoxSizer(wx.VERTICAL)
        robot_tab_layout.Add(self.robot_header, 1, wx.EXPAND|wx.TOP, 0)
        robot_tab_layout.Add(self.robot_connection_status, 2, wx.EXPAND|wx.ALL, 0)
        robot_tab_layout.Add(self.robot_connection_button, 2,  wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        robot_tab_layout.Add(self.white_space, 1, wx.EXPAND|wx.BOTTOM, 0)
        robot_tab_layout.Add(self.init_position_robot_button, 2, wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        robot_tab_layout.Add(self.position_setup_header, 1, wx.EXPAND|wx.ALL, 0)
        robot_tab_layout.Add(self.x_form, 1, wx.ALIGN_CENTER, 0)
        robot_tab_layout.Add(self.y_form, 1, wx.ALIGN_CENTER, 0)
        robot_tab_layout.Add(self.z_form, 1, wx.ALIGN_CENTER, 0)
        robot_tab_layout.Add(self.execute_button, 2, wx.EXPAND|wx.ALL, 20)
        self.robot_tab.SetSizer(robot_tab_layout)
        self.robot_tab.Layout()

        camera_tab_layout = wx.BoxSizer(wx.VERTICAL)
        camera_tab_layout.Add(self.camera_header, 1, wx.EXPAND|wx.TOP, 0)
        camera_tab_layout.Add(self.camera_control, 2, wx.EXPAND|wx.LEFT|wx.RIGHT, 20)
        camera_tab_layout.Add(self.video_box, 10, wx.EXPAND|wx.ALL, 20)
       
        self.camera_tab.SetSizer(camera_tab_layout)
        self.camera_tab.Layout()






        content_panel_layout = wx.BoxSizer(wx.HORIZONTAL)
        content_panel_layout.Add(self.robot_tab_background, 1, wx.EXPAND|wx.ALL, 10)
        content_panel_layout.Add(self.camera_tab_background, 3, wx.EXPAND|wx.ALL, 10)
        self.content_panel.SetSizer(content_panel_layout)
        self.content_panel.Layout()


        # Layout body panel (mode bar and sub body).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1,  wx.EXPAND|wx.ALL, 0)
        body_layout.Add(self.tab_header, 1,  wx.EXPAND|wx.ALL, 0)
        body_layout.Add(self.content_panel, 10, wx.EXPAND|wx.ALL, 20)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel
    def startButton_changeState(self, event):
        self.stopButton.onSelect(None)
        self.startButton.onDisable(None)
    def stopButton_changeState(self, event):
        self.startButton.onSelect(None)
        self.stopButton.onDisable(None)
