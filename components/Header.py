import wx

class CustomHeader():
    def __init__(self, parent, title=None, BackGround=None, TextColor=None, TextSize=None, isCenter = True) -> None:
        self.parent = parent
        self.panel = wx.Panel(self.parent)
        self.panel.SetBackgroundColour(BackGround)

        if TextSize == None:
            TextSize = 14

        if TextColor != None:
            self.panel.SetForegroundColour(TextColor)

            # Create header text for panel.
            self.panel_text = wx.StaticText(self.panel)
            self.panel_text.SetLabel(title)
            self.panel_text.SetForegroundColour(TextColor)
            self.panel_text.SetFont(wx.Font(TextSize, wx.DECORATIVE, wx.NORMAL, wx.BOLD))

        # Layout panel.
        panel_layout_vertical = wx.BoxSizer(wx.VERTICAL)
        panel_layout_horizontal = wx.BoxSizer(wx.HORIZONTAL)
        # width, height = self.panel.GetSize()
        panel_layout_horizontal.Add(self.panel_text, 1, wx.ALIGN_CENTER)
        if (isCenter == True):
            panel_layout_vertical.Add(panel_layout_horizontal, 1, wx.ALIGN_CENTER)
            self.panel.SetSizer(panel_layout_vertical)
        else:
            self.panel.SetSizer(panel_layout_horizontal)

        self.panel.Layout()
    

    def GetObject(self):
        return self.panel
    def Set_Label(self, label):
        self.panel_text.SetLabel(label)
