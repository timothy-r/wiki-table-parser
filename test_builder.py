# -*- coding: utf-8 -*-
# unit test case of builder

import unittest
from builder import Builder

class TestBuilder(unittest.TestCase):
    
    def assertEmptyData(self, product):
        """ assert that the product list has empty headers and data """
        self.assertEqual(1, len(product))
        self.assertEqual(0, len(product[0]))

    def assertHeaderValue(self, product, index, value):
        self.assertEqual(value, product[0][index])

    def assertDataValue(self, product, row, index, value):
        self.assertEqual(value, product[row][index])

    def testNewDataResetsData(self):
        b = Builder()
        b.addHeader('first')
        b.newData()
        p = b.getData()
        self.assertEmptyData(p)

    def testAddHeader(self):
        b = Builder()
        b.addHeader('blue')
        p = b.getData()
        self.assertHeaderValue(p, 0, 'blue')    

    def testAddTwoHeaders(self):
        b = Builder()
        b.addHeader('blue')
        b.addHeader('green')
        p = b.getData()
        self.assertHeaderValue(p, 0, 'blue')    
        self.assertHeaderValue(p, 1, 'green')    

    def testAddItem(self):
        b = Builder()
        b.addHeader('Rome')
        b.addItem('1AD')
        b.newRow()
        p = b.getData()
        self.assertDataValue(p, 1, 0, '1AD')    
