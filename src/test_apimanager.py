#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
import apimanager

from settings import _models

class TestApiManager(unittest.TestCase):
    
    def setUp(self):
        self.vars_input = ['190.564', '45.99', '0.098', '0.01154']

    def test_comparin1(self):
        
        apimanager.write_conparin(0, 1, self.vars_input)
        self.general()

    def general(self):
        out = apimanager.read_conparout()
        tmp_var =  out[0] 
        salida = tmp_var[:-2] + [tmp_var[-1], tmp_var[-2]]

        self.assertEqual(map(float, salida), map(float, self.vars_input ))
    
    def test_comparin2(self):
        apimanager.write_conparin(0, 2, self.vars_input)
        self.general()

    def test_comparin3(self):
        apimanager.write_conparin(0, 3, self.vars_input)
        self.general()
        
    def test_comparin4(self):
        apimanager.write_conparin(0, 4, self.vars_input)
        self.general()

    def test_comparin6(self):
        apimanager.write_conparin(0, 6, self.vars_input)
        self.general()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiManager)
    unittest.TextTestRunner(verbosity=2).run(suite)

