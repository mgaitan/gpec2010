import wx
from FoldPanelBar import *

#----------------------------------------------------------------------
# Some Icon Data For The Frame's Cosmetics...
#----------------------------------------------------------------------

def GetMondrianData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00qID\
ATX\x85\xed\xd6;\n\x800\x10E\xd1{\xc5\x8d\xb9r\x97\x16\x0b\xad$\x8a\x82:\x16\
o\xda\x84pB2\x1f\x81Fa\x8c\x9c\x08\x04Z{\xcf\xa72\xbcv\xfa\xc5\x08 \x80r\x80\
\xfc\xa2\x0e\x1c\xe4\xba\xfaX\x1d\xd0\xde]S\x07\x02\xd8>\xe1wa-`\x9fQ\xe9\
\x86\x01\x04\x10\x00\\(Dk\x1b-\x04\xdc\x1d\x07\x14\x98;\x0bS\x7f\x7f\xf9\x13\
\x04\x10@\xf9X\xbe\x00\xc9 \x14K\xc1<={\x00\x00\x00\x00IEND\xaeB`\x82' 

def GetMondrianBitmap():
    return wx.BitmapFromImage(GetMondrianImage())

def GetMondrianImage():
    import cStringIO
    stream = cStringIO.StringIO(GetMondrianData())
    return wx.ImageFromStream(stream)

def GetMondrianIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon

#----------------------------------------------------------------------


class FoldTestPanel(wx.Panel):

    def __init__(self, parent, id, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.NO_BORDER | wx.TAB_TRAVERSAL):
        
        wx.Panel.__init__(self, parent, id, pos, size, style)

        self.CreateControls()
        self.GetSizer().Fit(self)
        self.GetSizer().SetSizeHints(self)
        self.Centre()
        self.GetSizer().Layout()

        self.Bind(EVT_CAPTIONBAR, self.OnPressCaption)


    def OnPressCaption(self, event):
        event.Skip()

    def CreateControls(self):

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        
        subpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.NO_BORDER | wx.TAB_TRAVERSAL)
        sizer.Add(subpanel, 1, wx.GROW | wx.ADJUST_MINSIZE, 5)

        subsizer = wx.BoxSizer(wx.VERTICAL)
        subpanel.SetSizer(subsizer)
        subpanel.SetAutoLayout(True)
        itemstrings = ["One", "Two", "Three"]

        item5 = wx.Choice(subpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                          itemstrings, 0)
        
        subsizer.Add(item5, 0, wx.GROW | wx.ALL, 5)
        
        item6 = wx.TextCtrl(subpanel, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize,
                            wx.TE_MULTILINE)
        subsizer.Add(item6, 1, wx.GROW | wx.ALL, 5)

        item7 = wx.RadioButton(subpanel, wx.ID_ANY, "I Like This", wx.DefaultPosition,
                               wx.DefaultSize, 0)
        item7.SetValue(True)
        subsizer.Add(item7, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        item8 = wx.RadioButton(subpanel, wx.ID_ANY, "I Hate It", wx.DefaultPosition,
                               wx.DefaultSize, 0)
        item8.SetValue(False)
        subsizer.Add(item8, 0, wx.ALIGN_LEFT | wx.ALL, 5)


# ----------------------------------------------------------------------------
# Collapsed Implementation
# ----------------------------------------------------------------------------

class Collapsed(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(400,300), style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.SetIcon(GetMondrianIcon())
        self.SetMenuBar(self.CreateMenuBar())

        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-4, -3])
        self.statusbar.SetStatusText("Andrea Gavana @ 23 Mar 2005", 0)
        self.statusbar.SetStatusText("Welcome to wxPython!", 1)

        self.CreateFoldBar()
        

    def CreateFoldBar(self, vertical=True):
        
        if vertical:
            self.SetSize((500,600))
        else:
            self.SetSize((700,300))

        newstyle = (vertical and [FPB_VERTICAL] or [FPB_HORIZONTAL])[0]

        bar = FoldPanelBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                           FPB_DEFAULT_STYLE | newstyle, FPB_COLLAPSE_TO_BOTTOM)

        item = bar.AddFoldPanel("Test me", collapsed=False)
        button1 = wx.Button(item, wx.ID_ANY, "Collapse Me")
        button1.Bind(wx.EVT_BUTTON, self.OnCollapseMe)
        
        bar.AddFoldPanelWindow(item, button1, FPB_ALIGN_LEFT)

        item = bar.AddFoldPanel("Test me too!", collapsed=True)

        button2 = wx.Button(item, wx.ID_ANY, "Expand First One")
        button2.Bind(wx.EVT_BUTTON, self.OnExpandMe)
        
        bar.AddFoldPanelWindow(item, button2)
        bar.AddFoldPanelSeparator(item)

        newfoldpanel = FoldTestPanel(item, wx.ID_ANY)
        bar.AddFoldPanelWindow(item, newfoldpanel)

        bar.AddFoldPanelSeparator(item)

        bar.AddFoldPanelWindow(item, wx.TextCtrl(item, wx.ID_ANY, "Comment"),
                               FPB_ALIGN_LEFT, FPB_DEFAULT_SPACING, 20)

        item = bar.AddFoldPanel("Some Opinions ...", collapsed=False)
        bar.AddFoldPanelWindow(item, wx.CheckBox(item, wx.ID_ANY, "I Like This"))

        if vertical:
            # do not add this for horizontal for better presentation
            bar.AddFoldPanelWindow(item, wx.CheckBox(item, wx.ID_ANY, "And also this"))
            bar.AddFoldPanelWindow(item, wx.CheckBox(item, wx.ID_ANY, "And gimme this too"))

        bar.AddFoldPanelSeparator(item)

        bar.AddFoldPanelWindow(item, wx.CheckBox(item, wx.ID_ANY, "Check this too if you like"))

        if vertical:
            # do not add this for horizontal for better presentation
            bar.AddFoldPanelWindow(item, wx.CheckBox(item, wx.ID_ANY, "What about this"))

        item = bar.AddFoldPanel("Choose one ...", collapsed=False)
        bar.AddFoldPanelWindow(item, wx.StaticText(item, wx.ID_ANY, "Enter your comment"))
        bar.AddFoldPanelWindow(item, wx.TextCtrl(item, wx.ID_ANY, "Comment"),
                               FPB_ALIGN_WIDTH, FPB_DEFAULT_SPACING, 20)

        if hasattr(self, "pnl"):
            self.pnl.Destroy()

        self.pnl = bar

        size = self.GetClientSize()
        self.pnl.SetDimensions(0, 0, size.GetWidth(), size.GetHeight())


    def CreateMenuBar(self):

        FoldPanelBarTest_Quit = wx.NewId()
        FoldPanelBarTest_About = wx.NewId()
        FoldPanelBarTest_Horizontal = wx.NewId()
        FoldPanelBarTest_Vertical = wx.NewId()
        
        menuFile = wx.Menu()
        menuFile.Append(FoldPanelBarTest_Horizontal, "&Horizontal\tAlt-H")
        menuFile.Append(FoldPanelBarTest_Vertical, "&Vertical\tAlt-V")
        menuFile.AppendSeparator()
        menuFile.Append(FoldPanelBarTest_Quit, "E&xit\tAlt-X", "Quit This Program")

        helpMenu = wx.Menu()
        helpMenu.Append(FoldPanelBarTest_About, "&About...\tF1", "Show About Dialog")

        self.FoldPanelBarTest_Vertical = FoldPanelBarTest_Vertical
        self.FoldPanelBarTest_Horizontal = FoldPanelBarTest_Horizontal

        self.Bind(wx.EVT_MENU, self.OnQuit, id=FoldPanelBarTest_Quit)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=FoldPanelBarTest_About)
        self.Bind(wx.EVT_MENU, self.OnOrientation, id=FoldPanelBarTest_Horizontal)
        self.Bind(wx.EVT_MENU, self.OnOrientation, id=FoldPanelBarTest_Vertical)

        value = wx.MenuBar()
        value.Append(menuFile, "&File")
        value.Append(helpMenu, "&Help")

        return value


    def OnOrientation(self, event):

        self.CreateFoldBar(event.GetId() == self.FoldPanelBarTest_Vertical)


    def OnQuit(self, event):

        # True is to force the frame to close
        self.Close(True)


    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The FoldPanelBarTest Application.\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"
        dlg = wx.MessageDialog(self, msg, "About FoldPanelBarTest",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


    def OnCollapseMe(self, event):

        item = self.pnl.GetFoldPanel(0)
        self.pnl.Collapse(item)

    def OnExpandMe(self, event):

        self.pnl.Expand(self.pnl.GetFoldPanel(0))
        self.pnl.Collapse(self.pnl.GetFoldPanel(1))


def main():

    MyApp = wx.PySimpleApp()
    wx.InitAllImageHandlers()

    Frame = Collapsed(None, -1, title="FoldPanelBar wxPython Test Application",
                      pos=wx.Point(50, 50), size=wx.Size(500, 600))

    Frame.CenterOnScreen()    
    MyApp.SetTopWindow(Frame)

    Frame.Show()
    MyApp.MainLoop()


if __name__ == "__main__":
    
    main()
