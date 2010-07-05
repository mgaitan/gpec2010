#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import widgets
import os


import apimanager
from settings import PATH_ICONS

class VarsAndParamPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style = wx.TAB_TRAVERSAL
                     | wx.CLIP_CHILDREN
                     | wx.FULL_REPAINT_ON_RESIZE
                     )

        gbs = self.gbs = wx.GridBagSizer(6, 5)
    

        self.model_choices =  {'Soave-Redlich-Kwong':1, 'Peng-Robinson':2,
                            'RK-PR':3, 'PC-SAFT':4, 'SPHCT':6}
        self.ch = wx.Choice(self, -1, choices = self.model_choices.keys())
        

        gbs.Add( self.ch, (0,3), (1,2), flag=wx.ALIGN_RIGHT )

 
        vars_label = (('Tc [K]', 'Critical temperature'), 
                ('Pc [bar]', 'Critical Pressure'), 
                ('Vol [l/mol]', 'Critical Volume'), 
                (u'\u03c9', 'Acentric Factor') )

        #add first col
        self.vars = []
        for row, var in enumerate(vars_label):
            gbs.Add( wx.StaticText(self, -1, var[0]), (row+2, 0), flag=wx.ALIGN_RIGHT)
            self.vars.append(widgets.FloatCtrl(self, -1))
            gbs.Add ( self.vars[-1], (row+2, 1))

        self.param = []
        self.direction = 0
        self.model_id = 1
        

        #add radio buttons
        self.radio1 = wx.RadioButton( self, -1, "", style = wx.RB_GROUP)
        self.radio2 = wx.RadioButton( self, -1, "")
        self.gbs.Add(self.radio1, (1,1))
        self.gbs.Add(self.radio2, (1,4))


        self.params_labels = {1: ((u'ac [bar·m⁶Kmol²]', u'descrip ac'), 
                             ('b [l/mol]', 'descrip b'), (u'm', u'descrip m')  ),
                         2: ((u'ac [bar·m⁶Kmol²]', u'descrip ac'), 
                             (u'b [l/mol]', u'descrip b'), (u'm', u'descrip m')  ),
                         3: ((u'ac [bar·m⁶Kmol²]', u'descrip ac'), 
                             (u'b [l/mol]', u'descrip b'), (u'ω', 'descrip '),
                              ('k', 'descrip k') ),
                         4: ((u'ε/k', u'descript ε/k'), (u'ρ', u'descript ρ'),
                             (u'm', u'descript u') ),
                         6: ((u'T* [k]', u'descript T*'), (u'V* [l/mol]', 'descript V*'),
                             (u'c', u'descript c'))
                        }


        #add button in the center
        self.arrow = (wx.Bitmap(os.path.join(PATH_ICONS,"go-next.png")), 
                        wx.Bitmap(os.path.join(PATH_ICONS,"go-previous.png")))
        self.button = wx.BitmapButton(self, -1, self.arrow[0], style = wx.CENTRE)
        #self.button2left = wx.BitmapButton(self, -1, wx.Bitmap("/home/tin/facu/pi/src/images/go-previous.png", wx.BITMAP_TYPE_ANY))
        gbs.Add(self.button, (3,2), flag=wx.FIXED_MINSIZE | wx.ALIGN_CENTER)


   
        

        # Add a spacer at the end to ensure some extra space at the bottom
        #gbs.Add((10,10), (14,7))
    
        self.box = wx.BoxSizer()
        self.box.Add(gbs, 0, wx.ALL, 10)

        #set default on form
        self.SetParamsForm(self.model_id)
        self.SetDirectionOnForm()
        self.SetVarsValues(('190.56', '45.99', '0.1152', '0.0115'))
        

        #binding
        self.Bind(wx.EVT_CHOICE, self.OnSetModel, self.ch)
        self.Bind(wx.EVT_BUTTON, self.OnButton,  self.button)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDirectionSelect, self.radio1 )
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDirectionSelect, self.radio2 )


    def SetVarsValues(self, data):
        if len(data) == len(self.vars):
            for box, data in zip(self.vars, data):
                box.SetValue(data)
        else:
            wx.Bell()
            print "not enough data or boxes for EOS vars"

    def SetParamsValues(self, data):
        if len(data) == len(self.param):
            for box, data in zip(self.param, data):
                box.SetValue(data)
        else:
            wx.Bell()
            print "not enough data or boxes for EOS vars"
                


    
    def OnDirectionSelect(self, event):
        radio_selected = event.GetEventObject()
        if radio_selected == self.radio1:
            self.direction = 0
        else:
            self.direction = 1
        self.SetDirectionOnForm()

    def SetDirectionOnForm(self):
        """Update the form. Direction and enable of"""

        if self.direction == 0:
            for box in self.vars:
                box.Enable(True)
            for box in self.param:
                box.Enable(False)
            
            self.button.SetBitmapLabel(self.arrow[0])

        else:
            for box in self.vars:
                box.Enable(False)
            for box in self.param:
                box.Enable(True)
            self.button.SetBitmapLabel(self.arrow[1])



    def remove_gbcontitem(self, row, col):
        '''Removes a panel item as from the class gridbagsizer position (row, col)
        as well as destroying its children.'''

        item = self.gbs.FindItemAtPosition((row, col))
        if (item != None) and (item.IsWindow()):
            item.GetWindow().DestroyChildren()  # destroy panel components
            self.gbs.Remove(item.GetWindow()) # Remove Panel from Sizer

    def remove_gbitem(self, row, col):
        '''Removes a control item as from the class gridbagsizer
        position (row, col) and makes it invisible.'''

        item = self.gbs.FindItemAtPosition((row, col))
        if (item != None) and (item.IsWindow()):
            self.gbs.Remove(item.GetWindow()) # Remove Panel from Sizer
            item.Show(0)                        # make old control invisible

     

    def OnSetModel(self, event):
        self.model_id = self.model_choices[event.GetString()]
        self.SetParamsForm(self.model_id)

    def OnButton(self, event):
    
        if self.direction == 0:
            data = [box.GetValue() for box in self.vars]
        else:
            data = [box.GetValue() for box in self.param]

        apimanager.write_conparin(self.direction, self.model_id, data)

        data = apimanager.read_conparout()
        
        if data is not None:
            if self.direction == 0:
                self.SetParamsValues(data[1])
            else: 
                self.SetVarsValues(data[0])
        else:
            wx.Bell()
            print "error handling ModelsParam output"
            



    def SetParamsForm(self, model_id):
        """set a column of widgets for params depending on selected model"""
        
        #clean up
        for row in range(len(self.param)):
            self.remove_gbitem(row + 2, 3)
            self.remove_gbitem(row + 2, 4)

 
        self.param = []

        for row, var in enumerate(self.params_labels[model_id]):
            #add row an box to the form and the list
            self.gbs.Add(wx.StaticText(self, -1, var[0]), (row+2, 3), flag=wx.ALIGN_RIGHT)
            self.param.append(widgets.FloatCtrl(self, -1))
            self.gbs.Add ( self.param[-1], (row+2, 4))
    
        if self.direction == 0:
            self.SetDirectionOnForm()

        #FIT all
        self.gbs.Layout()
        
    
        self.SetSizerAndFit(self.box)
        self.SetClientSize(self.GetSize())



    



class TestFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Model Params")
        pane = self.pane = wx.Panel(self, -1, style = wx.TAB_TRAVERSAL
                     | wx.CLIP_CHILDREN
                     | wx.FULL_REPAINT_ON_RESIZE
                     )
        
        self.box = wx.BoxSizer(wx.VERTICAL)

        self.box.Add(VarsAndParamPanel(self,-1), 1, wx.ALL, 10)
        self.box.Add(VarsAndParamPanel(self,-1), 1, wx.ALL, 10)

        self.SetSizerAndFit(self.box)
        self.SetClientSize(self.GetSize())

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = TestFrame(None, -1)
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
