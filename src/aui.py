#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.aui
import os
import sys
import cPickle as pickle

import apimanager
from panels import SuitePlotsPanel, TabbedCases, InfoPanel, PlotsTreePanel
from tools.misc import curry

from wx.lib.pubsub import Publisher as pub

class MainFrame(wx.Frame):

    def __init__(self, parent, id=-1,
                 pos=wx.DefaultPosition, title='GPEC', size=(800,600),
                 style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style=style)

        self._mgr = wx.aui.AuiManager(self)

        self.SetBackgroundColour(wx.NullColour) #hack for win32

        self.title = title

        self.CenterOnScreen()

        self.CreateStatusBar()
        self.SetStatusText("")
        pub.subscribe(self.OnSetStatusText, 'status')

        menu = [
            ('&File', [
                ('&Open', self.FileOpen),
                ('&Save As...', self.FileSaveAs),
                ('&Save', self.FileSave),
                
                (),
                ('&Exit', self.onCloseWindow, "Quit this program"),

            ]),
            ('&Edit', [
                ('&Copy', self.EditCopy),
                ('&Paste', self.EditPaste),
            ]),
            ('&View', [
                ('&Restore default view', self.SetDefaultPerspective),
                
                #('Sub&menu', [
                #    ('&Three', curry(self.DataBox, 3)),
                #    ('&Four', curry(self.DataBox, 4)),
                #]),
            ]),
        ]

        


        self.SetMenuBar(self.BuildMenu(menu))

        # create several text controls
        self.cases_panel = TabbedCases(self, -1)

        #ugly hack to fix the size of case aui panel
        if sys.platform != 'win32':
            the_size = self.cases_panel.GetSize()
        else:
            the_size = wx.Size(330, -1)


        self.cases_auipane = wx.aui.AuiPaneInfo().Name("cases").\
                          Caption(u"Cases").Left().MinSize(the_size).MaxSize(the_size).\
                          Layer(1).Position(2).CloseButton(True).MinimizeButton(True)
                          
                          #MaxSize(self.cases_panel.GetSize()).\
        self.plots_panel = SuitePlotsPanel(self, -1)
        self.log_panel = InfoPanel(self, -1)


        self.plots_tree_panel = PlotsTreePanel(self, -1)
        self.plots_tree_auipane = wx.aui.AuiPaneInfo().\
                          Name("plots_tree").Caption("Manager").\
                          Floatable(True)

        self._mgr.AddPane(self.plots_tree_panel,self.plots_tree_auipane )

        # add the panes to the manager
        self._mgr.AddPane(self.cases_panel, self.cases_auipane )

        self._mgr.AddPane(self.plots_panel, wx.aui.AuiPaneInfo().Name('plot').Center().Layer(2).Caption(u"Plots").MaximizeButton(True))
        self._mgr.AddPane(self.log_panel, wx.aui.AuiPaneInfo().Name("log").Caption(u"Info").
                          MinSize(wx.Size(-1, 100)).
                          Bottom().Layer(0).Position(1).CloseButton(True).MaximizeButton(False))


        self.perspective_default = self._mgr.SavePerspective()

        # tell the manager to 'commit' all the changes just made
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.aui.EVT_AUI_PANE_CLOSE, self.OnClosePane)

        #self.Bind(wx.aui.EVT_AUI_RENDER, self.OnDragSash)

        self.Maximize()


        self.dirname = ''
        
        self.filename = None
        self.modified = False


        #a few hackies to refresh the ugly window
        pub.subscribe(self.RefreshMe, 'add checkbox')
        pub.subscribe(self.RefreshMe, 'log')
        pub.subscribe(self.RefreshMe, 'refresh all')
            
        self.registered = {}
        pub.subscribe(self.Register, 'register')
    

    def Register(self,  message):
        self.registered[message.data[0]] = message.data[1]

    def RefreshMe(self, message):
        return self.Refresh()


    
    def OnDragSash(self, evt):
        print 'dragged', evt


    def FileSaveAs(self,event):
        """Save the project as a new file"""
        dlg = wx.FileDialog(self, "Save as", self.dirname, "", "*.gpc", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            self.FileSave(event)

        dlg.Destroy()

    def FileSave(self,event):
        """Save the project in the file defined or in a new one"""

        if self.filename is None:
            self.FileSaveAs(event)
        else:
            data = self.cases_panel.SaveCases()

            with open(os.path.join(self.dirname, self.filename),'w') as fh:
                pickle.dump(data,fh)

            self.SetTitle("%s <%s>" % (self.title, self.filename))
            self.modified = False






    def OnClosePane(self, event):
        wx.CallAfter(self.egg)




    def egg(self):
        if all([not p.IsShown() for p in self._mgr.GetAllPanes()]):
            import grgevf


    def SetDefaultPerspective(self, event=None):
        self._mgr.LoadPerspective(self.perspective_default)


    def OnSetStatusText(self, message):
        self.SetStatusText(message.data)


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
        dlg = wx.FileDialog(self, "Open Project", self.dirname, "", "*.gpc", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            with open(os.path.join(self.dirname, self.filename),'r') as fh:
                data = pickle.load(fh)
                self.cases_panel.LoadCases(data)

            # Report on name of latest file read
            self.SetTitle("%s <%s>" % (self.title, self.filename))
            
            self.modified = False

        dlg.Destroy()



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
