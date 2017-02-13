from sys import argv

script, file_name = argv

print "We are going to erase {}.".format(file_name)
print "If you do not want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(file_name, 'w')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
target.close()