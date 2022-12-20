from colour import UIColour
import wx
from tabs.operation.components.Control import Control
from tabs.operation.components.Monitor import Monitor
from components.Header import CustomHeader


class OperationTab():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.current_mission = None

        #define custom color palette
        self.__ui_colour = UIColour()
        
        #Create wrapper panel of Operation page
        self.panel = wx.Panel(self.parent)
        self.body_panel = wx.Panel(self.parent)
        self.body_panel.SetBackgroundColour(self.__ui_colour.BLACK)

        # Create header mode. (Root Header)
        self.mode_header = CustomHeader(self.body_panel, "Operation", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 20).GetObject()



         # CONTROL SIDE (LEFT SIDE)
        # Create control panel (wrapper) .
        self.control_tab = Control(self.body_panel).GetObject()

        # MONITOR SIDE (RIGHT SIDE)
        # Create monitor panel (wrapper) .
        self.monitor_tab = Monitor(self.body_panel).GetObject()



        # Layout for content of page (control tab && monitor tab).
        content_layout = wx.BoxSizer(wx.HORIZONTAL)
        content_layout.Add(self.control_tab, 1, wx.EXPAND|wx.ALL, 1)
        content_layout.Add(self.monitor_tab, 2, wx.EXPAND|wx.ALL, 1)

        # Layout for entire page (header mode + content field).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 1)
        body_layout.Add(content_layout, 10, wx.EXPAND|wx.ALL, 1)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel


