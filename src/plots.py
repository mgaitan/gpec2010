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

        self.properties = {'Grid':wx.NewId(), 'Legends':wx.NewId() }
   

        self.curves = []    #curves to plot

        if arrays:
            self.setup_curves()

    def set_arrays(self, arrays):
        self.arrays = arrays        #TODO it's needed to have a whole copy? 
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

        self.canvas.draw()


class PT(BasePlot):
    """pressure-temperature diagram"""
    
    def __init__(self, parent, arrays=None, system=()):

        self.short_title = u"P-T"
        self.title = u'Pressure-Temperature projection of a global phase equilibrium diagram'
        self.xlabel = u'Temperature [K]'
        self.ylabel = u'Pressure [bar]'

        BasePlot.__init__(self, parent, arrays, self.title, self.xlabel, self.ylabel, system)        

    def setup_curves(self):


        self.curves.append( {'name': u'Vapor lines', 
                             'visible':True, 
                             'lines':( self.arrays[0][:,0],self.arrays[0][:,1], self.arrays[1][:,0],self.arrays[1][:,1]),
                              'color' : 'g',
                              'wx_id' : wx.NewId()  
                                } )

        self.curves.append( {'name': u'Critical line', 'visible':True, 
                             'lines':(self.arrays[2][:,0],self.arrays[2][:,1]),
                             'color' : 'b',
                             'wx_id' : wx.NewId()
                            } )

        #TODO add others curves AZE / LLV
        self.curves.append( {'name': 'LLV', 'visible':False,
                            'lines': (),            #TODO
                            'color': 'r', 
                            'wx_id' : wx.NewId()
                            } )



class Tx(BasePlot):
    """T-x plot"""
    
    def __init__(self, parent, arrays=None, system=()):
        self.short_title = u"T-x"
        self.title = u'Temperature-Composition projection of a global phase equilibrium diagram'
        self.xlabel = u'Composition'
        self.ylabel = u'Temperature [K]'

        BasePlot.__init__(self, parent, arrays, self.title, self.xlabel, self.ylabel, system)        

    def setup_curves(self):

        self.curves.append( {'name': u'Critical lines', 
                             'visible':True, 
                             'lines':( self.arrays[0][:,0],self.arrays[0][:,1], self.arrays[1][:,0],self.arrays[1][:,1]),
                             'color' : 'b', 
                             'wx_id' : wx.NewId()
                            } )

        self.curves.append( {'name': u'LLV lines', 
                             'visible':True, 
                             'lines':( self.arrays[0][:,0],self.arrays[0][:,1], self.arrays[1][:,0],self.arrays[1][:,1]),
                             'color' : 'b', 
                             'wx_id' : wx.NewId()
                            } )
        
