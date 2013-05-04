# -*- coding: utf-8 -*-
# integration test case of parser

import unittest
from parser import WikiTableParser
from builder import Builder

class TestParser(unittest.TestCase):

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    def assertEmptyData(self, product):
        """ assert that the product list has a single empty item """
        self.assertTrue(1 == len(product))
        self.assertTrue(0 == len(product[0]))

    def assertHeaderLength(self, product, length):
        self.assertTrue(length == len(product[0]))
        
    def assertOneHeader(self, product, value):
        self.assertTrue(1 == len(product))
        self.assertHeaderLength(product, 1)
        self.assertHeaderValue(product, 0, value)

    def assertHeaderValue(self, product, index, value):
        self.assertTrue(value == product[0][index])

    def assertDataValue(self, product, row, index, value):
        self.assertTrue(value == product[row][index])

    def test_parse_missing_reads_no_data(self):
        """ test parsing no table """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_missing_fixture()
        p.feed(html)
        # assert b.getData() has one empty list
        product = b.getData()
        self.assertEmptyData(product)

    def test_parse_non_html_reads_no_data(self):
        """ test parsing non-html string """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_non_html()
        p.feed(html)
        # assert b.getData() has one empty list
        product = b.getData()
        self.assertEmptyData(product)


    def test_parse_wrong_table_reads_no_data(self):
        """ test parsing no table """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_wrong_table_fixture()
        p.feed(html)
        # assert b.getData() has one empty list
        product = b.getData()
        self.assertEmptyData(product)

    def test_parse_single_header(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_single_header_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertOneHeader(product, 'one')

    def test_multi_class_table(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_multi_class_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertOneHeader(product, 'one')

    def test_parse_multi_header(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_multi_header_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertTrue(1 == len(product))
        self.assertHeaderLength(product, 3)
        self.assertHeaderValue(product, 0, 'one')
        self.assertHeaderValue(product, 1, 'two')
        self.assertHeaderValue(product, 2, 'three')

    def test_parse_table_data(self):
        """ test simple table header parsing """
        b = Builder()
        p = WikiTableParser(b)
        html = self.get_table_data_fixture()
        p.feed(html)
        # assert b.getData() has one header list with 1 item
        product = b.getData()
        self.assertTrue(2 == len(product))
        self.assertHeaderValue(product, 0, 'one')
        self.assertHeaderValue(product, 1, 'two')
        self.assertDataValue(product, 1, 0, '1')
        self.assertDataValue(product, 1, 1, 'England')

    def get_non_html(self):
        return 'some non-html>< text'

    def get_missing_fixture(self):
        """ return html that contains no table data """
        return '<html></html>'

    def get_wrong_table_fixture(self):
        """ return html that contains no table data """
        return '<html><body><table class="wrong"><tr><th>no</th></tr></table></body></html>'

    def get_single_header_fixture(self):
        """ return html that contains one header value """
        return '<html><body><table class="wikitable"><tr><th>one</th></tr></table></body></html>'

    def get_multi_header_fixture(self):
        """ return html that contains one header value """
        return '<html><body><table class="wikitable"><tr><th>one</th><th>two</th><th>three</th></tr></table></body></html>'

    def get_multi_class_fixture(self):
        """ return html that contains multiple table classes value """
        return '<html><body><table class="ouch wikitable other"><tr><th>one</th></tr></table></body></html>'

    def get_table_data_fixture(self):
        """ return html that contains table data """
        return '<html><body><table class="wikitable"><tr><th>one</th><th>two</th></tr><tr><td>1</td><td>England</td></tr></table></body></html>'



# run that test thing
if __name__ == '__main__':
    unittest.main()
