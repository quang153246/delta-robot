import wx
from components.ToggleButton import ToggleButton
from colour import UIColour

class Navigation():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.logoPath = "./image/TMA_logo.PNG"

        self.navigation_panel = wx.Panel(self.parent)
        self.navigation_panel.SetBackgroundColour(self.__ui_colour.BLACK)

        self.operation_button = ToggleButton(self.navigation_panel, Title= "Operation", BackGround= self.__ui_colour.BLUE_DARK, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=22)

        self.settings_button = ToggleButton(self.navigation_panel, Title= "Settings", BackGround= self.__ui_colour.BLUE_DARK,SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=True, TextSize=22)

        # Bind events
        self.operation_button.GetObject().Bind(wx.EVT_BUTTON, self.operation_button_changeState)
        self.settings_button.GetObject().Bind(wx.EVT_BUTTON, self.settings_button_changeState)
        # Create navigation logo.
        self.logo_panel = wx.Panel(self.navigation_panel)
        logo_width, logo_height = self.logo_panel.GetSize()
        self.logo_image = wx.Image(self.logoPath).Scale(int(logo_width)*7, int(logo_height)*5, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        self.logo_bitmap = wx.StaticBitmap(self.logo_panel)
        self.logo_bitmap.SetBitmap(self.logo_image)
        
        # Layout navigation panel.
        navigation_layout = wx.BoxSizer(wx.HORIZONTAL)
        navigation_layout.Add(self.operation_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 10)
        navigation_layout.Add(self.settings_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 10)
        navigation_layout.Add(self.logo_panel, 1, wx.EXPAND|wx.RIGHT, 1)
        
        self.navigation_panel.SetSizer(navigation_layout)
        self.navigation_panel.Layout()

    def operation_button_changeState(self, event):
        self.operation_button.onSelect(None)
        self.settings_button.onDisable(None)
    def settings_button_changeState(self, event):
        self.settings_button.onSelect(None)
        self.operation_button.onDisable(None)
        


    def GetObject(self):
        return self.navigation_panel