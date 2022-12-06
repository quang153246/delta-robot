from colour import UIColour
import wx
from components.Button import CustomButton
from components.Header import CustomHeader

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
        self.tab1 = wx.Panel(self.body_panel)
        self.tab1.SetBackgroundColour(self.__ui_colour.white)


        self.mission_box = wx.Panel(self.tab1)
        mission_box_layout = wx.BoxSizer(wx.VERTICAL)

        # Create header mission.
        self.mission_header = CustomHeader(self.mission_box, "Choose Mission", self.__ui_colour.black, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        # Create content mission.
        self.mission_content =  CustomHeader(self.mission_box, BackGround=self.__ui_colour.white).GetObject()
        # Create enable run immediately button.
        self.run_immediately_button = CustomButton(self.mission_box, "Enable run immediately", self.__ui_colour.deep_blue, self.__ui_colour.white).GetObject()

        mission_box_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        mission_box_layout.Add(self.mission_content, 2, wx.EXPAND|wx.ALL, 0)
        mission_box_layout.Add(self.run_immediately_button, 3, wx.EXPAND|wx.ALL, 45)
        self.mission_box.SetSizer(mission_box_layout)
        self.mission_box.Layout()



        self.control_box = wx.Panel(self.tab1)
        control_box_layout = wx.BoxSizer(wx.VERTICAL)
        # Create header control.
        self.control_header = CustomHeader(self.control_box, "Control", self.__ui_colour.black, self.__ui_colour.white).GetObject()

        # Create content control.
        self.control_content =  wx.Panel(self.control_box)
        control_content_layout =  wx.BoxSizer(wx.VERTICAL)
        self.startButton = CustomButton(self.control_content, "Start", self.__ui_colour.START_BUTTON, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        self.stopButton = CustomButton(self.control_content, "Stop", self.__ui_colour.STOP_BUTTON, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        control_content_layout.Add(self.startButton, 1, wx.EXPAND|wx.ALL, 20)
        control_content_layout.Add(self.stopButton, 1, wx.EXPAND|wx.ALL, 20)
        self.control_content.SetSizer(control_content_layout)
        self.control_content.Layout()


        control_box_layout.Add(self.control_header, 1, wx.EXPAND|wx.ALL, 0)
        control_box_layout.Add(self.control_content, 5, wx.EXPAND|wx.ALL, 0)
        self.control_box.SetSizer(control_box_layout)
        self.control_box.Layout()




        self.status_box = wx.Panel(self.tab1)
        status_box_layout = wx.BoxSizer(wx.VERTICAL)
        # Create header connection status.
        self.status_header = CustomHeader(self.status_box, "Connection Status", self.__ui_colour.black, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        # Create content connection status.
        self.status_content =  wx.Panel(self.status_box)
        status_content_layout =  wx.BoxSizer(wx.VERTICAL)

        #check robot
        robot_status = CustomHeader(self.status_content, "Robot Connection: ", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()
        # Check camera
        camera_status = CustomHeader(self.status_content, "Camera Connection: ", self.__ui_colour.white, self.__ui_colour.PRIMARY).GetObject()

        status_content_layout.Add(robot_status, 1, wx.ALIGN_CENTER, 0)
        status_content_layout.Add(camera_status,1, wx.ALIGN_CENTER, 0)
        self.status_content.SetSizer(status_content_layout)
        self.status_content.Layout()

        status_box_layout.Add(self.status_header, 1, wx.EXPAND|wx.ALL, 0)
        status_box_layout.Add(self.status_content, 3, wx.EXPAND|wx.ALL, 0)
        self.status_box.SetSizer(status_box_layout)
        self.status_box.Layout()



        # Layout interface panel.
        tab1_layout = wx.BoxSizer(wx.VERTICAL)
        # tab1_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        # tab1_layout.Add(self.mission_content, 5, wx.EXPAND|wx.ALL, 0)
        tab1_layout.Add(self.mission_box, 3, wx.EXPAND|wx.ALL, 0)
        tab1_layout.Add(self.control_box, 3, wx.EXPAND|wx.ALL, 0)
        tab1_layout.Add(self.status_box, 2, wx.EXPAND|wx.ALL, 0)
        self.tab1.SetSizer(tab1_layout)
        self.tab1.Layout()

        # Create monitor panel.
        self.monitor_bar = wx.Panel(self.body_panel)
        self.monitor_bar.SetBackgroundColour(self.__ui_colour.white)

        # Layout sub body panel (interface bar and monitor bar).
        sub_body_layout = wx.BoxSizer(wx.HORIZONTAL)
        sub_body_layout.Add(self.tab1, 1, wx.EXPAND|wx.ALL, 1)
        sub_body_layout.Add(self.monitor_bar, 2, wx.EXPAND|wx.ALL, 1)

        # Layout body panel (mode bar and sub body).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 1)
        body_layout.Add(sub_body_layout, 10, wx.EXPAND|wx.ALL, 1)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel
