"""
1)
Write a function that takes as an input argument the name of a file.
The function should read the contents of the file and then return this content.

2)
Write a function that takes three input arguments.
The first argument is the name of an output file.
The second and third arguments are the names of two input files.
The function should then use the function that you write in 1) to read the contents of both input files.
The function should finally write the contents of the first and second input files to the output file, separated by a blank line.
So, for example, if the contents of the first input file are:
Line 1: Something
Line 2: Something

And the contents of the second input file are:
Second file line # 1
Second file line # 2
Second file line # 3

Then, the contents of the output file should be:
Line 1: Something
Line 2: Something

Second file line # 1
Second file line # 2
Second file line # 3



You are responsible for creating the two input files. You can put whatever text you wish into both of these files.

In your program, you need to call the function that you define in 2) above.
Remember that function 2) takes three input arguments which are the names of some files.
It is up to you to decide how you want these names to be available in your program, for example:
You can use argv to read them when you call the program, or you can use the raw_input function 
to ask the user to enter these names. Do what you think it's best.
"""
from sys import argv
file_name, output_file, input_file1, input_file2 = argv

def file_content_read(file_name):
    fh = open(file_name)
    indata = fh.read()
    fh.close()
    return indata
    
    
def write_from_the_files_to_the_file(output_file, input_file1, input_file2):
    content1 = file_content_read(input_file1)
    content2 = file_content_read(input_file2)
    fh = open(output_file, "w")
    fh.write(content1)
    fh.write("\n")
    fh.write(content2)
    fh.close()
    
write_from_the_files_to_the_file(output_file, input_file1, input_file2)    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    