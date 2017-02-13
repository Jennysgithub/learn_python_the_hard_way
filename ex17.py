from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from {} to {}".format(from_file, to_file)

from_fh = open(from_file)
indata = from_fh.read()

print "The input file is {} bytes long".format(len(indata))

print "Does the output file exist? {}".format(exists(to_file))
print "Ready, hit return to continue, CTRL-C to abort."
raw_input()

to_fh = open(to_file, 'w')
to_fh.write(indata)

print "Alright, all done."  

from_fh.close()
to_fh.close()