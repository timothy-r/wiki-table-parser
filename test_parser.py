# -*- coding: utf-8 -*-
# test case of parser
import unittest
from parser import WikiTableParser
from builder import Builder

class TestParser(unittest.TestCase):

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    def test_parse(self):
        """ test simple table parsing """
        self.assertTrue(1)
        b = Builder()
        p = WikiTableParser(b)



# run that test thing
if __name__ == '__main__':
    unittest.main()
