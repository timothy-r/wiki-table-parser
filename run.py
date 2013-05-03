# python runner
import sys
from parser import WikiTableParser

# 1 download a file from a url
print sys.argv[1]

name = sys.argv[1]

# 2 read file from args[1] into a string
f = open(name,'r')
#print f

# 3 use a WikiTableParser to read data from the string into object / array
p = WikiTableParser();
p.feed(f.read())

# 4 write the data back out as json
rows = p.getData()

print rows
