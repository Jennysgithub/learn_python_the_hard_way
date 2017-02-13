"""
Write a function that takes two strings as input arguments.
The function should return a new string which consists of the two input strings separated by a space.

For example, if the function is called with the two input strings "My name is" and "Joel", then the
function should return the string "My name is Joel"
"""
# Function code goes here ...
def main_string(string1, string2):
    return "{} {}".format(string1, string2)
    # return string1 + " " + string2
    

"""
Write a function that takes three arguments as input.
The first two arguments are two numbers.
The third argument is a file name.
The function should calculate the sum of the two numbers and write the result of this sum to the file 
whose name was passed to the function as the third argument.
This function doesn't need to return anything.

For example, if the function is called with the numbers 10, and 15, and with the file name working_with_functions_1_output.txt 
then the contents of the working_with_functions_1_output.txt file should be just the number 25 on the first line and nothing else.
"""
# Function code goes here ...
def info(n1, n2, to_file):
    thesum = n1 + n2
    to_fh = open(to_file, "w")
    to_fh.write("{}".format(thesum))
    to_fh.close()
    
    
    
    
"""
Here is the flow of your program:

The program should be run from the terminal via something like this:

python working_with_functions_1.py working_with_functions_1_output.txt

The program should next ask the user to enter two strings, one at a time.
After the user enters both strings, the program should use these two strings to call the first function that you created from above.
The result of calling this function should be printed to the terminal.

After this, the program should then ask the user to enter two numbers, one at a time.
After the user enters both numbers, the program should then call the second function that you created from above. When calling this 
second function that you created, you will need to pass in both numbers and the name of the output file that you used when running the program in the terminal.
"""

from sys import argv

script, to_file = argv

string1 = raw_input("Please enter a string:")
string2 = raw_input("Please enter another string:")

new_string = main_string(string1, string2)
print new_string

n1 = int(raw_input("Please enter a number:"))
n2 = int(raw_input("please enter another number:"))

info(n1, n2, to_file)













