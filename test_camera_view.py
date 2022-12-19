import wx
import cv2
import nanocamera as nano

class ImagePanel(wx.Panel):

    def __init__(self, parent, fps):
        super().__init__(parent)
        self.fps = fps
        self.vs = camera = nano.Camera(camera_type=1, device_id=0, width=640, height=480, fps=15, enforce_fps=True)      

        frame = self.vs.read()
        # if not ret:
        #     print("Error")

        # Set panel size = frame size
        frame_height, frame_width, layers = frame.shape
        self.SetSize((frame_width, frame_height))

        # Change frane color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create buffer to store frame
        self.bmp = wx.Bitmap.FromBuffer(frame_width, frame_height, frame)

        # Set timer to update buffer
        self.timer = wx.Timer(self)
        self.timer.Start(int(1000.0 / self.fps))

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        frame = self.vs.read()
        # height, width, layers = frame.shape
        # print("Width, Height of frameeeee:", width, height)
        # print(self.vs.isReady())

        # if frame is not None:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.bmp.CopyFromBuffer(frame)
        self.Refresh()


class MainFrame(wx.Frame):

    def __init__(self):

        super().__init__(None, title='User stream')

        image_panel = ImagePanel(self, 10)

        img_panel_width, img_panel_height = image_panel.GetSize()

        self.SetSize(wx.Size(img_panel_width, img_panel_height))

        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()