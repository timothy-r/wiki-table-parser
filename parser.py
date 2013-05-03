# take a wiki table from a html source and return an assoc data array
# [	
#	 {"name":"x", "key":"value", "other-key":"more"}
# ], ...
#

from HTMLParser import HTMLParser

class WikiTableParser(HTMLParser):
    builder = 0
    data = []
    current = ''
    data_row = []
    header_row = []

    state = 'none' # also 'table' 'header-row' (reading header row)  'header-cell' and 'data-row' (reading regular row) 'data-cell'
    key = ''

    def __init__(self, builder):
        # hack - should call parent __init__ method
        self.reset()
        self.builder = builder
        self.data = []

    def getData(self):
		return self.data

	# if tag == table and state == 'none' attrs.class contains wikitable then state = 'table'
    def set_table_state(self, attrs, location):
        if 'start' == location:
            for t in attrs:
            	if t[0] == 'class' and 0 == t[1].find('wikitable'):
                	self.state = 'table'
                	return
        	self.state = 'none'

    def set_row_state(self, location):
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
                #print self.header_row                
                self.data.append(self.header_row)
                self.header_row = []
        elif 'data-row' == self.state:
            if 'end' == location:
                #print self.data_row
                self.data.append(self.data_row)
                self.data_row = []

    def set_cell_state(self, cell, location):
        if 'td' == cell:
            if 'start' == location:
                self.state = 'data-cell'
            else:
                self.state = 'data-row'
                self.data_row.append(self.current)
                self.current = ''
        elif 'th' == cell:
            if 'start' == location:
                self.state = 'header-cell'
            else:
                self.state = 'header-row'
                self.header_row.append(self.current)
                self.current = ''


    def handle_starttag(self, tag, attrs):
        if 'table' == tag:
			self.set_table_state(attrs, 'start')
        elif 'tr' == tag:
            self.set_row_state('start')
        elif 'th' == tag:
            self.set_cell_state('th', 'start')
            # self.state = 'header-cell'
        elif 'td' == tag:
            self.set_cell_state('td', 'start')

    def handle_endtag(self, tag):
        if 'table' == tag:
			self.set_table_state('', 'end')
        elif 'tr' == tag:
            self.set_row_state('end')
        elif 'th' == tag:
            self.set_cell_state('th', 'end')
            #self.state = 'header-row'
        elif 'td' == tag:
            self.set_cell_state('td', 'end')

    def handle_data(self, data):
        if self.state == 'header-cell':
            self.current = self.current + '' + data
        elif self.state == 'data-cell':
            self.current = self.current + '' + data

