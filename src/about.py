#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
from wx.lib.wordwrap import wordwrap


class AboutBox():
    def __init__(self, parent):
        with open(os.path.join( os.getcwd(), "LICENSE.txt" ), "r") as fh:
            license_text = fh.read()
            
        about_text = u"GPEC is a software that allows you to obtain phase diagrams and other thermodynamic plots for binary systems, as calculated with equations of state. It can be helpful for either educational, academic or development purposes. "\
                     u"It is easy to use and you do not have to provide any initial guesses or other inputs.\n\n "\
                     u"This is a rewriting from scratch version of the GPEC frontend, written in Python by Martín Gaitán as part as his "\
                     u"final degree project on Computer Enginnering at Universidad Nacional de Córdoba"

        info = wx.AboutDialogInfo()
        info.Name = "GPEC 2010"
        info.Version = "0.1 Beta 2.1"
        info.Copyright = u"(C) 2010 Martín Cismondi & Martín Gaitán "
        info.Description = wordwrap(about_text, 350, wx.ClientDC(parent))
        info.WebSite = ("http://gpec.efn.uncor.edu", "GPEC home page")
        info.Developers = [ u"Martín Gaitán (Python frontend) ",
                            u"Martín Cismondi Duarte (Fortran backend)",]

        info.License = wordwrap(license_text, 600, wx.ClientDC(parent))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
    
if __name__ == '__main__':
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    main_frame = AboutBox(None)
    app.SetTopWindow(main_frame)
    main_frame.Show()
    app.MainLoop()
 
