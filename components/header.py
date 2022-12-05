import wx

class CustomHeader():
    def __init__(self, parent, title=None, BackColor=None, TextColor=None) -> None:
        self.parent = parent
        self.panel = wx.Panel(self.parent)

        self.panel.SetBackgroundColour(BackColor)

        if TextColor != None:
            self.panel.SetForegroundColour(TextColor)

            # Create header text for panel.
            self.panel_text = wx.StaticText(self.panel)
            self.panel_text.SetLabel(title)
            self.panel_text.SetForegroundColour(TextColor)
            self.panel_text.SetFont(wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD))

            # Layout panel.
            panel_layout_vertical = wx.BoxSizer(wx.VERTICAL)
            panel_layout_horizontal = wx.BoxSizer(wx.HORIZONTAL)
            width, height = self.panel.GetSize()
            panel_layout_horizontal.Add(self.panel_text, 1, wx.ALIGN_CENTER, int(height/3))
            panel_layout_vertical.Add(panel_layout_horizontal, 1, wx.ALIGN_CENTER, int(width/3))
            self.panel.SetSizer(panel_layout_vertical)
            self.panel.Layout()


    def GetObject(self):
        return self.panel