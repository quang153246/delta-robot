import wx
from components.ToggleButton import ToggleButton
from colour import UIColour
from tabs.operation.Operation import OperationTab
from tabs.setting.Setting import SettingTab

class Navigation():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()
        self.logoPath = "./image/TMA_logo.PNG"

        # create App panel
        self.app = wx.Panel(self.parent)
        # create root Navigation 
        self.navigation_panel = wx.Panel(self.app)
        self.navigation_panel.SetBackgroundColour(self.__ui_colour.BLACK)

        self.operation_button = ToggleButton(self.navigation_panel, Title= "Operation", BackGround= self.__ui_colour.BLUE_DARK, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=22)

        self.settings_button = ToggleButton(self.navigation_panel, Title= "Settings", BackGround= self.__ui_colour.BLUE_DARK,SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=True, TextSize=22)

        # Bind events for button
        self.operation_button.GetObject().Bind(wx.EVT_BUTTON, self.operation_button_changeState)
        self.settings_button.GetObject().Bind(wx.EVT_BUTTON, self.settings_button_changeState)

        # Create logo.
        self.logo_panel = wx.Panel(self.navigation_panel)
        logo_width, logo_height = self.logo_panel.GetSize()
        self.logo_image = wx.Image(self.logoPath).Scale(int(logo_width)*5, int(logo_height)*3, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        self.logo_bitmap = wx.StaticBitmap(self.logo_panel)
        self.logo_bitmap.SetBitmap(self.logo_image)
        
        # Layout navigation panel.
        navigation_layout = wx.BoxSizer(wx.HORIZONTAL)
        navigation_layout.Add(self.operation_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 5)
        navigation_layout.Add(self.settings_button.GetObject(), 7, wx.EXPAND|wx.RIGHT, 5)
        navigation_layout.Add(self.logo_panel, 1, wx.EXPAND|wx.RIGHT, 1)
        
        self.navigation_panel.SetSizer(navigation_layout)
        self.navigation_panel.Layout()


        #========================================= CONTENT ========================================================
        # create content panel
        self.content = wx.Panel(self.app)

        # define tabs
        self.operation = OperationTab(self.content).GetObject()
        self.setting = SettingTab(self.content)
        self.setting_panel = self.setting.GetObject()
        self.panels = [self.operation, self.setting_panel]  # tabs array

        # layout for content_panel
        content_layout = wx.BoxSizer(wx.HORIZONTAL)
        # add all tab into content_panel
        for panel in self.panels:
            content_layout.Add(panel, 1, wx.EXPAND)
        # Show the first panel and hide the rest of panels
        self.Show(self.panels[0])

        self.content.SetSizer(content_layout)
        self.content.Layout()


        app_layout = wx.BoxSizer(wx.VERTICAL)
        app_layout.Add(self.navigation_panel, 1, wx.EXPAND|wx.ALL, 0)
        app_layout.Add(self.content, 10, wx.EXPAND|wx.ALL, 0)
        self.app.SetSizer(app_layout)
        self.app.Layout()

    # When click one of two buttons, the clicked button will be highlight and other will be disable
    def operation_button_changeState(self, event):
        self.operation_button.onSelect(None)
        self.settings_button.onDisable(None)
        self.setting.stop_stream()
        self.Show(self.operation)
        

    def settings_button_changeState(self, event):
        self.settings_button.onSelect(None)
        self.operation_button.onDisable(None)
        self.Show(self.setting_panel)
        


    def GetObject(self):
        return self.app


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