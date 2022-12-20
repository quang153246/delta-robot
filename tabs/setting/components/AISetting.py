import wx
from colour import UIColour
from components.Header import CustomHeader
from components.ToggleButton import ToggleButton
from components.VideoFrame import VideoFrame

class AISetting():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()

        self.panel = wx.Panel(self.parent)
        self.panel.SetBackgroundColour(self.__ui_colour.WHITE)

        #Video
        self.content = wx.Panel(self.panel)
            #components for Video Box
        self.note = CustomHeader(self.content, "Mandatory for the robot operation *", self.__ui_colour.WHITE, self.__ui_colour.RED_MAIN, 14, False).GetObject()
        self.video_label = CustomHeader(self.content, "Stream output:​", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 14, False).GetObject()
        # self.video_box = VideoFrame(self.content, 30).GetObject()

        
        # self.video_box = wx.Panel(self.content)
        # self.video_box.SetBackgroundColour(self.__ui_colour.GRAY_LIGHT)

        # video_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        # video_box_layout_sub = wx.BoxSizer(wx.VERTICAL)

        # self.stream_video = VideoFrame(self.video_box, 30).GetObject()

        # video_box_layout.Add(self.stream_video, 1, wx.EXPAND|wx.TOP|wx.BOTTOM,32)
        # video_box_layout_sub.Add(video_box_layout, 1, wx.EXPAND|wx.LEFT|wx.RIGHT,360 )
        # self.video_box.SetSizer(video_box_layout_sub)
        # self.video_box.Layout()


        content_layout_v = wx.BoxSizer(wx.VERTICAL)
        content_layout_v.Add(self.note, 1, wx.EXPAND|wx.ALL, 0)
        content_layout_v.Add(self.video_label, 1, wx.EXPAND|wx.ALL, 0)
        # content_layout_v.Add(self.video_box, 8, wx.EXPAND|wx.ALL, 0)

        self.content.SetSizer(content_layout_v)
        self.content.Layout()

        #Configuration
        self.configuration = wx.Panel(self.panel)
        self.select_model_label = CustomHeader(self.configuration, "Step 1:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 15, False).GetObject()
        self.select_model_button = ToggleButton(self.configuration, Title= "Select model", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround = self.__ui_colour.BLUE_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14)
        self.adjust_frame_label = CustomHeader(self.configuration, "Step 2:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 15, False).GetObject()
        self.adjust_frame_button = ToggleButton(self.configuration, Title= "Adjust frame", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround = self.__ui_colour.BLUE_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14)
        self.move_arm_label = CustomHeader(self.configuration, "Step 3:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 15, False).GetObject()
        self.move_arm_button = ToggleButton(self.configuration, Title= "Move arm", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround = self.__ui_colour.BLUE_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14)
        self.confirm_obj_label = CustomHeader(self.configuration, "Step 4:", self.__ui_colour.WHITE, self.__ui_colour.BLACK, 15, False).GetObject()
        self.confirm_obj_button = ToggleButton(self.configuration, Title= "Confirm object position", BackGround= self.__ui_colour.BLUE_MAIN, SubBackGround = self.__ui_colour.BLUE_DARK,TextColor= self.__ui_colour.white, State=False, TextSize=14)

        #Bind event for buttons
        self.select_model_button.GetObject().Bind(wx.EVT_BUTTON, self.onSelectModel)
        self.adjust_frame_button.GetObject().Bind(wx.EVT_BUTTON, self.onAdjustFrame)
        self.move_arm_button.GetObject().Bind(wx.EVT_BUTTON, self.onMoveArm)
        self.confirm_obj_button.GetObject().Bind(wx.EVT_BUTTON, self.onConfirm)


        configuration_layout =wx.BoxSizer(wx.VERTICAL)
        configuration_layout.Add(self.select_model_label, 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.select_model_button.GetObject(), 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.adjust_frame_label, 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.adjust_frame_button.GetObject(), 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.move_arm_label, 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.move_arm_button.GetObject(), 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.confirm_obj_label, 1 , wx.EXPAND|wx.ALL, 0)
        configuration_layout.Add(self.confirm_obj_button.GetObject(), 1 , wx.EXPAND|wx.ALL, 0)

        self.configuration.SetSizer(configuration_layout)
        self.configuration.Layout()


        # ========= Gather =============
        panel_layout_h = wx.BoxSizer(wx.HORIZONTAL)
        panel_layout_h.Add(self.content, 2, wx.EXPAND|wx.ALL, 20)
        panel_layout_h.Add(self.configuration, 1, wx.EXPAND|wx.ALL, 20)
        self.panel.SetSizer(panel_layout_h)
        self.panel.Layout()

    def GetObject(self):
        return self.panel
    def onSelectModel(self, event):
        print("select model")
    def onAdjustFrame(self, event):
        print("Adjust Frame")
    def onMoveArm(self, event):
        print("Move Arm")
    def onConfirm(self, event):
        print("Confirm")