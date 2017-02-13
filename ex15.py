from sys import argv

script, file_name = argv

file_handler = open(file_name) # Step 1: Open the file


print "Here is your file {}:".format(file_name)

content = file_handler.read() # Step 2: Do stuff with the file, in this case just read its contents
print content

file_handler.close() # Step 3: Close the file