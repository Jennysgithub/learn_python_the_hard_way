from sys import argv

file_name, from_file, to_file = argv

from_fh = open(from_file)
indata = from_fh.read()

username = raw_input("What is your name?")

to_fh = open(to_file, 'w')

line1 = "Hello {}, here is some text from another file: \n".format(username)
to_fh.write(line1)

to_fh.write(indata)

line2 = "\nGoodbye {}".format(username)
to_fh.write(line2)

from_fh.close()
to_fh.close()





