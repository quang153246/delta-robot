import wx

class CustomButton():
    def __init__(self, parent, title, BackColor, TextColor) -> None:
        self.parent = parent
        self.button = wx.Button(self.parent, style=wx.BORDER_NONE, label=title)
        self.button.SetBackgroundColour(BackColor)
        self.button.SetForegroundColour(TextColor)
        self.button.SetFont(wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD))


    def GetObject(self):
        return self.button