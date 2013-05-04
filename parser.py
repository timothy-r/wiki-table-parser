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
   
    def attrContains(self, attrs, key, value):
        """ test if attribute with key contains a value """
        for t in attrs:
            if t[0] == key and -1 != t[1].find(value):
                return True

        return False

	# if tag == table and state == 'none' attrs.class contains wikitable then state = 'table'
    def setTableState(self, attrs, location):
        if 'start' == location:
            if (self.attrContains(attrs, 'class', 'wikitable')):
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
                self.builder.newRow()

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
                self.builder.addHeader(self.current)
                self.current = ''

    def handle_starttag(self, tag, attrs):
        self.hidden = self.attrContains(attrs, 'style', 'display:none')

        if 'table' == tag:
			self.setTableState(attrs, 'start')
        elif 'tr' == tag:
            self.setRowState('start')
        elif 'th' == tag:
            self.setCellState('th', 'start')
        elif 'td' == tag:
            self.setCellState('td', 'start')

    def handle_endtag(self, tag):
        self.hidden = False

        if 'table' == tag:
			self.setTableState('', 'end')
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

