import wx
from components.Button import CustomButton
from colour import UIColour

class Navigation():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.logoPath = "./image/TMA_logo.PNG"

        self.navigation_panel = wx.Panel(self.parent)
        self.navigation_panel.SetBackgroundColour(self.__ui_colour.black)

        self.operation_button = CustomButton(self.navigation_panel, "Operation", self.__ui_colour.PRIMARY, self.__ui_colour.white).GetObject() 

        self.settings_button = CustomButton(self.navigation_panel, "Settings", self.__ui_colour.PRIMARY, self.__ui_colour.white).GetObject()

        # Create navigation logo.
        self.logo_panel = wx.Panel(self.navigation_panel)
        logo_width, logo_height = self.logo_panel.GetSize()
        self.logo_image = wx.Image(self.logoPath).Scale(int(logo_width)*7, int(logo_height)*5, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        self.logo_bitmap = wx.StaticBitmap(self.logo_panel)
        self.logo_bitmap.SetBitmap(self.logo_image)
        
        # Layout navigation panel.
        navigation_layout = wx.BoxSizer(wx.HORIZONTAL)
        navigation_layout.Add(self.operation_button, 7, wx.EXPAND|wx.RIGHT, 1)
        navigation_layout.Add(self.settings_button, 7, wx.EXPAND|wx.RIGHT, 1)
        navigation_layout.Add(self.logo_panel, 1, wx.EXPAND|wx.RIGHT, 1)
        
        self.navigation_panel.SetSizer(navigation_layout)
        self.navigation_panel.Layout()


    def GetObject(self):
        return self.navigation_panel