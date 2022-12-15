from colour import UIColour
import wx
from components.Header import CustomHeader
from components.VideoFrame import VideoFrame

class Monitor():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__ui_colour = UIColour()

         # Create monitor panel (wrapper) .
        self.monitor_tab = wx.Panel(self.parent)
        monitor_tab_w, monitor_tab_h = self.monitor_tab.GetSize()
        self.monitor_tab.SetBackgroundColour(self.__ui_colour.white)

        # --------Time Box--------
        self.time_box = wx.Panel(self.monitor_tab)
        time_box_layout = wx.BoxSizer(wx.HORIZONTAL)
        startTime = CustomHeader(self.time_box, "Start time: " + "7h AM", self.__ui_colour.white, self.__ui_colour.PRIMARY, 16).GetObject()
        currentTime = CustomHeader(self.time_box, "Current time: " + "9h AM", self.__ui_colour.white, self.__ui_colour.PRIMARY, 16).GetObject()
        stopTime = CustomHeader(self.time_box, "Stop time: " + "11h PM", self.__ui_colour.white, self.__ui_colour.PRIMARY, 16).GetObject()
        time_box_layout.Add(startTime, 1, wx.EXPAND|wx.ALL,0 )
        time_box_layout.Add(currentTime, 1, wx.EXPAND|wx.ALL,0 )
        time_box_layout.Add(stopTime, 1, wx.EXPAND|wx.ALL,0 )
        self.time_box.SetSizer(time_box_layout)
        self.time_box.Layout()

        # ----Video Box-----
        # Get video stream from camera

        # self.video_box = wx.Panel(self.monitor_tab)
        # self.video_box.SetBackgroundColour(self.__ui_colour.GRAY_LIGHT)

        # video_box_layout_h = wx.BoxSizer(wx.HORIZONTAL)
        # video_box_layout_v = wx.BoxSizer(wx.VERTICAL)

        # self.stream_video = VideoFrame(self.video_box, 30).GetObject()

        # video_box_layout_h.Add(self.stream_video, 1, wx.EXPAND|wx.TOP|wx.BOTTOM,100)
        # video_box_layout_v.Add(video_box_layout_h, 1, wx.EXPAND|wx.LEFT|wx.RIGHT,320 )
        # self.video_box.SetSizer(video_box_layout_v)
        # self.video_box.Layout()




        # ------ Result Box -------
        self.result_box = wx.Panel(self.monitor_tab)
        result_box_layout = wx.BoxSizer(wx.HORIZONTAL)

        not_good_items = CustomHeader(self.result_box, "Not Good Items: " + "100", self.__ui_colour.white, self.__ui_colour.GREEN_MAIN).GetObject()
        already_picked_items = CustomHeader(self.result_box, "Already_Picked_Items: " + "100", self.__ui_colour.white, self.__ui_colour.GREEN_MAIN).GetObject()
        result_box_layout.Add(not_good_items, 1, wx.EXPAND|wx.ALL, 1)
        result_box_layout.Add(already_picked_items, 1, wx.EXPAND|wx.ALL, 1)
   
        self.result_box.SetSizer(result_box_layout)
        self.result_box.Layout()


        # Layout for box of all components
        monitor_tab_layout = wx.BoxSizer(wx.VERTICAL)
        monitor_tab_layout.Add(self.time_box, 1 , wx.EXPAND|wx.ALL, 0)
        # monitor_tab_layout.Add(self.video_box, 6 , wx.EXPAND|wx.ALL, 0)
        monitor_tab_layout.Add(self.result_box, 10 , wx.EXPAND|wx.LEFT|wx.RIGHT, 10)

        self.monitor_tab.SetSizer(monitor_tab_layout)
        self.monitor_tab.Layout()

    def GetObject(self):
        return self.monitor_tab