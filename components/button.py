import wx
from colour import UIColour

class CustomButton():

    def __init__(self, parent, title, background, textColor) -> None:
        self.__ui_colour = UIColour()

        self.button_state = False
        self.parent = parent
        self.button = wx.Button(self.parent, style=wx.BORDER_NONE, label=title)
        self.button.SetBackgroundColour(background)
        self.button.SetForegroundColour(textColor)
        self.button.SetFont(wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        self.button.Bind(wx.EVT_BUTTON, self.onToggle)
        self.button.Bind(wx.EVT_MOTION, self.onMove)
    def onClick(self, event):
        print("Clicked")
    def onMove(self, event):
        print("Moving")
        # create wx.Image object
        img = wx.Image('./image/pointer_50x50.png')
          
        # create wx.Cursor object
        crsr = wx.Cursor(img)
        self.button.SetCursor(crsr)
    def onToggle(self, event):
        print("Toggle")
        self.button_state = not(self.button_state)
        print(self.button_state)
        if self.button_state == True:
            self.button.SetBackgroundColour(self.__ui_colour.GRAY_MAIN)
        else:
            self.button.SetBackgroundColour(self.__ui_colour.START_BUTTON)


    def GetObject(self):
        return self.button