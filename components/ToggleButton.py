import wx
import time
from colour import UIColour

class ToggleButton():

    def __init__(self, parent, Title, SubTitle = None , BackGround = None, SubBackGround = None , TextColor= None, SubTextColor = None, TextSize = None, State = False, callback = None) -> None:
        self.__ui_colour = UIColour()
        self.init_label = Title
        self.toggle_label = SubTitle
        self.init_backGround = BackGround
        self.toggle_backGround = SubBackGround
        self.init_textColor = TextColor
        self.toggle_textColor = SubTextColor
        self.callback = callback

        self.button_state = State | False

        if (TextSize == None):
            self.textSize = 14
        else:
            self.textSize = TextSize


        self.parent = parent
        self.button = wx.Button(self.parent, style=wx.BORDER_NONE, label = self.init_label)

        if (self.button_state == True):
            self.button.SetBackgroundColour(self.toggle_backGround)
        else:
            self.button.SetBackgroundColour(self.init_backGround)
        self.button.SetForegroundColour(self.init_textColor)
        self.button.SetFont(wx.Font(self.textSize, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        self.button.Bind(wx.EVT_BUTTON, self.onSelect)
        self.button.Bind(wx.EVT_MOTION, self.onMove)
        self.button.Bind(wx.EVT_BUTTON, self.onToggle)

    def onDisable(self, event):

        self.button_state == True
        self.button.SetBackgroundColour(self.toggle_backGround)
        if(self.toggle_label != None):
                self.button.SetLabel(self.toggle_label)

    def onSelect(self, event):
        self.button_state == False
        if(self.toggle_label != None):
            self.button.SetLabel(self.init_label)
        self.button.SetBackgroundColour(self.init_backGround)
        self.button.SetForegroundColour(self.init_textColor)


    def onMove(self, event):
        img = wx.Image('./image/pointer_50x50.png')
        crsr = wx.Cursor(img)
        self.button.SetCursor(crsr)

    def onToggle(self, event):
        if (self.callback != None):
            self.callback()
        self.getState = not(self.getState)
        if self.getState == False:
            self.button.SetBackgroundColour(self.toggle_backGround)
            if(self.toggle_label != None):
                self.button.SetLabel(self.toggle_label)
            if(self.toggle_textColor != None):
                self.button.SetForegroundColour(self.toggle_textColor)
        else:
            if(self.toggle_label != None):
                self.button.SetLabel(self.init_label)
            self.button.SetBackgroundColour(self.init_backGround)
            self.button.SetForegroundColour(self.init_textColor)

    def getState(self):
        return self.button_state

    def GetObject(self):
        return self.button