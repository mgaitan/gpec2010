import wx

class FloatValidator( wx.PyValidator):
    def __init__(self, pyVar = None):
        wx.PyValidator.__init__(self)
        self.charlist = [ str(n) for n in range(0, 10) ]
        self.charlist.append('.')
        self.charlist.append('-')
        self.codelist = [ wx.WXK_SPACE, wx.WXK_DELETE, \
        wx.WXK_BACK, wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_TAB]

        self.Bind(wx.EVT_CHAR, self.ProcessKey)
        
    def Clone (self):
        return FloatValidator()

    def ProcessKey(self, event):
        key = event.GetKeyCode()
        
        if key in self.codelist or chr(key) in self.charlist:
            event.Skip()
            return
        
        if not wx.Validator_IsSilent():
            wx.Bell()

class FloatCtrl(wx.TextCtrl):
    def __init__(self, parent, id, value=0.0):
        wx.TextCtrl.__init__(self, parent, id, str(value), \
        validator = FloatValidator())
        self.SetMinSize((50,-1))
        self.SetMaxSize((100,-1))
        #self.SetFont(PlainFont(12))

class FloatControlUnit(wx.Panel):
    
     def __init__(self, parent, value=0.0, unit=""):
        wx.Panel.__init__(self, parent, -1)
        fgs = wx.FlexGridSizer(cols=2, hgap=4)
        fgs.Add(FloatControl(self, value))
        #fgs.Add((10,10))
        fgs.Add(wx.StaticText(self, -1, unit))
        box = wx.BoxSizer()
        box.Add(fgs, 1, wx.EXPAND|wx.LEFT|wx.ALL)
        self.SetSizer(box)
