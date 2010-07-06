import wx
import wx.lib.buttons as buttons
import cStringIO

import PyCollapsiblePane as PCP

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
def GetSmilesData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x02\x89IDAT8\x8dm\x93\xddK\x93a\x18\xc6\x7f\xef\xc7\xb3\xa6\xc3 aV\xcc\
\xad\x99\x8d\\\x08\x11AAd\x91\x95\x85F\'\x9dD\x8d\xa8\xe9\xb6X\x87\xe1\x7f\
\xd0A\xe2y\'\xe6I\x7f@\'!T\x96\'A\x10A\xf4!\xcc\xd1\xb7&DP \xba\xe5\xde\xd7\
\xed\xea\xc0\xcdF\xf9\xc0u\xf2<\xcf\xc5}\xdf\xd7u\xddX\xb6\xc3\xbfH\xa5.)\
\x1e\xdf)\xd7\xb5d\x8c\xadD"\xaa\\.\xa3\xcd\xfe\xda4\x9dl&\xad\xceHP\xbd\xbd\
\x9fx\xf0\xe0\x08\xe5\xf2eJ\xa5\x8b\xdc\xbf\xbf\x9f\xae\xaeGtFj\xcaf\xae\xa9\
\x99cY\xb6\x03\xc0\xe9S\xc7\x14\x8b\xfd\xe4\xce\x9d\xf3\x18\xe3\x01%`\x05\
\xa8\x02\x15\xe0#\xbe_ \x9f\xf7\x98\x9f?\xc2\xf4\x93\xe7\x16\xb0\xdeA6\x93V,\
\x06\x13\x13\xb71&\t\x84\xea\xc4F\xb1U\xa0\x8c1\x16\x13\x13[\x88\xc5\x9e\x91\
\xcd\\]\x7f\xb4l\x87h\xb4]\x9eW\x90\xf4E\xd2c\x8d\x8e\x8e\n\x90\x94\x92\x94\
\x12\xa0p8,\xa9UR\x8b<\x0fE;\x91e;\xb8\xd9LZ]]k\x18\xd3\x028@\x8d\xf1\xf1\
\xf1\xa6)\x97\xe8\xe9\xe9ann\x0eh\x05\xd50\x04\xb9q\xbd\xca\xe7\xf9\x94\xec\
\x99\x99\x87\x0c\rE\x80E\xe0#\xf0\xba\x89\\\x01\x16YXXh\xba\xabA\xa5\x95\xa1\
\x93m\xcc\xccLa\x19c\xabT\xba\x891m\xc0*\xc3\xc3\xdf\x99\x9c\xf46\x84\x83\
\x85\xba\xa0ur\xb5\nK\x1d\xf8\xab\x0e\xa1]\xf3\r\x1b\xbd\xba\xe2\xcbLN\xfa\
\xc0\x12\xf0\x0e(6\x91\x05Zcwg\x10\xfc\x16\xf0\x83\x00\xd8\xf1x\x84b\xf1\x1b\
\xf0\x03(\x92L\xbe\x04^\xd4+\xeb/\x19\x1f\xaa6\x9f\xbf/C\xb9\x8d\xe2\x9cE|W\
\x18\xb7\xbf\xff\x0cSS\xf7\xe8\xed\r\x00\xa2P\x80PH\x94\x1a\x85\xa9\x01kP\
\xb58\xb8\xaf\r}\x89@y+S\x8f\x7f\xd1\x7f\xfcd\xc3FK\x9e\xd7R\xb7i\xdd*\x05\
\x83\n\x04\x02r]G\xa1\xa0\xab\xfd\xdd\xed\xd2\xe2^\xa9\xd0\'\xef\xd5\tEw\x04\
\xb4\x11\xe5\xc1\xc14\xf9\xfc\xeaz\x9b\r\xfc\xf6\xa9\xf8>\xbecq8\xd9\xc1\xeb\
\xa7QX\x0e\xc3Z\x80\xfc\xad"\x83g\xce\xb1\x11$\xcbv\x18\x18\xe8\xd3\xc8\x08\
\xf2<$\xd5Q\xb5\xa5\x95m\xd2\xb7\xa4\xf4\xe1\x90\xbc7G5ra\x87\x06\x8e\x1f\
\xd0\x7f\xcb4\xfd\xe4\xb9\xe58\xc3tw\xc3\xd8\x18\xcc\xce\x82_q\xf0+6\xb3\xef\
W\x18\xbb\xfb\x95\xee\xb3/p\xb6\xf61\xfd\xec\xad\xb5\x11\x8b\xcdV4\x97K+\x91\
\xd8.\xe3"\xe3\xa2\xc4\x9e\x0e\xe52W6]\xe7?\xc6#-\xf1\x056\x98<\x00\x00\x00\
\x00IEND\xaeB`\x82' 

def GetSmilesBitmap():
    return wx.BitmapFromImage(GetSmilesImage())

def GetSmilesImage():
    import cStringIO
    stream = cStringIO.StringIO(GetSmilesData())
    return wx.ImageFromStream(stream)


btnlbl1 = "call Expand(True)"
btnlbl2 = "call Expand(False)"

choices = ["wx.Button", "GenButton", "GenBitmapButton", "GenBitmapTextButton", "GTK Expander"]
gtkChoices = ["3, 6", "4, 8", "5, 10"]


class PyCollapsiblePaneDemo(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        panel = TestPanel(self)
        
        self.SetMinSize((640,480))
        self.SetIcon(GetMondrianIcon())

        self.Centre(wx.BOTH)

        statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        statusbar.SetStatusWidths([-2, -1])
        # statusbar fields
        statusbar_fields = [("PyCollapsiblePane Demo, Andrea Gavana @ 09 Aug 2007"),
                            ("Welcome To wxPython!")]

        for i in range(len(statusbar_fields)):
            statusbar.SetStatusText(statusbar_fields[i], i)
            
        self.CreateMenuBar()
        self.Show()


    def CreateMenuBar(self):

        file_menu = wx.Menu()
        
        AS_EXIT = wx.NewId()        
        file_menu.Append(AS_EXIT, "&Exit")
        self.Bind(wx.EVT_MENU, self.OnClose, id=AS_EXIT)

        help_menu = wx.Menu()

        AS_ABOUT = wx.NewId()        
        help_menu.Append(AS_ABOUT, "&About...")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=AS_ABOUT)

        menu_bar = wx.MenuBar()

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")        

        self.SetMenuBar(menu_bar)


    def OnClose(self, event):
        
        self.Destroy()


    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The PyCollapsiblePane Demo.\n\n" + \
              "Author: Andrea Gavana @ 09 Aug 2007\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n" + \
              "To Me At The Following Adresses:\n\n" + \
              "gavana@kpo.kz\n" + "andrea.gavana@gmail.com\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"
              
        dlg = wx.MessageDialog(self, msg, "PyCollapsiblePane Demo",
                               wx.OK | wx.ICON_INFORMATION)

        if wx.Platform != '__WXMAC__':
            dlg.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL, False))
            
        dlg.ShowModal()
        dlg.Destroy()

        
class TestPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent, -1)

        self.label1 = "Click here to show pane"
        self.label2 = "Click here to hide pane"

        title = wx.StaticText(self, label="PyCollapsiblePane")
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        title.SetForegroundColour("blue")

        self.cp = cp = PCP.PyCollapsiblePane(self, label=self.label1,
                                             style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, cp)
        self.MakePaneContent(cp.GetPane())

        radioBox = wx.RadioBox(self, -1, "Button Types", choices=choices, style=wx.RA_SPECIFY_ROWS)
        self.static1 = wx.StaticText(self, -1, "Collapsed Button Text:")
        self.static2 = wx.StaticText(self, -1, "Expanded Button Text:")

        self.buttonText1 = wx.TextCtrl(self, -1, self.label1)
        self.buttonText2 = wx.TextCtrl(self, -1, self.label2)
        self.updateButton = wx.Button(self, -1, "Update!")

        self.gtkText = wx.StaticText(self, -1, "Expander Size")
        self.gtkChoice = wx.ComboBox(self, -1, choices=gtkChoices)
        self.gtkChoice.SetSelection(0)
        
        self.gtkText.Enable(False)
        self.gtkChoice.Enable(False)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        radioSizer = wx.BoxSizer(wx.HORIZONTAL)
        dummySizer = wx.BoxSizer(wx.VERTICAL)

        dummySizer.Add(self.gtkText, 0, wx.EXPAND|wx.BOTTOM, 2)
        dummySizer.Add(self.gtkChoice, 0, wx.EXPAND)

        radioSizer.Add(radioBox, 0, wx.EXPAND)
        radioSizer.Add(dummySizer, 0, wx.ALIGN_BOTTOM|wx.LEFT, 10)

        self.SetSizer(sizer)
        sizer.Add((0, 10))
        sizer.Add(title, 0, wx.LEFT|wx.RIGHT, 25)
        sizer.Add((0, 10))
        sizer.Add(radioSizer, 0, wx.LEFT, 25)

        sizer.Add((0, 10))
        subSizer = wx.FlexGridSizer(2, 3, 5, 5)
        subSizer.Add(self.static1, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        subSizer.Add(self.buttonText1, 0, wx.EXPAND)
        subSizer.Add((0, 0))
        subSizer.Add(self.static2, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        subSizer.Add(self.buttonText2, 0, wx.EXPAND)
        subSizer.Add(self.updateButton, 0, wx.LEFT|wx.RIGHT, 10)
        
        subSizer.AddGrowableCol(1)
        
        sizer.Add(subSizer, 0, wx.EXPAND|wx.LEFT, 20)
        sizer.Add((0, 15))
        sizer.Add(cp, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 20)

        self.btn = wx.Button(self, label=btnlbl1)
        sizer.Add(self.btn, 0, wx.ALL, 25)

        self.Bind(wx.EVT_BUTTON, self.OnToggle, self.btn)
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, self.updateButton)
        self.Bind(wx.EVT_RADIOBOX, self.OnButtonChoice)
        self.Bind(wx.EVT_COMBOBOX, self.OnUserChoice, self.gtkChoice)
        
        
    def OnToggle(self, event):
        
        self.cp.Collapse(self.cp.IsExpanded())
        self.OnPaneChanged()


    def OnUpdate(self, event):

        self.label1 = self.buttonText1.GetValue()
        self.label2 = self.buttonText2.GetValue()

        self.OnPaneChanged(None)
        

    def OnButtonChoice(self, event):

        selection = event.GetSelection()
        
        if self.cp.IsExpanded():
            label = self.label1
        else:
            label = self.label2

        style = self.cp.GetWindowStyleFlag()
        if selection < 4:
            style &= ~PCP.CP_GTK_EXPANDER
        else:
            style |= PCP.CP_GTK_EXPANDER
            
        self.gtkText.Enable(selection == 4)
        self.gtkChoice.Enable(selection == 4)
        
        self.Freeze()
        cp = PCP.PyCollapsiblePane(self, label=self.label1, style=style)
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, cp)
        self.MakePaneContent(cp.GetPane())
        self.GetSizer().Replace(self.cp, cp)
        
        self.cp.Destroy()
        self.cp = cp
        self.Thaw()
        
        if selection == 0:     # standard wx.Button
            btn = wx.Button(self.cp, -1, label)
        elif selection == 1:   # buttons.GenButton
            btn = buttons.GenButton(self.cp, -1, label)
        elif selection == 2:   # buttons.GenBitmapButton
            bmp = GetSmilesBitmap()
            btn = buttons.GenBitmapButton(self.cp, -1, bmp)
        elif selection == 3:   # buttons.GenBitmapTextButton
            bmp = GetMondrianBitmap()
            btn = buttons.GenBitmapTextButton(self.cp, -1, bmp, label)

        if selection < 4:
            self.cp.SetButton(btn)
            btn.Bind(wx.EVT_BUTTON, self.OnToggle)
        else:
            self.cp.SetExpanderDimensions(*self.GetUserSize())

        self.OnPaneChanged(None)
        self.Layout()
        

    def OnPaneChanged(self, event=None):

        if event:
            print 'wx.EVT_COLLAPSIBLEPANE_CHANGED: %s' % event.Collapsed

        # redo the layout
        self.Layout()
        
        # and also change the labels
        if self.cp.IsExpanded():
            self.cp.SetLabel(self.label2)
            self.btn.SetLabel(btnlbl2)
        else:
            self.cp.SetLabel(self.label1)
            self.btn.SetLabel(btnlbl1)
            
        self.btn.SetInitialSize()


    def OnUserChoice(self, event):

        self.cp.SetExpanderDimensions(*self.GetUserSize(event.GetSelection()))


    def GetUserSize(self, selection=None):

        if selection is None:
            selection = self.gtkChoice.GetSelection()

        choice = gtkChoices[selection]
        width, height = choice.split(",")

        return int(width), int(height)
            

    def MakePaneContent(self, pane):

        '''Just make a few controls to put on the collapsible pane'''

        nameLbl = wx.StaticText(pane, -1, "Name:")
        name = wx.TextCtrl(pane, -1, "");

        addrLbl = wx.StaticText(pane, -1, "Address:")
        addr1 = wx.TextCtrl(pane, -1, "");
        addr2 = wx.TextCtrl(pane, -1, "");

        cstLbl = wx.StaticText(pane, -1, "City, State, Zip:")
        city  = wx.TextCtrl(pane, -1, "", size=(150,-1));
        state = wx.TextCtrl(pane, -1, "", size=(50,-1));
        zip   = wx.TextCtrl(pane, -1, "", size=(70,-1));
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl, 0, 
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)
        addrSizer.Add((5,5)) 
        addrSizer.Add(addr2, 0, wx.EXPAND)

        addrSizer.Add(cstLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 1)
        cstSizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        border = wx.BoxSizer()
        border.Add(addrSizer, 1, wx.EXPAND|wx.ALL, 5)
        pane.SetSizer(border)


app = wx.PySimpleApp()
frame = PyCollapsiblePaneDemo(None, -1, "PyCollapsiblePane wxPython Demo :-D",
                              size=(600, 550))
app.MainLoop()

