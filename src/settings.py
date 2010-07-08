#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, sys

#path where fortran executables are
PATH_BIN = os.path.join( os.getcwd(), "bin" )

#path where fortran executables are
PATH_TEMP = os.path.join( os.getcwd(), "tmp" )   

PATH_ICONS = os.path.join( os.getcwd(), "icons" )

_models = {'Soave-Redlich-Kwong':1, 
          'Peng-Robinson':2,
          'RK-PR':3, 
          'PC-SAFT':4, 
          'SPHCT':6}
