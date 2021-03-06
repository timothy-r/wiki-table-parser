# python runner
import sys
from table_parser import *
from builder import Builder

# 1 download a file from a url
#print sys.argv[1]

name = sys.argv[1]

# 2 read file from args[1] into a string
f = open(name,'r')

# 3 use a WikiTableParser to read data from the string into object / array
b = Builder()
p = WikiTableParser(b)

p.feed(f.read())

# 4 write the data back out as json
#rows = p.getData()

rows = b.getData()

for d in rows:
    print d
