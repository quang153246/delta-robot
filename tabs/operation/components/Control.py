from colour import UIColour
import wx
from components.ToggleButton import ToggleButton
from components.Header import CustomHeader
from components.Select import Select

class Control():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()

         # Create Control side panel (left side)
        self.control_tab = wx.Panel(self.parent)
        self.control_tab.SetBackgroundColour(self.__ui_colour.WHITE)

        # Create mission box
        self.mission_box = wx.Panel(self.control_tab)


        mission_box_layout_v =  wx.BoxSizer(wx.VERTICAL)
        mission_box_layout_h =  wx.BoxSizer(wx.HORIZONTAL)
        # Create two layout for one Pannel to make it can padding with two different sizes following vertical and horizontal

        self.select_label = CustomHeader(self.mission_box, "Choose Mission (Optional):", self.__ui_colour.WHITE, self.__ui_colour.GREEN_MAIN).GetObject()
        self.select = Select(self.mission_box).GetObject()

        # Add components to layout
        mission_box_layout_v.Add(self.select_label, 1, wx.EXPAND|wx.TOP, 20)
        mission_box_layout_v.Add(self.select, 1, wx.EXPAND|wx.ALL, 10)
        mission_box_layout_h.Add(mission_box_layout_v, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 45)
       
        self.mission_box.SetSizer(mission_box_layout_h)
        self.mission_box.Layout()

        # Control box (Start & Stop)
        self.control_box = wx.Panel(self.control_tab)

        # Create content control.
        control_box_layout_v =  wx.BoxSizer(wx.VERTICAL)
        control_box_layout_h =  wx.BoxSizer(wx.HORIZONTAL)
        # Create 2 layout to padding with TOP|BOTTOM LEFT|RIGHT of each component

        # Layout for box of all components
        control_box_layout_sub =  wx.BoxSizer(wx.HORIZONTAL)

        self.control_label = CustomHeader(self.control_box, "Control:", self.__ui_colour.WHITE, self.__ui_colour.GREEN_MAIN)
        self.startButton = ToggleButton(self.control_box, Title= "Start", BackGround= self.__ui_colour.GREEN_DARK, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State= False, TextSize=15)
        self.stopButton = ToggleButton(self.control_box, Title= "Stop", BackGround= self.__ui_colour.RED_DARK, SubBackGround= self.__ui_colour.GRAY_MAIN, TextColor= self.__ui_colour.WHITE, State=True, TextSize=15)
        # Bind event for buttons
        self.startButton.GetObject().Bind(wx.EVT_BUTTON, self.startButton_changeState)
        self.stopButton.GetObject().Bind(wx.EVT_BUTTON, self.stopButton_changeState)

        control_box_layout_v.Add(self.control_label.GetObject(), 1, wx.EXPAND|wx.BOTTOM, 10)
        control_box_layout_v.Add(self.startButton.GetObject(), 3, wx.EXPAND|wx.BOTTOM, 10)
        control_box_layout_v.Add(self.stopButton.GetObject(), 3, wx.EXPAND|wx.TOP, 10)

        control_box_layout_h.Add(control_box_layout_v, 1,  wx.EXPAND|wx.LEFT|wx.RIGHT, 40)
        
        control_box_layout_sub.Add(control_box_layout_h, 1, wx.EXPAND|wx.BOTTOM, 20)
        
        self.control_box.SetSizer(control_box_layout_sub)
        self.control_box.Layout()

        # ----Create Status Box------
        self.status_box = wx.Panel(self.control_tab)
        status_box_layout = wx.BoxSizer(wx.VERTICAL)

        # Create header connection status.
        self.status_header = CustomHeader(self.status_box, "Connection Status", self.__ui_colour.GRAY_DARK, self.__ui_colour.TEXT_HEADER_MODE).GetObject()
        # Create content connection status.
        self.status_content =  wx.Panel(self.status_box)
        status_content_layout =  wx.BoxSizer(wx.VERTICAL)

        #check robot
        robot_status = CustomHeader(self.status_content, "Robot Connection: " + "True", self.__ui_colour.white, self.__ui_colour.PRIMARY, 16).GetObject()
        # Check camera
        camera_status = CustomHeader(self.status_content, "Camera Connection: " + "True", self.__ui_colour.white, self.__ui_colour.PRIMARY, 16).GetObject()

        status_content_layout.Add(robot_status, 1, wx.ALIGN_CENTER, 0)
        status_content_layout.Add(camera_status,1, wx.ALIGN_CENTER, 0)
        self.status_content.SetSizer(status_content_layout)
        self.status_content.Layout()

        status_box_layout.Add(self.status_header, 1, wx.EXPAND|wx.ALL, 0)
        status_box_layout.Add(self.status_content, 3, wx.EXPAND|wx.ALL, 0)
        self.status_box.SetSizer(status_box_layout)
        self.status_box.Layout()

         # Layout for Control Side (left side)
        control_tab_layout = wx.BoxSizer(wx.VERTICAL)
        control_tab_layout.Add(self.mission_box, 2, wx.EXPAND|wx.ALL, 0)
        control_tab_layout.Add(self.control_box, 2, wx.EXPAND|wx.ALL, 0)
        control_tab_layout.Add(self.status_box, 3, wx.EXPAND|wx.ALL, 0)
        self.control_tab.SetSizer(control_tab_layout)
        self.control_tab.Layout()

    def GetObject(self):
        return self.control_tab
    def startButton_changeState(self, event):
        self.stopButton.onSelect(None)
        self.startButton.onDisable(None)
        print("Start Robot")
    def stopButton_changeState(self, event):
        self.startButton.onSelect(None)
        self.stopButton.onDisable(None)
        print("Stop robot")