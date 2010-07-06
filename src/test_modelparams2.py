#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import widgets
import os

import wx.lib.buttons
import apimanager
from settings import PATH_ICONS

#list-add

class VarsAndParamPanel(wx.Panel):
    """a panel with 2 columns of inputs. First colums input EOS variables. 
        The second one are the inputs to model parameters (change depending
        the model selected). 
        This parameter are related and is possible to calcule a group of values
        defining the other one. 
        """

    def __init__(self, parent, id, model_id=1, setup_data=None):
        

        wx.Panel.__init__(self, parent, id, style = wx.TAB_TRAVERSAL
                     | wx.CLIP_CHILDREN
                     | wx.FULL_REPAINT_ON_RESIZE
                     )

        gbs = self.gbs = wx.GridBagSizer(6, 5)
    

 
        vars_label = (('Tc [K]', 'Critical temperature'), 
                ('Pc [bar]', 'Critical Pressure'), 
                ('Vol [l/mol]', 'Critical Volume'), 
                (u'\u03c9', 'Acentric Factor') )

        #add title
        self.title = wx.StaticText(self, -1, '', (5, 120), style = wx.ALIGN_CENTER)
        self.title.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))
        gbs.Add(self.title, (0,0), (1,4),  flag=wx.ALIGN_CENTER)


        #add first col
        self.vars = []
        for row, var in enumerate(vars_label):
            gbs.Add( wx.StaticText(self, -1, var[0]), (row+2, 0), flag=wx.ALIGN_RIGHT)
            self.vars.append(widgets.FloatCtrl(self, -1))
            gbs.Add ( self.vars[-1], (row+2, 1))

        self.params = []


        

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
        self.button = wx.BitmapButton(self, -1, self.arrow[0], style = wx.CENTRE | wx.BU_AUTODRAW)
        #self.button2left = wx.BitmapButton(self, -1, wx.Bitmap("/home/tin/facu/pi/src/images/go-previous.png", wx.BITMAP_TYPE_ANY))
        gbs.Add(self.button, (3,2), flag=wx.FIXED_MINSIZE | wx.ALIGN_CENTER)


   
        

        # Add a spacer at the end to ensure some extra space at the bottom
        #gbs.Add((10,10), (14,7))
    
        self.box = wx.BoxSizer()
        self.box.Add(gbs, 0, wx.ALL, 10)


        #set default on form
        self.direction = 0
        self.model_id = model_id
      

        if setup_data is not None:
            self.enabled = True
            self.SetData(setup_data)
            self.SetDirectionOnForm()
        else:
            
            self.EnableAll(False)

        
        self.SetParamsForm(self.model_id)
        


        #binding
        self.Bind(wx.EVT_BUTTON, self.OnButton,  self.button)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDirectionSelect, self.radio1 )
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDirectionSelect, self.radio2 )

    def SetData(self, data):
        self.title.SetLabel(data[0])
        self.SetVarsValues(data[1:])
        self.EnableAll()
        

    def EnableAll(self, flag=True):
        self.enabled = flag
        for box in self.vars :
            box.Enable(flag)

        self.button.Enable(flag)
        self.radio1.Enable(flag)
        self.radio2.Enable(flag)
        

    def SetVarsValues(self, data):
        if len(data) == len(self.vars):
            for box, data in zip(self.vars, data):
                box.SetValue(data)
        else:
            wx.Bell()
            print "not enough data or boxes for EOS vars"

    def SetParamsValues(self, data):
        if len(data) == len(self.params):
            for box, data in zip(self.params, data):
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
            for box in self.params:
                box.Enable(False)
            
            self.button.SetBitmapLabel(self.arrow[0])
        else:
            for box in self.vars:
                box.Enable(False)
            for box in self.params:
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

     



    def OnButton(self, event):
    
        if self.direction == 0:
            data = [box.GetValue() for box in self.vars]
        else:
            data = [box.GetValue() for box in self.params]

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
        self.model_id = model_id
        for row in range(len(self.params)):
            self.remove_gbitem(row + 2, 3)
            self.remove_gbitem(row + 2, 4)

 
        self.params = []

        for row, var in enumerate(self.params_labels[model_id]):
            #add row an box to the form and the list
            self.gbs.Add(wx.StaticText(self, -1, var[0]), (row+2, 3), flag=wx.ALIGN_RIGHT)
            self.params.append(widgets.FloatCtrl(self, -1))
            self.gbs.Add ( self.params[-1], (row+2, 4))
    
        

        if self.direction == 0:
            self.SetDirectionOnForm()

        self.EnableAll(self.enabled)

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


        self.model_choices =  {'Soave-Redlich-Kwong':1, 'Peng-Robinson':2,
                            'RK-PR':3, 'PC-SAFT':4, 'SPHCT':6}
        self.ch = wx.Choice(self, -1, choices = self.model_choices.keys())
        
        #model ID by default
        self.model_id = 1
        self.ch.SetSelection(0)

        first_row_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.load_button = wx.lib.buttons.GenBitmapTextButton(self, -1, wx.Bitmap(os.path.join(PATH_ICONS,"compose.png")), "Load System")
        
        first_row_sizer.Add(self.load_button, 0, flag=wx.ALL | wx.ALIGN_LEFT | wx.EXPAND , border=5)
        first_row_sizer.Add((60, 20), 0, wx.EXPAND)

        first_row_sizer.Add(wx.StaticText(self, -1, "Model:"), 0, flag= wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, border=5)
        first_row_sizer.Add(self.ch, 0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL , border=5)
        self.box.Add( first_row_sizer, 0, flag= wx.TOP | wx.RIGHT | wx.FIXED_MINSIZE | wx.ALIGN_RIGHT, border = 5)

        
        self.panels = (VarsAndParamPanel(self,-1), VarsAndParamPanel(self,-1))

        self.box.Add(self.panels[0], 0, wx.EXPAND )
        self.box.Add(self.panels[1], 0, wx.EXPAND )


        #collapsible for extra variables

        self.cp = cp = wx.CollapsiblePane(self, label='Other case variables',
                                          style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        self.MakeCollipsable(cp.GetPane())
        self.box.Add(self.cp, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 25)



            
        self.accept_button = wx.lib.buttons.GenBitmapTextButton(self, -1, wx.Bitmap(os.path.join(PATH_ICONS,"document-save.png")), "Write GPECIN.DAT")


        but_sizer =  wx.BoxSizer(wx.HORIZONTAL)
        
        but_sizer.Add(self.accept_button, 0, flag=wx.ALL , border=5)

        self.box.Add(but_sizer, 0, flag= wx.ALL | wx.FIXED_MINSIZE | wx.ALIGN_RIGHT, border = 5)

        
        #self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, cp)


        self.SetSizerAndFit(self.box)
        self.SetClientSize(self.GetSize())

        #Binding
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, cp)
        self.Bind(wx.EVT_CHOICE, self.OnSetModel, self.ch)
        self.Bind(wx.EVT_BUTTON, self.OnLoadSystem, self.load_button)
        self.Bind(wx.EVT_BUTTON, self.OnWriteGPECIN, self.accept_button)

    def MakeCollipsable(self, pane):
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
    
        self.temperature = widgets.FloatCtrl(pane, -1, "2000.0");
        temperatureLbl = wx.StaticText(pane, -1, "Temperature [k]")

        self.k12 = widgets.FloatCtrl(pane, -1);
        k12Lbl = wx.StaticText(pane, -1, "K12")

        self.l12 = widgets.FloatCtrl(pane, -1);
        l12Lbl = wx.StaticText(pane, -1, "L12")

        addrSizer.Add(temperatureLbl, 0, 
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.temperature, 0)
        addrSizer.Add(l12Lbl, 0, 
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.l12, 0)
        addrSizer.Add(k12Lbl, 0, 
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.k12, 0)

        border = wx.BoxSizer()
        border.Add(addrSizer, 1, wx.EXPAND|wx.ALL, 5)
        pane.SetSizer(border)
    
    def OnPaneChanged(self, evt=None):
        # redo the layout
        self.Layout()
        self.SetClientSize(self.GetSize())
        self.Fit()
    

    def OnLoadSystem(self, event):
        self.panels[0].SetData(('METHANE', '190.56', '45.99', '0.1152', '0.0115'))
        self.panels[1].SetData(('BUTANE', '194.56', '12.99', '1.1452', '0.0115'))

    def OnSetModel(self, event):
        for panel in self.panels:
            self.model_id = self.model_choices[event.GetString()]
            panel.SetParamsForm(self.model_id)

        self.SetSizerAndFit(self.box)
        self.SetClientSize(self.GetSize())

    def OnWriteGPECIN(self, event):
        pass

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = TestFrame(None, -1)
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
