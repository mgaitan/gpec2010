import wx
from PanelLayout import PanelLayout

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title)
        
        
        scrollWindow = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        scrollWindow.SetScrollbars(20,20,55,40)
        
        #BEGIN PANEL 1
        PL1 = PanelLayout(scrollWindow, title="Panel 1", expand=1) 
                
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        pnl1 = wx.Button(PL1, -1, "Button1")
        pnl2 = wx.Button(PL1, -1, "Button2")
        pnl3 = wx.Button(PL1, -1, "Button3")
        
        hbox.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(pnl3, 1, wx.EXPAND | wx.ALL, 3)
                
        #END PANEL 1
        PL1.FinishLayout()
        
        #BEGIN PANEL 2
        PL2 = PanelLayout(scrollWindow, title="Panel 2", expand=0) 
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        pnl5 = wx.Button(PL2, -1, "Button4")
        pnl6 = wx.Button(PL2, -1, "Button5")
        pnl7 = wx.Button(PL2, -1, "Button6")
        pnl8 = wx.Button(PL2, -1, "Button7")
        hbox1.Add(pnl5, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(pnl6, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(pnl7, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(pnl8, 1, wx.EXPAND | wx.ALL, 3)
        
        #END PANEL 2
        PL2.FinishLayout()
        
        self.Centre()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Panel Layout Demo')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()