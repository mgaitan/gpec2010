# --------------------------------------------------------------------------- #
# License: wxWidgets license
#
# Python Code By:
#
# Prashant Saxena, @ Mon July 10 10:12:52 2008
# Latest Revision: Mon Aug 18 00:44:57 2008
#
# For All Kind Of Problems, Requests Of Enhancements And Bug Reports, Please
# Write To Me At:
#
#digital@pantheon-studios.in
# animator333@yahoo.com
#
# Or, Obviously, To The wxPython Mailing List!!!
#
#
# End Of Comments
# --------------------------------------------------------------------------- #

import wx

class PanelLayout(wx.Panel):
    
    """
    A new approach to create a collapsable Panel.
    """
    
    masterSizer = wx.BoxSizer(wx.VERTICAL)
    
    def __init__(self, parent, title='Frame Layout', expand=0):
        wx.Panel.__init__(self, parent, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        
        self.expand = expand #expand status
        self.parent = parent #parent of this panel
        self.title = title
        
        #this will be the main sizer for this panel
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        #this sizer contains expand button and title of frame
        self.hbox = wx.BoxSizer(wx.VERTICAL)
        
        self.btn = wx.Button(self, id=-1, label=title, size=(-1,18),  style=wx.BU_LEFT|wx.STATIC_BORDER, name='cpbtn')
        font1 = wx.Font(8, wx.NORMAL, wx.NORMAL, wx.BOLD)
        self.btn.SetFont(font1)
        self.btn.Bind(wx.EVT_BUTTON, self.OnExpand)
        
        self.lbl = wx.StaticText(self, -1, size=(-1,5), name='cplbl')
        
        self.hbox.Add(self.btn, 1, wx.EXPAND)
        self.hbox.Add(self.lbl, 0)
        
        #add to main sizer(vbox)
        self.vbox.Add(self.hbox, 0, wx.EXPAND)
               

    def OnExpand(self, event=None):

        #either hide or show the children
        for child in self.GetChildren():
            #ignore button and label here
            if child.GetName() == 'cpbtn' or child.GetName() == 'cplbl':  continue
            child.Show(self.expand)
        
        #toggle the status of 'expand'
        self.expand = not self.expand  
        
        #It's a hack to show a margin of 5 unit between button and first child of this panel.
        #When panel is collapsed, hide the label and when panel is visible show it.
        #
        if not self.expand:
            self.lbl.Show(1)
        else:
             self.lbl.Show(0)
                    
        #This will rearrange everythig again.
        self.parent.SetSizer(self.__class__.masterSizer)
        
        self.parent.Layout()
        self.parent.SendSizeEvent() #make scrollbars visible if parent is scrolledWindow and if they are required automatically
        self.lbl.SetFocus() #Remove focus from button when pressed
        self.parent.Refresh()
       
        if event: event.Skip()
            
    def FinishLayout(self):
        
        allSizers = []
        childSizer = None
        #Get all the sizers containing all the children of this panel
        for child in self.GetChildren():
            if child.GetName() == 'cpbtn' or child.GetName() == 'cplbl':  continue
            
            childSizer = child.GetContainingSizer()
            if childSizer != None:
                #add the sizer in the list if it's no there.
                #can't use set as it changes the order of elements
                #this way we can have unique sizer or not repeating ones
                if not childSizer in allSizers:
                    allSizers.append(childSizer)
            
        #Get root level sizers and add to main sizer name 'vbox'
        if len(allSizers):
            for sizer in self.getRootSizers(allSizers):        
                self.vbox.Add(sizer, 0, wx.EXPAND)
        else:
            print 'children of this panel are not in any sizers. They should be in a sizer/s'                
                
        #When deleting this panel in any case, masterSizer is also getting deleted. we have to create it again
        if not isinstance(self.__class__.masterSizer, wx._core.BoxSizer):
            self.__class__.masterSizer = wx.BoxSizer(wx.VERTICAL)
                
        self.__class__.masterSizer.Add(self, 0, wx.EXPAND)    
        
        #Rearrange everything
        self.SetSizer(self.vbox)
        self.Fit()
        self.OnExpand()
        
    
    def getRootSizers(self, sizerList):
        '''
        'sizerList' contains many sizers and may possible nested sizers or sizers added inside another sizers.
        This function process the list and returns only root level sizers.
        We'll add only root level sizers to main sizer of this class name 'vbox'.
        '''
        finalList = sizerList[:]
        copyList = sizerList[:]
                
        for sizer in copyList:
            if len(sizer.GetChildren()):
                for child in sizer.GetChildren():
                    if child.GetClassName() == 'wxSizerItem':
                        try:
                            finalList.remove(child.GetSizer())
                        except:
                            pass
        return finalList 
                