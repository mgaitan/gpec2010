#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, sys

try: 
    import fs.memoryfs
    MFS = True      #memory FS are present
    memfs = fs.memoryfs.MemoryFS()
except ImportError:
    MFS = False
    

#path where fortran executables are
PATH_BIN = os.path.join( os.getcwd(), "bin" )


work_in_memory = True       #if temporary files are written to memory

if work_in_memory and MFS:
    _path_temp = memfs.makedir('tmp')
else:
    _path_temp = os.path.join( os.getcwd(), "tmp" )   


PATH_ICONS = os.path.join( os.getcwd(), "icons" )

_models = {'Soave-Redlich-Kwong':1, 
          'Peng-Robinson':2,
          'RK-PR':3, 
          'PC-SAFT':4, 
          'SPHCT':6}

VC_RATIO = 1.168    #relation MODEL/EXPERIMENTAL for critical volumen
TIMEOUT = 10 #seconds to timeout the calculation 
