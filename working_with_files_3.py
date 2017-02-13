"""
Write a program that takes two arguments when called from the command line.
The arguments represent two output files, so your program will write two output files.

The program will then ask the user to enter 10 numbers, one at a time, as follows:
The program asks for the first number, the user enters the number.
The program asks for the second number, the user enters the second number.
...
and so on until the program asks for the tenth number and the user enters it.

The program will then write the numbers that the user entered to both output files as follows:

The contents of the first output file will be the numbers that the user entered, one number per line,
in the same order as the user entered the numbers, so this file will have 10 lines.

The contents of the second output file will be the numbers that the user entered, all the numbers on the same line,
separated by commas (,). So this output file will have just one line.

BONUS POINT: Print to the terminal the sum of the numbers that the user entered!
--------------------------------------------------------------------------
FULL EXAMPLE:

If we call the program like this:
python working_with_files_3.py wwf_3_output_1.txt wwf_3_output_2.txt

Then in the terminal we will see the following, for example:

Please enter a number: 1
Please enter a number: 2
Please enter a number: 3
Please enter a number: 4
Please enter a number: 5
Please enter a number: 6
Please enter a number: 7
Please enter a number: 8
Please enter a number: 9
Please enter a number: 10

After the 10th number, the program finishes, and if we open the output files these are their contents:

wwf_3_output_1.txt has these contents:

1
2
3
4
5
6
7
8
9
10

wwf_3_output_2.txt has these contents:

1,2,3,4,5,6,7,8,9,10



NOTE, if you did the BONUS POINTS, then in the terminal you should be printing the number 55,
since = 55
"""


from sys import argv

file_name, to_file1, to_file2 = argv

number1 = raw_input("Please enter the first number: ")
number2 = raw_input("Please enter the second number: ")
number3 = raw_input("Please enter the third number: ")
number4 = raw_input("Please enter the fourth number: ")
number5 = raw_input("Please enter the fifth number: ")
number6 = raw_input("Please enter the sixth number: ")
number7 = raw_input("Please enter the seventh number: ")
number8 = raw_input("Please enter the eightth number: ")
number9 = raw_input("Please enter the nineghth number: ")
number10 = raw_input("Please enter the tenth number: ")

to_fh1 = open(to_file1, 'w')

line1 = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(
number1, number2, number3, number4, number5, number6, number7, number8, number9, number10
)
to_fh1.write(line1)

to_fh2 = open(to_file2, "w")

line2 = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}" .format(
number1, number2, number3, number4, number5, number6, number7, number8, number9, number10
)

to_fh2.write(line2)

to_fh1.close()
to_fh2.close()

print int(number1) + int(number2) + int(number3) + int(number4) + int(number5) + int(number6) + int(number7) + int(number8) + int(number9) + int(number10)
 















