import wx
from components.ToggleButton import ToggleButton
from colour import UIColour

class SettingNav():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()

        self.nav_panel = wx.Panel(self.parent)
        self.nav_panel.SetBackgroundColour(self.__ui_colour.BLACK)

        self.hardware_check_button = ToggleButton(self.nav_panel, Title= "Hardware check", BackGround= self.__ui_colour.BLUE_DARK, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=16)
        self.AI_setting_button = ToggleButton(self.nav_panel, Title= "AI settings", BackGround= self.__ui_colour.BLUE_DARK, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=True, TextSize=16)
        self.create_mission_button = ToggleButton(self.nav_panel, Title= "Create mission", BackGround= self.__ui_colour.BLUE_DARK, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=True, TextSize=16)


        # Bind events
        self.hardware_check_button.GetObject().Bind(wx.EVT_BUTTON, self.handle_changeState_hardware_check)
        self.AI_setting_button.GetObject().Bind(wx.EVT_BUTTON, self.handle_changeState_AI_setting)
        self.create_mission_button.GetObject().Bind(wx.EVT_BUTTON, self.handle_changeState_create_misstion)
        
        # Layout navigation panel.
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.hardware_check_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 10)
        layout.Add(self.AI_setting_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 10)
        layout.Add(self.create_mission_button.GetObject(), 7, wx.EXPAND|wx.RIGHT)
        
        self.nav_panel.SetSizer(layout)
        self.nav_panel.Layout()

    def handle_changeState_hardware_check(self, event):
        self.hardware_check_button.onSelect(None)
        self.AI_setting_button.onDisable(None)
        self.create_mission_button.onDisable(None)
    def handle_changeState_AI_setting(self, event):
        self.hardware_check_button.onDisable(None)
        self.AI_setting_button.onSelect(None)
        self.create_mission_button.onDisable(None)
    def handle_changeState_create_misstion(self, event):
        self.hardware_check_button.onDisable(None)
        self.AI_setting_button.onDisable(None)
        self.create_mission_button.onSelect(None)
        


    def GetObject(self):
        return self.nav_panel