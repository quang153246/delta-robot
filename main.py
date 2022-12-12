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
        self.operation = OperationTab(self.main_frame).GetObject()
        self.setting = SettingTab(self.main_frame).GetObject()

        # Layout main frame.
        main_layout = wx.BoxSizer(wx.VERTICAL)
        main_layout.Add(self.navigation, 1, wx.EXPAND|wx.ALL, 0)
        main_layout.Add(self.setting, 10, wx.EXPAND|wx.ALL, 0)
        self.main_frame.SetSizer(main_layout)
        self.main_frame.Layout()


    def show(self):
        self.main_frame.Show(True)

if __name__ == "__main__":
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show()
    app.MainLoop()



# import random
# import wx
 
# ########################################################################
# class TabPanel(wx.Panel):
#     #----------------------------------------------------------------------
#     def __init__(self, parent, page):
#         """"""
#         wx.Panel.__init__(self, parent=parent)
#         self.page = page
 
#         colors = ["red", "gray", "yellow", "green"]
#         self.SetBackgroundColour(random.choice(colors))
 
#         btn = wx.Button(self, label="Change Selection")
#         btn.Bind(wx.EVT_BUTTON, self.remove)
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(btn, 0, wx.ALL, 10)
#         self.SetSizer(sizer)
        
#     #----------------------------------------------------------------------
#     def onChangeSelection(self, event):
#         """
#         Change the page!
#         """
#         notebook = self.GetParent()
#         notebook.SetSelection(self.page)
#     def remove(self, event):
#         self.Destroy()
 
# ########################################################################
# class DemoFrame(wx.Frame):
#     """
#     Frame that holds all other widgets
#     """
 
#     #----------------------------------------------------------------------
#     def __init__(self):
#         """Constructor"""        
#         wx.Frame.__init__(self, None, wx.ID_ANY, 
#                           "Notebook Tutorial",
#                           size=(600,400)
#                           )
#         panel = wx.Panel(self)
 
#         notebook = wx.Notebook(panel)
        
#         tabOne = TabPanel(notebook, 1)
#         # tabOne =   OperationTab(notebook).GetObject()
#         notebook.AddPage(tabOne, "Operation")

#         tabTwo = TabPanel(notebook, 2)
#         # tabTwo = SettingTab(notebook).GetObject()
#         notebook.AddPage(tabTwo, "Settings")
 
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
#         panel.SetSizer(sizer)
#         self.Layout()
 
#         self.Show()
 
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = DemoFrame()
#     app.MainLoop()