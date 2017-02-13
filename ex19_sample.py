"""
Write a function that takes two numbers as input and returns the sum of the numbers.

Write a program that asks the uses to enter two numbers.
Then with those two numbers, call your function from above and print the result to the terminal.
"""
def numbers_sum(number1, number2):
    return number1 + number2

number1 = int(raw_input("Please enter the first number: "))
number2 = int(raw_input("Please enter the second number: "))

print numbers_sum(number1, number2)