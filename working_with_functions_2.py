"""
Write a function that takes a number as input and returns the number multiplied by 10.

You should name this function: multiply_by_10
"""
# function code here ...
def multiply_by_10(number):
    return number * 10
"""
Write a function that when called, will ask the user for a number, and then it will return the number that the user entered.

You should name this function: ask_for_a_number
"""
# function code here ...
def ask_for_a_number():
    input_number = int(raw_input("Please enter the number:"))
    return input_number
"""
Write a function that takes two arguments, the first argument is a number and the second argument is the name of a file.
The function should write the number passed as argument to the file specified by file name.

You should name this function: write_number_to_file
"""
# function code here ...
def write_number_to_file(number, file_name):
    fh = open(file_name, "w")
    fh.write(str(number))
    fh.close()

"""
Your main program:

Step 1: Ask the user to enter a file name.
Step 2: Ask the user to enter a number by calling the function ask_for_a_number that you created.
Step 3: Using the number that the user entered, call the function multiply_by_10 that you created.
Step 4: Print the result of step 3 to the terminal.
Step 5: Using the number that the user entered from Step 2, and the file name that the user entered from Step 1),
        call the function write_number_to_file that you created.

"""

file_name = raw_input("Please enter a file name")

number = ask_for_a_number()
print multiply_by_10(number)
write_number_to_file(number, file_name)

