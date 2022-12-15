import wx
from components.ToggleButton import ToggleButton
from colour import UIColour
from tabs.setting.components.Hardware import Hardware
from tabs.setting.components.AISetting import AISetting
from tabs.setting.components.Mission import Mission


class SettingNav():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.wrapper =  wx.Panel(self.parent)

        self.nav_panel = wx.Panel(self.wrapper)
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
        layout.Add(self.hardware_check_button.GetObject(), 1, wx.EXPAND|wx.RIGHT, 10)
        layout.Add(self.AI_setting_button.GetObject(), 1, wx.EXPAND|wx.RIGHT, 10)
        layout.Add(self.create_mission_button.GetObject(), 1, wx.EXPAND|wx.RIGHT)
        
        self.nav_panel.SetSizer(layout)
        self.nav_panel.Layout()

        #===============================================================
        self.content = wx.Panel(self.wrapper)
        content_layout = wx.BoxSizer(wx.HORIZONTAL)

        self.hardware = Hardware(self.content).GetObject()
        self.AI_setting = AISetting(self.content).GetObject()
        self.mission = Mission(self.content).GetObject()
        self.panels = [self.hardware, self.AI_setting, self.mission]

        
        for panel in self.panels:
            content_layout.Add(panel, 1 , wx.EXPAND)
        self.Show(self.panels[0])

        self.content.SetSizer(content_layout)
        self.content.Layout()


        app_layout = wx.BoxSizer(wx.VERTICAL)
        app_layout.Add(self.nav_panel, 1, wx.EXPAND|wx.ALL, 0)
        app_layout.Add(self.content, 10, wx.EXPAND|wx.ALL, 0)
        self.wrapper.SetSizer(app_layout)
        self.wrapper.Layout()

    def handle_changeState_hardware_check(self, event):
        self.hardware_check_button.onSelect(None)
        self.AI_setting_button.onDisable(None)
        self.create_mission_button.onDisable(None)
        self.Show(self.hardware)
    def handle_changeState_AI_setting(self, event):
        self.hardware_check_button.onDisable(None)
        self.AI_setting_button.onSelect(None)
        self.create_mission_button.onDisable(None)
        self.Show(self.AI_setting)

    def handle_changeState_create_misstion(self, event):
        self.hardware_check_button.onDisable(None)
        self.AI_setting_button.onDisable(None)
        self.create_mission_button.onSelect(None)
        self.Show(self.mission)
        


    def GetObject(self):
        return self.wrapper
   # Show some panel and hide the rest of panels
    def Show(self, panel):
        # For each panel in the list of panels
        for p in self.panels:
            # Show the given panel
            if p == panel:
                p.Show()
            else:
                # and hide the rest
                p.Hide()
        # Rearrange the window
        self.parent.Layout()