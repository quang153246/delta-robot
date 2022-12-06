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
        self.interface_bar = wx.Panel(self.body_panel)
        self.interface_bar.SetBackgroundColour(self.__ui_colour.white)

        # Create header mission.
        self.mission_header = CustomHeader(self.interface_bar, "Choose Mission", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content mission.
        self.mission_content =  CustomHeader(self.interface_bar, BackGround=self.__ui_colour.white).GetObject()
        # Create enable run immediately button.
        self.run_immediately_button = CustomButton(self.interface_bar, "Enable run immediately", self.__ui_colour.deep_blue, self.__ui_colour.white).GetObject()

        # Create header control.
        self.control_header = CustomHeader(self.interface_bar, "Control", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content control.
        self.control_content =  CustomHeader(self.interface_bar, BackGround=self.__ui_colour.white).GetObject()

        # Create header connection status.
        self.connection_status_header = CustomHeader(self.interface_bar, "Connection Status", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content connection status.
        self.connection_status_content =  CustomHeader(self.interface_bar, BackGround=self.__ui_colour.white).GetObject()

        # Layout interface panel.
        interface_bar_layout = wx.BoxSizer(wx.VERTICAL)
        interface_bar_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.mission_content, 5, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.control_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.control_content, 5, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.connection_status_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.connection_status_content, 2, wx.EXPAND|wx.ALL, 0)
        self.interface_bar.SetSizer(interface_bar_layout)
        self.interface_bar.Layout()

        # Create monitor panel.
        self.monitor_bar = wx.Panel(self.body_panel)
        self.monitor_bar.SetBackgroundColour(self.__ui_colour.white)

        # Layout sub body panel (interface bar and monitor bar).
        sub_body_layout = wx.BoxSizer(wx.HORIZONTAL)
        sub_body_layout.Add(self.interface_bar, 1, wx.EXPAND|wx.ALL, 1)
        sub_body_layout.Add(self.monitor_bar, 2, wx.EXPAND|wx.ALL, 1)

        # Layout body panel (mode bar and sub body).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 1)
        body_layout.Add(sub_body_layout, 10, wx.EXPAND|wx.ALL, 1)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel
