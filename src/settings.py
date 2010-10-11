#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, sys


PATH_BIN = os.path.join( os.getcwd(), "bin" ) #path where fortran executables are

work_in_memory = False       #if temporary files are written to memory. 
  

PATH_TEMP = os.path.join( os.getcwd(), "tmp" )   

PATH_ICONS = os.path.join( os.getcwd(), "icons" )

MODELS_OPTIONS = {'Soave-Redlich-Kwong':1, 
                  'Peng-Robinson':2,
                  'RK-PR':3, 
                  'PC-SAFT':4, 
                  'SPHCT':6}            #TODO; should it be inverted?

MODELS_OPTIONS_I = {1: 'SRK', 
                  2:'Peng-Robinson',
                  3:'RK-PR', 
                  4:'PC-SAFT', 
                  5:'SPHCT'} 


VC_RATIO_DEFAULT = 1.168    #relation MODEL/EXPERIMENTAL for critical volumen
TIMEOUT = 10 #seconds to timeout the calculation 

IPYTHON_CONSOLE = False

WEIGHT_POWER = 14 # weight = (Tc ^ WEIGHT_POWER) / Pc

BIN_AVAILABLE = {'2PhPxy': {'in':['twophin.DAT2'], 'out': ['PXYOUT.DAT']} , 
                 '2PhTxy': {'in':['twophin.DAT2'], 'out': ['TXYOUT.DAT']} , 
                 'FUGi': {'in': ['GPECIN.DAT', 'FUGIN.DAT'], 'out': ['FUGOUT.DAT']}, 
                 'GPEC': {'in': ['GPECIN.DAT'], 'out': ['GPECOUT.DAT'] },
                 'IsoplethGPEC': {'in':['GPECIN.DAT', 'GPECOUT.DAT', 'ZforIsop.dat'], 
                                  'out':['ISOPOUT.DAT'] },
                 'IsoXT': {'in': ['GPECIN.DAT', 'IsoXTin.DAT'], 
                           'out': ['IsoXTout.DAT'] },
                 'Models': {'in':[], 'out':[] }, 
                 'ModelsParam': {'in':['CONPARIN.DAT'], 'out':['CONPAROUT.DAT'] }, 
                 'PCSAFT': {'in':['CONPARIN.DAT'], 'out':['CONPAROUT.DAT'] }, 
                 'PxyGPEC': {'in':['GPECIN.DAT', 'GPECOUT.DAT', 'TFORPXY.dat'], 
                            'out':['PXYOUT.DAT'] }, 
                 'TxyGPEC': {'in':['GPECIN.DAT', 'GPECOUT.DAT', 'PFORTXY.dat'], 
                            'out':['TXYOUT.DAT'] } 
                }


COMBINING_RULES = {0: 'van Der Waals', 1:'Lorentz-Berthelot'}

PLOT_SUITES = {'globalsuite': ['PT', 'Tx', 'Px', 'Trho', 'Prho'], 
               'isop': ['IsoPT', 'IsoTx', 'IsoPx', 'IsoTrho', 'IsoPrho'], 
               'pxy': ['Pxy', 'PxyPrho'], 
               'txy': ['Txy', 'TxyTrho']
               }

PLOT_IN_3D = True  #just to disallow 3d for speedup on testing purpose






