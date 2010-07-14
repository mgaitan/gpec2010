#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MATPLOTLIB
import matplotlib
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

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
   

        self.curves = []    #curves to plot

        if arrays:
            self.setup_curves()

    def set_arrays(self, arrays):
        self.arrays = arrays
        self.setup_curves()
     

    def setup_curves (self):
        """each one sutype declare curves as a group of line2d

            - redefined by each sub class"""

        pass


    def plot(self):
        """plot all visible curve"""
        for curve in self.curves:
            if curve['visible']:
                self.axes.plot(*curve['lines'], color=curve['color'], label=curve['name'])

        
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
                              'color' : 'g'} )

        self.curves.append( {'name': u'Critical line', 'visible':True, 
                             'lines':(self.arrays[2][:,0],self.arrays[2][:,1]),
                              'color' : 'b'} )

        #TODO add others curves AZE / LLV
        self.curves.append( {'name': 'LLV', 'visible':False,
                            'lines': (),            #TODO
                            'color': 'r'} )



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
                              'color' : 'b'} )

        self.curves.append( {'name': u'LLV lines', 
                             'visible':True, 
                             'lines':( self.arrays[0][:,0],self.arrays[0][:,1], self.arrays[1][:,0],self.arrays[1][:,1]),
                              'color' : 'b'} )
        
