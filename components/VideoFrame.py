import wx
import cv2
from colour import UIColour


class VideoFrame():

    def __init__(self, parent):
        self.image_panel = wx.Panel(parent)
        self.frame_width = 640
        self.frame_height = 480
        print("Width, Height of frameeeee:", self.frame_width, self.frame_height)
        # self.image_panel.SetSize((self.frame_width, self.frame_height))
        self.image_panel.SetBackgroundColour(UIColour().BLACK)

        # Change frane color and flip image
        # frame = cv2.flip(frame, 1)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create buffer to store frame
        # frame = np.zeros([self.frame_height, self.frame_width], dtype=int)
        # self.bmp = wx.Bitmap.FromBuffer(self.frame_width, self.frame_height, frame)

        # Set timer to update buffer
        # self.timer = wx.Timer(self.image_panel)
        # self.timer.Start(int(1000.0 / self.fps))

        # self.image_panel.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.image_panel.Bind(wx.EVT_TIMER, self.NextFrame)

    # def OnPaint(self, evt):
    #     dc = wx.BufferedPaintDC(self.image_panel)
    #     dc.DrawBitmap(self.bmp, 0, 0)

    # def NextFrame(self, event):
    #     ret, frame = self.cap.read()
    
    #     if ret:
    #         frame = cv2.flip(frame, 1)
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         self.bmp.CopyFromBuffer(frame)
    #         self.image_panel.Refresh()

    def GetObject(self):
        # print(self.image_panel)
        return self.image_panel

    def GetBuffer(self):
        return self.bmp
