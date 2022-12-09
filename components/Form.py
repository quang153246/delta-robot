import wx
from components.Header import CustomHeader
from colour import UIColour


class Form():
    def __init__(self, parent, label, textColor, key) -> None:
        self.__ui_colour = UIColour()
        self.parent = parent
        self.key = key

        self.form = wx.Panel(self.parent)

        self.form_label = CustomHeader(self.form, label, self.__ui_colour.WHITE, textColor).GetObject()
        self.form_input = wx.TextCtrl(self.form, -1, "")

        self.form_layout = wx.BoxSizer(wx.HORIZONTAL)
        self.form_layout.Add(self.form_label, 1, wx.EXPAND|wx.ALL, 5)
        self.form_layout.Add(self.form_input, 3, wx.EXPAND|wx.ALL, 5)
        self.form.SetSizer(self.form_layout)
        self.form.Layout()


    def GetObject(self):
        return self.form