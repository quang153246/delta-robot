import wx

########################################################################
class Mission:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, id, name, startTime, stopTime):
        """Constructor"""
        self.id = id
        self.name = name
        self.startTime = startTime
        self.stopTime = stopTime

########################################################################
class Select():

    #----------------------------------------------------------------------
    def __init__(self, parent) -> None:
        # wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")

        # Add a panel so it looks the correct on all platforms
        self.parent = parent
        self.panel = wx.Panel(self.parent)

        missions = [Mission(0, "Ca Sáng", "123144", "2132132"),
                Mission(1, "Ca Chiều", "2225252", "12315324")]

        sampleList = []
        self.cb = wx.ComboBox(self.panel, size=wx.DefaultSize, choices=sampleList, name="mission_select")
        self.cb.SetSize((300,-1))
        self.widgetMaker(self.cb, missions)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cb, 1, flag=wx.EXPAND|wx.ALL, border=0)

        self.panel.SetSizer(sizer)
        self.panel.Bind(wx.EVT_COMBOBOX, self.onSelect)

    #----------------------------------------------------------------------
    def widgetMaker(self, widget, objects):
        
        for obj in objects:
            widget.Append(obj.name, obj)

    #----------------------------------------------------------------------
    def onSelect(self, event):
        print ("You selected: " + self.cb.GetStringSelection())
        obj = self.cb.GetClientData(self.cb.GetSelection())
        text = """ The object's attributes are: %s  %s    %s  %s""" % (obj.id, obj.name, obj.startTime, obj.stopTime)
        print(text)

    def GetObject(self):
        return self.panel
