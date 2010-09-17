#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mvcmodels
 
#pubsub
from wx.lib.pubsub import Publisher as pub






class ControllerCompound(object):
    def __init__(self, view):
        self.view = view
        self.model = mvcmodels.ModelCompound(12, 'carbono', 23.0, 34.5, 345, 1.23)
        pub.subscribe(self.compound_vars_change, "compound vars changed")


    def compound_vars_change(self, message):
        data = message.data
        self.view.SetParamsValues(data)


def main():
    
    return 0

if __name__ == '__main__':
    main()
