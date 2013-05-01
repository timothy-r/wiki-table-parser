# python runner
import sys
from wiki_table_parser import WikiTableParser

print sys.argv[1]

name = sys.argv[1]

# 1 read file from args[1] into a string
f = open(name,'r')
#print f

# 2 use a WikiTableParser to read data from the string into object / array
p = WikiTableParser();
p.feed(f.read())
# 3 write the data back out as json
rows = p.getData()

print rows
