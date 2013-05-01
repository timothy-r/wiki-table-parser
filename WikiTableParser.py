# take a wiki table from a html source and return an assoc data array
# [	
#	 {"name":"x", "key":"value", "other-key":"more"}
# ], ...
#

from HTMLParser import HTMLParser

class WikiTableParser(HTMLParser):
    data = []
    state = 'none' # also 'table' 'header-row' (reading header row)  'header-cell' and 'data-row' (reading regular row) 'data-cell'
    key = ''

    def __init(self):
        self.data = []
	
	# if tag == table and state == 'none' attrs.class contains wikitable then state = 'table'
    def set_table_state(self, attrs):
        for t in attrs:
            if t[0] == 'class' and 0 == t[1].find('wikitable'):
                self.state = 'table'
                return
        self.state = 'none'

    def set_row_state(self, location):
        # if in a table then state = header-row otherwise
        if 'table' == self.state:
            self.state = 'header-row'
        elif 'header-row' == self.state:
            self.state = 'data-row'

    def set_cell_state(self):
        if 'data-row' == self.state:
            self.state = 'data-cell'

    def handle_starttag(self, tag, attrs):
        if 'table' == tag:
			self.set_table_state(attrs)
        elif 'tr' == tag:
            self.set_row_state('start')
        elif 'th' == tag:
            self.state = 'header-cell'
        elif 'td' == tag:
            self.set_cell_state()

    def handle_endtag(self, tag):
        if self.state == 'table':
            print "tag : ", tag

    def handle_data(self, data):
        if self.state == 'header-cell':
            print "header data  : ", data

# instantiate the parser and fed it some HTML
parser = WikiTableParser()
parser.feed('<table class="wikitable sortable" style="text-align: right"><tr><th>Rank<br /></th><th>Country</th><th>Total in km (sq mi)</th><th>Land in km (sq mi)</th><th>Water in km (sq mi)</th><th>&#160;% water</th><th class="unsortable">Notes</th></tr><tr><td><span style="display:none">7000100000000000000</span>1</td><td align="left"><span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/22px-Flag_of_Russia.svg.png" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/33px-Flag_of_Russia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/44px-Flag_of_Russia.svg.png 2x" />&#160;</span><a href="/wiki/Russia" title="Russia">Russia</a></td><td><span style="display:none">7007170982420000000</span>17,098,242<br />(6,601,668)</td><td><span style="display:none">7007163777420000000</span>16,377,742<br />(6,323,482)</td><td><span style="display:none">7005720500000000000</span>720,500<br />(278,200)</td><td>4.21</td><td align="left">Largest country in the world.</td></tr><tr>')
