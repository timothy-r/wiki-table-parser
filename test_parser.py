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
        """ test parsing no table """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_missing_fixture()
        p.feed(html)
        # assert b.getData() has one empty list
        product = b.getData()
        self.assertTrue(1 == len(product))
        self.assertTrue(0 == len(product[0]))

    def test_parse_single_header(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_single_header_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertTrue(1 == len(product))
        self.assertTrue(1 == len(product[0]))
        self.assertTrue('one' == product[0][0])

    def test_multi_class_table(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_multi_class_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        print product
        self.assertTrue(1 == len(product))
        self.assertTrue(1 == len(product[0]))
        self.assertTrue('one' == product[0][0])


    def test_parse_multi_header(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_multi_header_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertTrue(1 == len(product))
        self.assertTrue(3 == len(product[0]))
        self.assertTrue('one' == product[0][0])
        self.assertTrue('two' == product[0][1])
        self.assertTrue('three' == product[0][2])


    def get_missing_fixture(self):
        """ return html that contains no table data """
        return '<html></html>'

    def get_single_header_fixture(self):
        """ return html that contains one header value """
        return '<html><body><table class="wikitable"><tr><th>one</th></tr></table></body></html>'

    def get_multi_header_fixture(self):
        """ return html that contains one header value """
        return '<html><body><table class="wikitable"><tr><th>one</th><th>two</th><th>three</th></tr></table></body></html>'

    def get_multi_class_fixture(self):
        """ return html that contains multiple table classes value """
        return '<html><body><table class="ouch wikitable other"><tr><th>one</th></tr></table></body></html>'


# run that test thing
if __name__ == '__main__':
    unittest.main()
