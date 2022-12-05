from colour import UIColour
import wx
from components.button import CustomButton
from components.header import CustomHeader

class MainFrame():
    def __init__(self) -> None:
        # Create main frame of the GUI and set it maximize.
        self.__ui_colour = UIColour()
        self.main_frame = wx.Frame(None, style=wx.NO_BORDER)
        self.main_frame.SetBackgroundColour(self.__ui_colour.white)
        self.main_frame.Maximize()

        # Create navigation panel and navigation buttons (Operation, Settings).
        self.navigation_panel = wx.Panel(self.main_frame)
        self.navigation_panel.SetBackgroundColour(self.__ui_colour.black)

        self.operation_button = CustomButton(self.navigation_panel, "Operation", self.__ui_colour.true_blue, self.__ui_colour.white).GetObject() 

        self.settings_button = CustomButton(self.navigation_panel, "Settings", self.__ui_colour.true_blue, self.__ui_colour.white).GetObject()

        # Create navigation logo.
        self.logo_panel = wx.Panel(self.navigation_panel)
        logo_width, logo_height = self.logo_panel.GetSize()
        self.logo_image = wx.Image("./image/TMA_logo.PNG").Scale(int(logo_width)*7, int(logo_height)*5, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        self.logo_bitmap = wx.StaticBitmap(self.logo_panel)
        self.logo_bitmap.SetBitmap(self.logo_image)
        
        # Layout navigation panel.
        navigation_layout = wx.BoxSizer(wx.HORIZONTAL)
        navigation_layout.Add(self.operation_button, 7, wx.EXPAND|wx.RIGHT, 1)
        navigation_layout.Add(self.settings_button, 7, wx.EXPAND|wx.RIGHT, 1)
        navigation_layout.Add(self.logo_panel, 1, wx.EXPAND|wx.RIGHT, 1)
        
        self.navigation_panel.SetSizer(navigation_layout)
        self.navigation_panel.Layout()

        # Create body panel.
        self.body_panel = wx.Panel(self.main_frame)
        self.body_panel.SetBackgroundColour(self.__ui_colour.black)

        # Create header mode.
        self.mode_header = CustomHeader(self.body_panel, "Operation", self.__ui_colour.white, self.__ui_colour.black).GetObject()

        # Create interface panel.
        self.interface_bar = wx.Panel(self.body_panel)
        self.interface_bar.SetBackgroundColour(self.__ui_colour.white)

        # Create header mission.
        self.mission_header = CustomHeader(self.interface_bar, "Choose Mission", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content mission.
        self.mission_content =  CustomHeader(self.interface_bar, BackColor=self.__ui_colour.white).GetObject()
        # Create enable run immediately button.
        self.run_immediately_button = CustomButton(self.interface_bar, "Enable run immediately", self.__ui_colour.deep_blue, self.__ui_colour.white).GetObject()

        # Create header control.
        self.control_header = CustomHeader(self.interface_bar, "Control", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content control.
        self.control_content =  CustomHeader(self.interface_bar, BackColor=self.__ui_colour.white).GetObject()

        # Create header connection status.
        self.connection_status_header = CustomHeader(self.interface_bar, "Connection Status", self.__ui_colour.black, self.__ui_colour.white).GetObject()
        # Create content connection status.
        self.connection_status_content =  CustomHeader(self.interface_bar, BackColor=self.__ui_colour.white).GetObject()

        # Layout interface panel.
        interface_bar_layout = wx.BoxSizer(wx.VERTICAL)
        interface_bar_layout.Add(self.mission_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.mission_content, 5, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.control_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.control_content, 5, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.connection_status_header, 1, wx.EXPAND|wx.ALL, 0)
        interface_bar_layout.Add(self.connection_status_content, 2, wx.EXPAND|wx.ALL, 0)
        self.interface_bar.SetSizer(interface_bar_layout)
        self.interface_bar.Layout()

        # Create monitor panel.
        self.monitor_bar = wx.Panel(self.body_panel)
        self.monitor_bar.SetBackgroundColour(self.__ui_colour.white)

        # Layout sub body panel (interface bar and monitor bar).
        sub_body_layout = wx.BoxSizer(wx.HORIZONTAL)
        sub_body_layout.Add(self.interface_bar, 1, wx.EXPAND|wx.ALL, 1)
        sub_body_layout.Add(self.monitor_bar, 2, wx.EXPAND|wx.ALL, 1)

        # Layout body panel (mode bar and sub body).
        body_layout = wx.BoxSizer(wx.VERTICAL)
        body_layout.Add(self.mode_header, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 1)
        body_layout.Add(sub_body_layout, 10, wx.EXPAND|wx.ALL, 1)
        self.body_panel.SetSizer(body_layout)
        self.body_panel.Layout()

        # Layout main frame.
        main_layout = wx.BoxSizer(wx.VERTICAL)
        main_layout.Add(self.navigation_panel, 1, wx.EXPAND|wx.ALL, 0)
        main_layout.Add(self.body_panel, 10, wx.EXPAND|wx.ALL, 0)
        self.main_frame.SetSizer(main_layout)
        self.main_frame.Layout()


    def show(self):
        self.main_frame.Show(True)

if __name__ == "__main__":
    app = wx.App()
    main_frame = MainFrame()
    main_frame.show()
    app.MainLoop()