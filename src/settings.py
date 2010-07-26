#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, sys


PATH_BIN = os.path.join( os.getcwd(), "bin" ) #path where fortran executables are

work_in_memory = False       #if temporary files are written to memory. 
  

PATH_TEMP = os.path.join( os.getcwd(), "tmp" )   

PATH_ICONS = os.path.join( os.getcwd(), "icons" )

_models = {'Soave-Redlich-Kwong':1, 
          'Peng-Robinson':2,
          'RK-PR':3, 
          'PC-SAFT':4, 
          'SPHCT':6}            #TODO; should it be inverted?


VC_RATIO = 1.168    #relation MODEL/EXPERIMENTAL for critical volumen
TIMEOUT = 10 #seconds to timeout the calculation 


WEIGHT_POWER = 14 # weight = (Tc ^ WEIGHT_POWER) / Pc

BIN_AVAILABLE = ['2PhPxy', '2PhTxy', 'FUGi', 'GPEC', 'IsoplethGPEC', 'IsoXT', 
                  'Models', 'ModelsParam', 'PCSAFT', 'PxyGPEC', 'TxyGPEC']

COMBINING_RULES = {0: 'van Der Waals', 1:'Lorentz-Berthelot'}
