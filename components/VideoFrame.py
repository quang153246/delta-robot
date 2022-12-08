import wx
import cv2

class ImagePanel():

    def __init__(self, parent, fps):
        self.image_panel = wx.Panel(parent)
        self.fps = fps
        self.vs = cv2.VideoCapture(0)       

        ret, frame = self.vs.read()
        if not ret:
            print("Error")

        # Set panel size = frame size
        frame_height, frame_width, layers = frame.shape
        print("Width, Height of frameeeee:", frame_width, frame_height)
        self.image_panel.SetSize((frame_width, frame_height))

        # Change frane color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create buffer to store frame
        self.bmp = wx.Bitmap.FromBuffer(frame_width, frame_height, frame)

        # Set timer to update buffer
        self.timer = wx.Timer(self.image_panel)
        self.timer.Start(int(1000.0 / self.fps))

        self.image_panel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.image_panel.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self.image_panel)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.vs.read()
        # height, width, layers = frame.shape
        # print("Width, Height of frameeeee:", width, height)

        if ret:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.image_panel.Refresh()

    def GetObject(self):
        return self.image_panel