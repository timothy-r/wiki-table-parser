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

    def test_parse_missing_reads_no_data(self):
        """ test simple table parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_missing_fixture()
        p.feed(html)
        # assert b.getData() has one empty list
        product = b.getData()
        self.assertTrue(1 == len(product))
        self.assertTrue(0 == len(product[0]))

    def get_missing_fixture(self):
        """ return html that contains no table data """
        return '<html></html>'


# run that test thing
if __name__ == '__main__':
    unittest.main()
