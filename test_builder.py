# -*- coding: utf-8 -*-
# unit test case of builder

import unittest
from builder import Builder

class TestBuilder(unittest.TestCase):
    
    def assertEmptyData(self, product):
        """ assert that the product list has empty headers and data """
        self.assertEqual(0, len(product))

    def assertDataValue(self, product, row, key, value):
        self.assertEqual(value, product[row][key])

    def assertDataLength(self, product, length):
        self.assertEqual(length, len(product))

    def testCallingNewDataResetsData(self):
        b = Builder()
        b.addHeader('first')
        b.newData()
        p = b.getData()
        self.assertEmptyData(p)

    def testAddHeaderDoesNotProduceData(self):
        b = Builder()
        b.addHeader('blue')
        b.addHeader('green')
        p = b.getData()
        self.assertDataLength(p, 0)

    def testAddItem(self):
        b = Builder()
        b.addHeader('Rome')
        b.addItem('1AD')
        p = b.getData()
        self.assertDataLength(p, 1)
        self.assertDataValue(p, 0, 'Rome', '1AD')    

    def testAddTwoItems(self):
        b = Builder()
        b.addHeader('City')
        b.addHeader('Year')
        b.addItem('Rome')
        b.addItem('1AD')
        p = b.getData()
        self.assertDataLength(p, 1)
        self.assertDataValue(p, 0, 'City', 'Rome')    
        self.assertDataValue(p, 0, 'Year', '1AD')    

    def testAddTwoRows(self):
        b = Builder()
        b.addHeader('Year')
        b.addItem('1AD')
        b.newRow()
        b.addItem('100BC')
        p = b.getData()
        self.assertDataLength(p, 2)
        self.assertDataValue(p, 0, 'Year', '1AD')    
        self.assertDataValue(p, 1, 'Year', '100BC')    

    def testAddingTooManyValuesThrowsException(self):
        b = Builder()
        b.addHeader('Year')
        b.addItem('1AD')
        """ this next method should throw the exception """
        self.assertRaises(Exception, b.addItem, '100BC')

# run that test thing
if __name__ == '__main__':
    unittest.main()

