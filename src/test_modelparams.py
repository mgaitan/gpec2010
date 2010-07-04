import wx
import wx.lib.sized_controls as sc

class GridFrame(sc.SizedFrame):
    def __init__(self, parent, id):
        sc.SizedFrame.__init__(self, parent, id, "Grid Layout Demo Frame")
        
        pane = self.GetContentsPane()
        pane.SetSizerType("grid", {"cols":8}) # 3-column grid layout
        
        # row 1
        wx.StaticText(pane, -1, u'Tc')
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.StaticText(pane, -1, u'Pc')
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.StaticText(pane, -1, u'Vc')
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.StaticText(pane, -1, u'OM')
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        
        # row 2
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="left")

        # row 3

        #wx.TextCtrl(pane, -1).SetSizerProps(halign="left")
        wx.Panel(pane, -1).SetSizerProps(halign="left")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="center")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="right")
        wx.TextCtrl(pane, -1).SetSizerProps(halign="right")
        
        self.CreateStatusBar() # should always do this when there's a resize border
        
        self.Fit()
        self.SetMinSize(self.GetSize())


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = GridFrame(None, -1)
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
