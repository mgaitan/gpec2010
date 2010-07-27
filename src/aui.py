import wx
import wx.aui

import apimanager
from panels import SuitePlotsPanel, TabbedCases, InfoPanel
from tools.misc import curry

from wx.lib.pubsub import Publisher as pub

class MainFrame(wx.Frame):

    def __init__(self, parent, id=-1, title='GPEC',
                 pos=wx.DefaultPosition, size=(800,600),
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style=style)

        self._mgr = wx.aui.AuiManager(self)

        self.SetBackgroundColour(wx.NullColour) #hack for win32


        self.CenterOnScreen()

        self.CreateStatusBar()
        self.SetStatusText("This is the statusbar")


        menu = [
            ('&File', [
                ('&Open', self.FileOpen),
                (),
                ('&Exit', self.onCloseWindow, "Quit this program"),

            ]),
            ('&Edit', [
                ('&Copy', self.EditCopy),
                ('&Paste', self.EditPaste),
            ]),
            ('&View', [
                ('&One item', curry(self.DataBox, 1)),
                ('&Second item', curry(self.DataBox, 2)),
                ('Sub&menu', [
                    ('&Three', curry(self.DataBox, 3)),
                    ('&Four', curry(self.DataBox, 4)),
                ]),
            ]),
        ]

        self.SetMenuBar(self.BuildMenu(menu))

        # create several text controls
        self.cases_panel = TabbedCases(self, -1)
        self.plots_panel = SuitePlotsPanel(self, -1)
        self.log_panel = InfoPanel(self, -1)

        # add the panes to the manager
        self._mgr.AddPane(self.cases_panel, wx.aui.AuiPaneInfo().Name("cases").
                          Caption(u"Cases").Left().MinSize(self.cases_panel.GetSize()).
                          MaxSize(self.cases_panel.GetSize()).
                          Layer(1).Position(2).CloseButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.plots_panel, wx.aui.AuiPaneInfo().Name('plot').CenterPane())
        self._mgr.AddPane(self.log_panel, wx.aui.AuiPaneInfo().Name("log").Caption(u"Info").
                          MinSize(wx.Size(-1, 100)).
                          Bottom().Layer(0).Position(1).CloseButton(True).MaximizeButton(False))

        # tell the manager to 'commit' all the changes just made
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)


    def OnClose(self, event):
        # deinitialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()


    def onCloseWindow(self, event):
        # dialog to verify exit (including menuExit)
        dlg = wx.MessageDialog(self, "Want to exit?", "Exit", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.OnClose(event)  # frame
        dlg.Destroy()


    def FileOpen(self, event):
        self.Info(self, 'You chose File->Open')
    def EditCopy(self, event):
        self.Info(self, 'You chose Edit->Copy')
    def EditPaste(self, event):
        self.Info(self, 'You chose Edit->Paste')
    def DataBox(self, num, event):
        self.Info(self, 'You chose item %d' % (num,))
    def Info(self, parent, message, caption = 'Better Menus'):
        dlg = wx.MessageDialog(parent, message, caption, \
            wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


    def BuildMenu(self, menu):
        mainMenu = wx.MenuBar()
        for title, subMenu in menu:
            mainMenu.Append(self.BuildSubmenu(subMenu), title)
        return mainMenu

    def BuildSubmenu(self, subMenu):
        subMenuObject = wx.Menu()
        for item in subMenu:
            if not item:                #allow now to add separators
                subMenuObject.AppendSeparator()
                continue
            statustext = '';    uihandler = None
            if len(item) == 2:
                title, action = item
            elif len(item) == 3:
                if type(item[2]) is str:
                    title, action, statustext = item
                else:
                    title, action, statustext = item
            elif len(item) == 4:
                title, action, statustext, uihandler = item
            else:
                raise AssertionError, \
                    'Item %s should have either 2 to 4 parts' % (item,)
            if type(action) is list:
                _id = wx.NewId()
                subMenuObject.AppendMenu(_id, title, self.BuildSubmenu(action))
            else:
                _id = wx.NewId()
                subMenuObject.Append(_id, title, statustext)
                wx.EVT_MENU(self, _id, action)
            if uihandler:
                wx.EVT_UPDATE_UI(self, _id, uihandler)
        return subMenuObject




if __name__ == "__main__":
    apimanager.clean_tmp() #sometimes are problems with file handling between 
                           #python and GPEC at the same time. Trying a magic clean-up

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    main_frame = MainFrame(None, -1)
    app.SetTopWindow(main_frame)
    main_frame.Show()

    pub.sendMessage('log', ('ok', 'GPEC is ready. Define a system to begin') )
    app.MainLoop()
