"""
Write a program that asks the user for a username.
The program should accept three input parameters when run from the command line.
The three input parameters are the names of two input files and the name of an output file.
The program then will write some data to the output file.
The first line of the output file should be the following string: Hello <username>.
The next line in the output file should be left blank.
Then the following line should be the following string: Here are the contents of <input_file_1>:
The following lines should be the contents of the first input file.
After this, there should be one blank line in the output file.
Then the following line should be the following string: Here are the contents of <input_file_2>:
The following lines should be the contents of the second input file.
--------------------------------------------------------------------------------
FULL EXAMPLE:

Suppose the first input file, which is called working_with_files_2_input_1.txt has the following contents:

This is the first line of the first input file.
And this is the second line.
This is the last one.

Suppose the second input file, which is called working_with_files_2_input_2.txt has the following contents:

Input file 2, line #1
This file is shorter.

Suppose that we want our output file to be called working_with_files_2_output.txt

Then, when we run this program like this in the terminal:

python working_with_files_2.py working_with_files_2_input_1.txt working_with_files_2_input_2.txt working_with_files_2_output.txt

Our program will ask for the username and, assuming that for example we enter the name "Jenny",
then, after the program finishes, the contents of the output file working_with_files_2_output.txt should be:

Hello Jenny.

Here are the contents of working_with_files_2_input_1.txt:
This is the first line of the first input file.
And this is the second line.
This is the last one.

Here are the contents of working_with_files_2_input_1.txt:
Input file 2, line #1
This file is shorter.
"""
from sys import argv

file_name, from_file1, from_file2, to_file = argv

from_fh1 = open(from_file1)
indata1 = from_fh1.read()

from_fh2 = open(from_file2)
indata2 = from_fh2.read()

username = raw_input("What is your name?")

to_fh = open(to_file, 'w')

line1 = "Hello {}!\n\n".format(username)
to_fh.write(line1)
line2 = "Here are the contents of {}: \n".format(from_file1)
to_fh.write(line2)

to_fh.write(indata1)
to_fh.write('\n\n')

line3 = "Here are the contents of {}: \n".format(from_file2)
to_fh.write(line3)

to_fh.write(indata2)

from_fh1.close()
from_fh2.close()
to_fh.close()






