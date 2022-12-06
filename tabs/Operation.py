from colour import UIColour
import wx
from components.button import CustomButton
from components.header import CustomHeader
from components.Select import Select

class OperationTab():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.panel = wx.Panel(self.parent)
        self.body_panel = wx.Panel(self.parent)
        self.body_panel.SetBackgroundColour(self.__ui_colour.black)

        # Create header mode.
        self.mode_header = CustomHeader(self.body_panel, "Operation", self.__ui_colour.white, self.__ui_colour.black).GetObject()

        # Create interface panel.
        self.control_tab = wx.Panel(self.body_panel)
        self.control_tab.SetBackgroundColour(self.__ui_colour.white)


        self.mission_box = wx.Panel(self.control_tab)
        mission_box_layout = wx.BoxSizer(wx.VERTICAL)

        # Create header mission.
        self.mission_header = CustomHeader(self.mission_box, "Choose Mission", self.__ui_colour.black, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        # Create content mission.
        # self.mission_content =  CustomHeader(self.mission_box, BackGround=self.__ui_colour.white).GetObject()

        self.mission_content =  wx.Panel(self.mission_box)


        mission_content_layout =  wx.BoxSizer(wx.HORIZONTAL)
        sub =  wx.BoxSizer(wx.VERTICAL)
        self.select = Select(self.mission_content).GetObject()
        mission_content_layout.Add(self.select, 1, wx.EXPAND|wx.TOP, 20)
        sub.Add(mission_content_layout, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 45)
       
        self.mission_content.SetSizer(sub)
        self.mission_content.Layout()

        # Create enable run immediately button.
        self.run_immediately_button = CustomButton(self.mission_box, "Enable run immediately", self.__ui_colour.deep_blue, self.__ui_colour.white).GetObject()

        mission_box_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        mission_box_layout.Add(self.mission_content, 1, wx.EXPAND|wx.ALL, 0)
        mission_box_layout.Add(self.run_immediately_button, 3, wx.EXPAND|wx.ALL, 45)
        self.mission_box.SetSizer(mission_box_layout)
        self.mission_box.Layout()



        self.control_box = wx.Panel(self.control_tab)
        control_box_layout = wx.BoxSizer(wx.VERTICAL)
        # Create header control.
        self.control_header = CustomHeader(self.control_box, "Control", self.__ui_colour.black, self.__ui_colour.white).GetObject()

        # Create content control.
        self.control_content =  wx.Panel(self.control_box)
        control_content_layout_v =  wx.BoxSizer(wx.VERTICAL)
        control_content_layout_h =  wx.BoxSizer(wx.HORIZONTAL)
        control_content_layout_sub =  wx.BoxSizer(wx.HORIZONTAL)
        self.startButton = CustomButton(self.control_content, "Start", self.__ui_colour.START_BUTTON, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        self.stopButton = CustomButton(self.control_content, "Stop", self.__ui_colour.STOP_BUTTON, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        control_content_layout_v.Add(self.startButton, 1, wx.EXPAND|wx.BOTTOM, 10)
        control_content_layout_v.Add(self.stopButton, 1, wx.EXPAND|wx.TOP, 10)
        control_content_layout_h.Add(control_content_layout_v, 1,  wx.EXPAND|wx.LEFT|wx.RIGHT, 45)
        
        control_content_layout_sub.Add(control_content_layout_h, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 20)
        
        self.control_content.SetSizer(control_content_layout_sub)
        self.control_content.Layout()


        control_box_layout.Add(self.control_header, 1, wx.EXPAND|wx.ALL, 0)
        control_box_layout.Add(self.control_content, 5, wx.EXPAND|wx.ALL, 0)
        self.control_box.SetSizer(control_box_layout)
        self.control_box.Layout()




        self.status_box = wx.Panel(self.control_tab)
        status_box_layout = wx.BoxSizer(wx.VERTICAL)
        # Create header connection status.
        self.status_header = CustomHeader(self.status_box, "Connection Status", self.__ui_colour.black, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        # Create content connection status.
        self.status_content =  wx.Panel(self.status_box)
        status_content_layout =  wx.BoxSizer(wx.VERTICAL)

        #check robot
        robot_status = CustomHeader(self.status_content, "Robot Connection: " + "OK", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()
        # Check camera
        camera_status = CustomHeader(self.status_content, "Camera Connection: " + "OK", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()

        status_content_layout.Add(robot_status, 1, wx.ALIGN_CENTER, 0)
        status_content_layout.Add(camera_status,1, wx.ALIGN_CENTER, 0)
        self.status_content.SetSizer(status_content_layout)
        self.status_content.Layout()

        status_box_layout.Add(self.status_header, 1, wx.EXPAND|wx.ALL, 0)
        status_box_layout.Add(self.status_content, 3, wx.EXPAND|wx.ALL, 0)
        self.status_box.SetSizer(status_box_layout)
        self.status_box.Layout()



        # Layout interface panel.
        control_tab_layout = wx.BoxSizer(wx.VERTICAL)
        # control_tab_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        # control_tab_layout.Add(self.mission_content, 5, wx.EXPAND|wx.ALL, 0)
        control_tab_layout.Add(self.mission_box, 3, wx.EXPAND|wx.ALL, 0)
        control_tab_layout.Add(self.control_box, 3, wx.EXPAND|wx.ALL, 0)
        control_tab_layout.Add(self.status_box, 2, wx.EXPAND|wx.ALL, 0)
        self.control_tab.SetSizer(control_tab_layout)
        self.control_tab.Layout()

#===============================================================================================

        # Create monitor panel.
        self.monitor_tab = wx.Panel(self.body_panel)
        monitor_tab_w, monitor_tab_h = self.monitor_tab.GetSize()
        print(monitor_tab_w, monitor_tab_h)
        self.monitor_tab.SetBackgroundColour(self.__ui_colour.white)

        # --------Time Box--------
        self.time_box = wx.Panel(self.monitor_tab)
        time_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        startTime = CustomHeader(self.time_box, "Start time: " + "7h AM", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()
        currentTime = CustomHeader(self.time_box, "Current time: " + "9h AM", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()
        stopTime = CustomHeader(self.time_box, "Stop time: " + "11h PM", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()
        time_box_layout.Add(startTime, 1, wx.EXPAND|wx.ALL,0 )
        time_box_layout.Add(currentTime, 1, wx.EXPAND|wx.ALL,0 )
        time_box_layout.Add(stopTime, 1, wx.EXPAND|wx.ALL,0 )
        self.time_box.SetSizer(time_box_layout)
        self.time_box.Layout()

        # ----Video Box-----
        self.video_box = wx.Panel(self.monitor_tab)
        self.video_box.SetBackgroundColour(self.__ui_colour.black)

        video_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        video_box_layout_sub = wx.BoxSizer(wx.VERTICAL)

        self.stream_video = wx.Panel(self.video_box)
        logo_width, logo_height = self.video_box.GetSize()
        self.logo_image = wx.Image("./image/sample.png").Scale(int(logo_width)*40, int(logo_height)*26, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        self.logo_bitmap = wx.StaticBitmap(self.stream_video)
        self.logo_bitmap.SetBitmap(self.logo_image)

        video_box_layout.Add(self.stream_video, 1, wx.ALIGN_CENTER,0 )
        # video_box_layout_sub.Add(video_box_layout, 1, wx.ALIGN_CENTER,0 )
        self.video_box.SetSizer(video_box_layout)
        self.video_box.Layout()

        # ------ Result_box Box -------
        self.result_box = wx.Panel(self.monitor_tab)
        result_box_layout = wx.BoxSizer(wx.HORIZONTAL)

        not_good_items = CustomHeader(self.result_box, "Not Good Items: " + "100", self.__ui_colour.white, self.__ui_colour.STOP_BUTTON).GetObject()
        already_picked_items = CustomHeader(self.result_box, "Already_Picked_Items: " + "100", self.__ui_colour.white, self.__ui_colour.STOP_BUTTON).GetObject()
        result_box_layout.Add(not_good_items, 1, wx.EXPAND|wx.ALL, 1)
        result_box_layout.Add(already_picked_items, 1, wx.EXPAND|wx.ALL, 1)
   
        self.result_box.SetSizer(result_box_layout)
        self.result_box.Layout()



        monitor_tab_layout = wx.BoxSizer(wx.VERTICAL)
        monitor_tab_layout.Add(self.time_box, 1 , wx.EXPAND|wx.ALL, 0)
        monitor_tab_layout.Add(self.video_box, 6 , wx.ALIGN_CENTER, 0)
        monitor_tab_layout.Add(self.result_box, 1 , wx.EXPAND|wx.LEFT|wx.RIGHT, 10)

        self.monitor_tab.SetSizer(monitor_tab_layout)
        self.monitor_tab.Layout()


        # Layout sub body panel (interface bar and monitor bar).
        sub_body_layout = wx.BoxSizer(wx.HORIZONTAL)
        sub_body_layout.Add(self.control_tab, 1, wx.EXPAND|wx.ALL, 1)
        sub_body_layout.Add(self.monitor_tab, 2, wx.EXPAND|wx.ALL, 1)

        # Layout body panel (mode bar and sub body).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 1)
        body_layout.Add(sub_body_layout, 10, wx.EXPAND|wx.ALL, 1)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel
