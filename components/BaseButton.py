import wx
from colour import UIColour

class BaseButton():

    def __init__(self, parent, title, BackGround, TextColor, TextSize = None) -> None:
        self.__ui_colour = UIColour()

        if (TextSize == None):
            TextSize = 14

        self.button_state = False
        self.parent = parent
        self.button = wx.Button(self.parent, style=wx.BORDER_NONE, label=title)
        self.button.SetBackgroundColour(BackGround)
        self.button.SetForegroundColour(TextColor)
        self.button.SetFont(wx.Font(TextSize, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        self.button.Bind(wx.EVT_BUTTON, self.onToggle)
        # self.button.Bind(wx.EVT_MOTION, self.onMove)
   
    def onMove(self, event):
        img = wx.Image('./image/pointer_50x50.png')
        crsr = wx.Cursor(img)
        self.button.SetCursor(crsr)

    def onToggle(self, event):
        self.button_state = not(self.button_state)
        print(self.button_state)
        if self.button_state == True:
            self.button.SetBackgroundColour(self.__ui_colour.GRAY_LIGHT)
        else:
            self.button.SetBackgroundColour(self.__ui_colour.GRAY_DARK)


    def GetObject(self):
        return self.button