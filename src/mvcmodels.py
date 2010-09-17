#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

#pubsub
from wx.lib.pubsub import Publisher as pub

#constants
from settings import VC_RATIO

class ModelCompound(object):
    def __init__(self, id,  name, tc, pc, vc, acentric_factor, vc_rat=VC_RATIO):
        self._id = id     
        self._name = name        
        self.set_compound_vars(tc, pc, vc, acentric_factor, vc_rat)

        self.ac = self.b = self.m = 0.0
        self.omega = self.k = 0.0
        self.e_k = self.ro = 0.0
        self.t_asterisk = self.v_asterisk = self.c = 0.0

    def __unicode__(self):
        return unicode(self.__dict__)

    def __repr__(self):
        return pprint.pformat(self.__dict__)

    def get_compound_vars(self):
        return self.tc, self.pc, self.vc, self.acentric_factor, self.vc_rat

    def get_eos_vars(self, model):
        if model == 1 or model == 2:
            return self.ac, self.b, self.m
        elif model == 3:
            return self.ac, self.b, self.omega, self.k
        elif model == 4:
            return self.e_k, self.ro, self.m
        elif model == 6: 
            return self.t_asterisk, self.v_asterisk, self.c


    def set_compound_vars(self, tc, pc, vc, acentric_factor, vc_rat):
        self.tc = tc                            #Tc [K]', 'Critical temperature'
        self.pc = pc                            #Pc [bar]', 'Critical Pressure'
        self.vc = vc                            #Vol [l/mol]', 'Critical Volume'
        self.acentric_factor = acentric_factor  #'Acentric Factor'
        self.vc_rat = vc_rat
        pub.sendMessage('compound vars changed', self.get_compound_vars()) 
   
    def set_eos_vars(self, model, *params):
        #TODO: should be some kind of hook for allow New models whitout hack this code. 
        
        if model == 1 or model == 2:          #Soave-Redlich-Kwong #Peng-Robinson
            self.ac, self.b, self.m = params
        elif model == 3:       #RK-PR
            self.ac, self.b, self.omega, self.k = params
        elif model == 4:       #PC-SAFT
            self.e_k, self.ro, self.m = params        
        elif model == 6:       #SPHCT - simplified perturbed hard chain theory
            self.t_asterisk, self.v_asterisk, self.c = params

        pub.sendMessage('eos vars changed', ( model, self.get_eos_vars(model) ) )
            

class ModelCase(object):
    def __init__(self, eos_model=None, compound1=None, compound2):
        self.set_eos_model(eos_model)
        self.set_compound(compound1, compound2)
        self.extra_vars(combining_rule=0, max_p=2000.0, k12=0.0, l12=0.0)

    def set_eos_model (self, eos_model):
        self.eos_model = eos_model
        pub.sendMessage('model eos model changed', self.eos_model) 

    def set_compounds(self, compound1, compound2):
        self.compound1 = compound1
        self.compound2 = compound1
        pub.sendMessage('model compounds changed', (self.compound1, self.compound2) )
    
    def set_extra_vars(self, **params):
        for param in params.keys():
            setattr(self, param, params[param])
        pub.sendMessage('model extra vars changed', (self.combining_rule, self.max_p, self.k12, self.l12)) 
   


class ControllerCase(object):
    def __init__(self):
        self.model = mvcmodels.ModelsCase()
        



        
