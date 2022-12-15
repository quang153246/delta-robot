from colour import UIColour
import wx
from components.Header import CustomHeader
from components.SettingNav import SettingNav
from tabs.setting.components.Hardware import Hardware
from tabs.setting.components.AISetting import AISetting
from tabs.setting.components.Mission import Mission


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
       
        # Gather all components (Header mode, header tab, content)
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1,  wx.EXPAND|wx.ALL, 0)
        body_layout.Add(self.tab_header, 10,  wx.EXPAND|wx.ALL, 0)
        
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()


    def GetObject(self):
        return self.body_panel
   
