from colour import UIColour
import wx
from components.Navigation import Navigation
from tabs.operation.Operation import OperationTab
from tabs.setting.Setting import SettingTab

class MainFrame():
    def __init__(self) -> None:
        # Create main frame of the GUI and set it maximize.
        self.__ui_colour = UIColour()
        self.main_frame = wx.Frame(None, style=wx.NO_BORDER)
        self.main_frame.SetBackgroundColour(self.__ui_colour.white)
        self.main_frame.Maximize()

        # NavBar
        self.navigation = Navigation(self.main_frame).GetObject()

        # Tab
        # self.operation = OperationTab(self.main_frame).GetObject()
        # self.setting = SettingTab(self.main_frame).GetObject()

        # Layout main frame.
        main_layout = wx.BoxSizer(wx.VERTICAL)
        main_layout.Add(self.navigation, 1, wx.EXPAND|wx.ALL, 0)
        # main_layout.Add(self.setting, 10, wx.EXPAND|wx.ALL, 0)
        self.main_frame.SetSizer(main_layout)
        self.main_frame.Layout()


    def show(self):
        self.main_frame.Show(True)

if __name__ == "__main__":
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show()
    app.MainLoop()

