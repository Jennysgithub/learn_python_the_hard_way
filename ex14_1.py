"""
Write a program that takes a username as an argument from the command line and save it to a variable.
Your program then should:
    1) Print the string "Hello, my name is <variable from above>".
    2) Ask the user to enter a number.
    3) Print the string: "You entered the number <number from above>".
    
For example, if we run the program like this: python ex14_1.py Jenny
then the program will output:

Hello, my name is Jenny.
Please enter a number: ...
You entered the number ...
"""

from sys import argv

program_name, user_name = argv

print "Hello, my name is {}.".format(user_name)

print "Please enter a number:"
yogurt = raw_input()

print "You entered the number {}.".format(yogurt)