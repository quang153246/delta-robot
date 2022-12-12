import wx
from colour import UIColour
import wx
from components.ToggleButton import ToggleButton
from components.Header import CustomHeader
from components.SettingNav import SettingNav
from components.VideoFrame import VideoFrame
from components.Form import Form

class HardwareCheck():
    def __init__(self, parent) -> None:
        self.parent = parent
