# take a wiki table from a html source and call appropriate builder methods
# acts as the director in the builder pattern
# [	
#	 {"name":"x", "key":"value", "other-key":"more"}
# ], ...

from HTMLParser import HTMLParser

class WikiTableParser(HTMLParser):
    builder = 0
    current = ''
    reading = False
    hidden = False

    state = 'none' # also 'table' 'header-row' (reading header row)  'header-cell' and 'data-row' (reading regular row) 'data-cell'

    def __init__(self, builder):
        HTMLParser.__init__(self)
        self.builder = builder
   
	# if tag == table and state == 'none' attrs.class contains wikitable then state = 'table'
    def setTableState(self, alist, location):
        if 'start' == location:
            if (alist.contains('class', 'wikitable')):
                self.state = 'table'
                self.reading = True
                self.builder.newData()
                return
        self.state = 'none'
        self.reading = False

    def setRowState(self, location):
        if not self.reading:
            return

        # if in a table then state = header-row otherwise
        if 'table' == self.state:
            if 'start' == location:
                self.state = 'header-row'
            else:
                self.state = 'none'
        elif 'header-row' == self.state:
            if 'start' == location:
                self.state = 'data-row'
            else:
                self.state = ''
        elif 'data-row' == self.state:
            if 'end' == location:
                self.builder.newSet()

    def setCellState(self, cell, location):
        if not self.reading:
            return

        if 'td' == cell:
            if 'start' == location:
                self.state = 'data-cell'
            else:
                self.state = 'data-row'
                self.builder.addItem(self.current)
                self.current = ''
        elif 'th' == cell:
            if 'start' == location:
                self.state = 'header-cell'
            else:
                self.state = 'header-row'
                self.builder.addKey(self.current)
                self.current = ''

    def handle_starttag(self, tag, attrs):
        alist = AttributeList(attrs)
        self.hidden = alist.contains('style', 'display:none')
        #self.hidden = self.attrContains(attrs, 'style', 'display:none')

        if 'table' == tag:
			self.setTableState(alist, 'start')
        elif 'tr' == tag:
            self.setRowState('start')
        elif 'th' == tag:
            self.setCellState('th', 'start')
        elif 'td' == tag:
            self.setCellState('td', 'start')

    def handle_endtag(self, tag):
        alist = AttributeList([])
        self.hidden = False

        if 'table' == tag:
			self.setTableState(alist, 'end')
        elif 'tr' == tag:
            self.setRowState('end')
        elif 'th' == tag:
            self.setCellState('th', 'end')
        elif 'td' == tag:
            self.setCellState('td', 'end')

    def handle_data(self, data):
        if not self.hidden:
            if self.state == 'header-cell':
                self.current = self.current + '' + data
            elif self.state == 'data-cell':
                self.current = self.current + '' + data


""" Wrapper for an attribute list """

class AttributeList:
    attributes = [];

    def __init__(self, attributes):
        self.attributes = attributes
       
    def contains(self, key, value):
        """ test if attribute with key contains a value """
        for a in self.attributes:
            if a[0] == key and -1 != a[1].find(value):
                return True

        return False

