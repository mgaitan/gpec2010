#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MATPLOTLIB
import matplotlib
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

import wx

class BasePlot(object):
    """a base plot class for GPEC"""

    def __init__(self, parent, arrays=None, title=None, xlabel=None, ylabel=None, system=()):

        self.title = title
        if len(system)==2:
            self.title += '-  System %s-%s' % system 

        self.system = system
        self.arrays = arrays

        
        self.fig = Figure()     #dpi=self.dpi
        self.canvas = FigCanvas(parent, -1, self.fig)
        
        self.axes = self.fig.add_subplot(111)


        self.axes.set_title(title)
        self.axes.set_ylabel(ylabel)
        self.axes.set_xlabel(xlabel)

        self.axes.set_autoscale_on(True)
                

        self.properties = {'Grid':wx.NewId(), 'Legends':wx.NewId(), 'Log X': wx.NewId(), 'Log Y': wx.NewId(), }
   

        self.curves = []    #curves to plot

        if arrays:
            self.setup_curves()

     

    def setup_curves (self):
        """each one sutype declare curves as a group of line2d

            - redefined by each sub class"""

        pass


    def plot(self):
        """plot all visible curves"""
        for curve in self.curves:
            if curve['visible']:
                curve['line2d'] = self.axes.plot(*curve['lines'], color=curve['color'], label=curve['name'])
        

        
        self.canvas.draw()


    def OnToggleCurve(self, event):
        wx_id = event.GetId()
        curve = [curve for curve in self.curves  if curve['wx_id'] == wx_id][0]     #TODO better way?        

        curve['visible'] = not curve['visible']
        for line in curve['line2d']:
            line.set_visible(curve['visible']) 

        self.canvas.draw()

    def OnToggleProperty(self, event):
        wx_id = event.GetId()
        prop = dict([[v,k] for k,v in self.properties.items()])[wx_id] #inverted dict

        if prop == 'Grid':
            self.axes.grid()

        elif prop == 'Legends':
            if self.axes.get_legend():
                self.axes.legend_ = None        #a tricky way to remove lengeds
            else:
                self.axes.legend(loc='best')  

        elif prop == 'Log X':
            if self.axes.get_xscale() == 'linear':
                self.axes.set_xscale('log')
            else:
                self.axes.set_xscale('linear')

        elif prop == 'Log Y':
            if self.axes.get_yscale() == 'linear':
                self.axes.set_yscale('log')
            else:
                self.axes.set_yscale('linear')



        self.canvas.draw()


class PT(BasePlot):
    """pressure-temperature diagram"""
    
    def __init__(self, parent, arrays=None, system=()):

        self.short_title = u"P-T"
        self.title = u'Pressure-Temperature projection of a global phase equilibrium diagram'
        self.xlabel = u'Temperature [K]'
        self.ylabel = u'Pressure [bar]'

        BasePlot.__init__(self, parent, arrays, self.title, self.xlabel, self.ylabel, system)        

    def setup_curves(self, arrays):

        if 'VAP' in arrays.keys():
            for num, vap_curve in enumerate(arrays['VAP']):
                
                counter = u'' if len(arrays['VAP']) == 1 else u' %i' % (num + 1)

                self.curves.append( {'name': u'Vapor line' + counter , 
                                     'visible':True, 
                                     'lines':( vap_curve[:,0], vap_curve[:,1]),
                                      'color' : 'green',
                                      'wx_id' : wx.NewId(),
                                      'type': 'VAP',
                                        } )             

        if 'CRI' in arrays.keys():
            for num, cri_curve in enumerate(arrays['CRI']):

                counter = u'' if len(arrays['CRI']) == 1 else u' %i' % (num + 1)
                self.curves.append( {'name': u'Critical line' + counter , 
                                     'visible':True, 
                                     'lines':(cri_curve[:,0],cri_curve[:,1]),
                                     'color' : 'black',
                                     'wx_id' : wx.NewId(),
                                     'type': 'CRI'
                                    } )


        if 'LLV' in arrays.keys():
            for num, llv_curve in enumerate(arrays['LLV']):
                self.curves.append( { 'name': 'LLV', 
                                      'visible':True,
                                      'lines': (llv_curve[:,0], llv_curve[:,1]),           #TODO
                                      'color': 'red', 
                                      'wx_id' : wx.NewId(),
                                       'type': 'LLV',
                                    } )



class Tx(BasePlot):
    """T-x plot"""
    
    def __init__(self, parent, arrays=None, system=()):
        self.short_title = u"T-x"
        self.title = u'Temperature-Composition projection of a global phase equilibrium diagram'
        self.xlabel = u'Composition'    #TODO DEFINE system inside the plot
        self.ylabel = u'Temperature [K]'

        BasePlot.__init__(self, parent, arrays, self.title, self.xlabel, self.ylabel, system)        

    def setup_curves(self, arrays):

               
        
        if 'CRI' in arrays.keys():
            for num, cri_curve in enumerate(arrays['CRI']):

                counter = u'' if len(arrays['CRI']) == 1 else u' %i' % (num + 1)

                self.curves.append( {'name': u'Critical line' + counter, 
                                     'visible':True, 
                                     'lines':(cri_curve[:,3],cri_curve[:,0]),
                                     'color' : 'black',
                                     'wx_id' : wx.NewId(),
                                     'type': 'CRI'
                                    } )


        if 'LLV' in arrays.keys():
            for num, llv_curve in enumerate(arrays['LLV']):
            
                counter = u'' if len(arrays['CRI']) == 1 else u' %i' % (num + 1)

                self.curves.append( { 'name': 'LLV' + counter, 
                                      'visible':True,
                                      'lines': (llv_curve[:,2], llv_curve[:,0]),   
                                      'color': 'red', 
                                      'wx_id' : wx.NewId(),
                                       'type': 'LLV',
                                    } )




