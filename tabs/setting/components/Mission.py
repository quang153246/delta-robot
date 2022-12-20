import wx
from colour import UIColour
from components.Header import CustomHeader
from components.ToggleButton import ToggleButton
from components.Form import Form

class Mission():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()

        self.panel = wx.Panel(self.parent)

        self.mission_list = wx.Panel(self.panel)
        self.mission_list_label = CustomHeader(self.mission_list, "Mission List:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 14, False).GetObject()
        self.mission_list_table = wx.Panel(self.mission_list)
        mission_list_layout = wx.BoxSizer(wx.VERTICAL)
        mission_list_layout.Add(self.mission_list_label, 1, wx.EXPAND)
        mission_list_layout.Add(self.mission_list_table, 10, wx.EXPAND)
        self.mission_list.SetSizer(mission_list_layout)
        self.mission_list.Layout()




        self.mission_control = wx.Panel(self.panel)
        self.mission_control_label = CustomHeader(self.mission_control, "Mission:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 15, False).GetObject()


        self.name_input = Form(self.mission_control, "Name:", self.__ui_colour.BLACK, "name").GetObject()
        self.start_time_input = Form(self.mission_control, "Start time:", self.__ui_colour.BLACK, "start_time").GetObject()
        self.stop_time_input = Form(self.mission_control, "Stop time:", self.__ui_colour.BLACK, "stop_time").GetObject()

        
        self.create_btn_group = wx.Panel(self.mission_control)
        self.save_btn = ToggleButton(self.create_btn_group, Title= "Save", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround = self.__ui_colour.BLUE_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14,callback=self.onSave).GetObject()
        self.reset_btn = ToggleButton(self.create_btn_group, Title= "Reset", BackGround= self.__ui_colour.GRAY_MAIN, SubBackGround = self.__ui_colour.GRAY_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14,callback=self.onReset).GetObject()
        create_btn_group_layout = wx.BoxSizer(wx.HORIZONTAL)
        create_btn_group_layout.Add(self.save_btn, 1 , wx.EXPAND| wx.ALL, 15)
        create_btn_group_layout.Add(self.reset_btn, 1 , wx.EXPAND| wx.ALL, 15)
        self.create_btn_group.SetSizer(create_btn_group_layout)
        self.create_btn_group.Layout()

        self.action_btn_group = wx.Panel(self.mission_control)
        self.update_btn = ToggleButton(self.action_btn_group, Title= "Update", BackGround= self.__ui_colour.GREEN_MAIN, SubBackGround = self.__ui_colour.GREEN_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14,callback=self.onEdit).GetObject()
        self.delete_btn = ToggleButton(self.action_btn_group, Title= "Delete", BackGround= self.__ui_colour.RED_MAIN, SubBackGround = self.__ui_colour.RED_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14, callback=self.onDelete).GetObject()
        action_btn_group_layout = wx.BoxSizer(wx.HORIZONTAL)
        action_btn_group_layout.Add(self.update_btn, 1 , wx.EXPAND | wx.ALL, 15)
        action_btn_group_layout.Add(self.delete_btn, 1 , wx.EXPAND | wx.ALL, 15)
        self.action_btn_group.SetSizer(action_btn_group_layout)
        self.action_btn_group.Layout()


        mission_control_layout = wx.BoxSizer(wx.VERTICAL)
        mission_control_layout.Add(self.mission_control_label, 1 , wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        mission_control_layout.Add(self.name_input, 1 , wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        mission_control_layout.Add(self.start_time_input, 1 , wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        mission_control_layout.Add(self.stop_time_input, 1 , wx.EXPAND|wx.LEFT|wx.RIGHT, 15)
        mission_control_layout.Add(self.create_btn_group, 2 , wx.EXPAND|wx.TOP, 10)
        mission_control_layout.Add(self.action_btn_group, 2 , wx.EXPAND|wx.TOP, 10)
        self.mission_control.SetSizer(mission_control_layout)
        self.mission_control.Layout()


        panel_layout = wx.BoxSizer(wx.HORIZONTAL)
        panel_layout.Add(self.mission_list, 2, wx.EXPAND)
        panel_layout.Add(self.mission_control, 3, wx.EXPAND)
        self.panel.SetSizer(panel_layout)
        self.panel.Layout()


    def GetObject(self):
        return self.panel

    def onSave(self):
        print("Save")

    def onReset(self):
        print("Reset")

    def onEdit(self):
        print("Edit")

    def onDelete(self):
        print("Delete")





