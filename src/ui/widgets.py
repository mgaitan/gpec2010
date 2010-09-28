#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import  wx.lib.mixins.listctrl  as  listmix

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


    def TransferToWindow(self):
     return True

    def TransferFromWindow(self):
     return True




class FloatCtrl(wx.TextCtrl):
    def __init__(self, parent, id, value=0.0, ):
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

#class AListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    #def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 #size=wx.DefaultSize, style=0):
        #wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        #listmix.ListCtrlAutoWidthMixin.__init__(self)


class GridBagSizerEnh(wx.GridBagSizer):
    """a grid Bag sizer enhaced. Adds a method to remove/hide windows giving its 
     coordinates instead the window instance"""

    def __init__(self, *arg, **kwarg):
        wx.GridBagSizer.__init__(self, *arg, **kwarg)

    def remove_gbcontitem(self, row, col):
        '''Removes a panel item as from the class gridbagsizer position (row, col)
        as well as destroying its children.'''

        item = gbs.FindItemAtPosition((row, col))
        if (item != None) and (item.IsWindow()):
            item.GetWindow().DestroyChildren()  # destroy panel components
            self.Remove(item.GetWindow()) # Remove Panel from Sizer

    def remove_gbitem(self, row, col):
        '''Removes a control item as from the class gridbagsizer
        position (row, col) and makes it invisible.'''

        item = self.FindItemAtPosition((row, col))
        if (item != None) and (item.IsWindow()):
            self.Remove(item.GetWindow()) # Remove Panel from Sizer
            item.Show(0)                        # make old control invisible

