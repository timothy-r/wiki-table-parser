# -*- coding: utf-8 -*-
# integration test case of parser

import unittest
from attribute_list import AttributeList

class TestAttributeList(unittest.TestCase):

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    def testEmptyAttributeListContainsNothing(self):
        """ test that an empty AttributeList contains no values """
        l = []
        alist = AttributeList(l)
        key = 'a'
        value = '2'
        self.assertFalse(alist.contains(key, value))

    def testAttributeListContains(self):
        """ tests AttributeList with values reports that it contains them """
        key = 'a'
        value = '2'
        l = [(key, value)]
        alist = AttributeList(l)
        self.assertTrue(alist.contains(key, value))
