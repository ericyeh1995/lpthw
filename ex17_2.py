from sys import argv
from os.path import exists

script, from_file, to_file = argv

f = open(from_file)
t = open(to_file, 'w')
t.write(f.read())

print "ok"

f.close()
t.close()


