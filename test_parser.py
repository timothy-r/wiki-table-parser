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
        self.assertEqual(0, len(product))

    def assertDataValue(self, product, row, key, value):
        self.assertEqual(value, product[row][key])

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

    def testParseMultiHeadersReadsNoData(self):
        """ test simple table header parsing """
        html = self.get_multi_header_fixture()
        self.whenProductIsGenerated(html)

        self.assertEmptyData(self.product)

    def testParseTableData(self):
        """ test single row table data parsing """
        html = self.get_table_data_fixture()
        self.whenProductIsGenerated(html)
        self.assertEqual(1, len(self.product))
        self.assertDataValue(self.product, 0, 'one', '1')
        self.assertDataValue(self.product, 0, 'two', 'England')

    def testIgnoreHiddenValues(self):
        """ test parser ignores data flagged as hidden """
        html = self.get_hidden_cell_data_fixture()
        self.whenProductIsGenerated(html)

        self.assertDataValue(self.product, 0, 'one', 'Show this')

    def get_non_html(self):
        """ return a non-html string """
        return 'some non-html>< text'

    def get_missing_fixture(self):
        """ return html that contains no table data """
        return '<html></html>'

    def get_wrong_table_fixture(self):
        """ return html that contains no table data """
        return '<html><body><table class="wrong"><tr><th>no</th></tr></table></body></html>'

    def get_multi_header_fixture(self):
        """ return html that contains one header value """
        return '<html><body><table class="wikitable"><tr><th>one</th><th>two</th><th>three</th></tr></table></body></html>'

    def get_table_data_fixture(self):
        """ return html that contains table data """
        return '<html><body><table class="not wikitable other"><tr><th>one</th><th>two</th></tr><tr><td>1</td><td>England</td></tr></table></body></html>'

    def get_hidden_cell_data_fixture(self):
        """ return html that contains hidden cell data """
        return '<html><body><table class="wikitable"><tr><th>one</th></tr><tr><td><span style="display:none;">Hidden text </span>Show this</td></tr></table></body></html>'


# run that test thing
if __name__ == '__main__':
    unittest.main()


