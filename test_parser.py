# -*- coding: utf-8 -*-
# integration test case of parser

import unittest
from parser import WikiTableParser
from builder import Builder

class TestParser(unittest.TestCase):
    
    product = []

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    def assertEmptyData(self, product):
        """ assert that the product list has empty headers and data """
        self.assertEqual(1, len(product))
        self.assertEqual(0, len(product[0]))

    def assertHeaderLength(self, product, length):
        self.assertEqual(length, len(product[0]))
        
    def assertOneHeader(self, product, value):
        self.assertEqual(1, len(product))
        self.assertHeaderLength(product, 1)
        self.assertHeaderValue(product, 0, value)

    def assertHeaderValue(self, product, index, value):
        self.assertEqual(value, product[0][index])

    def assertDataValue(self, product, row, index, value):
        self.assertEqual(value, product[row][index])

    def whenProductIsGenerated(self, html):
        b = Builder()
        p = WikiTableParser(b)
        p.feed(html)
        self.product = b.getData()

    def testParseMissingReadsNoData(self):
        """ test parsing no table """
        html = self.get_missing_fixture()
        self.whenProductIsGenerated(html)

        self.assertEmptyData(self.product)

    def testParseNonhtmlReadsNoData(self):
        """ test parsing non-html string """
        html = self.get_non_html()
        self.whenProductIsGenerated(html)

        self.assertEmptyData(self.product)

    def testParseWrongTableReadsNoData(self):
        """ test parsing no table """
        html = self.get_wrong_table_fixture()
        self.whenProductIsGenerated(html)

        self.assertEmptyData(self.product)

    def testParseSingleHeader(self):
        """ test simple table header parsing """
        html = self.get_single_header_fixture()
        self.whenProductIsGenerated(html)

        self.assertOneHeader(self.product, 'one')

    def testMultiClassTable(self):
        """ test simple table header parsing """
        html = self.get_multi_class_fixture()
        self.whenProductIsGenerated(html)
        self.assertOneHeader(self.product, 'one')

    def testParseMultiHeader(self):
        """ test simple table header parsing """
        html = self.get_multi_header_fixture()
        self.whenProductIsGenerated(html)

        self.assertEqual(1, len(self.product))
        self.assertHeaderLength(self.product, 3)
        self.assertHeaderValue(self.product, 0, 'one')
        self.assertHeaderValue(self.product, 1, 'two')
        self.assertHeaderValue(self.product, 2, 'three')

    def testParseTableData(self):
        """ test single row table data parsing """
        html = self.get_table_data_fixture()
        self.whenProductIsGenerated(html)
        self.assertEqual(2, len(self.product))
        self.assertHeaderValue(self.product, 0, 'one')
        self.assertHeaderValue(self.product, 1, 'two')
        self.assertDataValue(self.product, 1, 0, '1')
        self.assertDataValue(self.product, 1, 1, 'England')

    def testIgnoreHiddenValues(self):
        """ test parser ignores data flagged as hidden """
        html = self.get_hidden_cell_data_fixture()
        self.whenProductIsGenerated(html)

        self.assertDataValue(self.product, 1, 0, 'Show this')

    def get_non_html(self):
        """ return a non-html string """
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

    def get_hidden_cell_data_fixture(self):
        """ return html that contains hidden cell data """
        return '<html><body><table class="wikitable"><tr><th>one</th></tr><tr><td><span style="display:none;">Hidden text </span>Show this</td></tr></table></body></html>'


# run that test thing
if __name__ == '__main__':
    unittest.main()


