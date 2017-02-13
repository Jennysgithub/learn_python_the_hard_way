from random import randint
from sys import argv

def count_matches(number1, number2, number3, gn1, gn2, gn3):
    match = 0

    if number1 == gn1:
        match = match + 1
        # Compare number2 with gn2 and gn3
        if number2 == gn2:
            match = match + 1
            # Compare number3 with gn3
            if number3 == gn3:
                match = match + 1
        elif number2 == gn3:
            match = match + 1
            # Compare number3 with gn2
            if number3 == gn2:
                match = match + 1
        elif number3 == gn2:
            match = match + 1
        elif number3 == gn3:
            match = match + 1
    elif number1 == gn2:
        match = match + 1
        # Compare number2 with gn1 and gn3
        if number2 == gn1:
            match = match + 1
            # Compare number3 with gn3
            if number3 == gn3:
                match = match + 1
        elif number2 == gn3:
            match = match + 1
            # Compare number3 with gn1
            if number3 == gn1:
                match = match + 1
        elif number3 == gn1:
            match = match + 1
        elif number3 == gn3:
            match = match + 1
    elif number1 == gn3:
         match = match + 1
         # Compare number2 with gn1 and gn2
         if number2 == gn1:
             match = match + 1
             # Compare number3 with gn2
             if number3 == gn2:
                 match = match + 1
         elif number2 == gn2:
             match = match + 1
             # Compare number3 with gn1
             if number3 == gn1:
                 match = match + 1
         elif number3 == gn1:
             match = match + 1
         elif number3 == gn2:
             match = match + 1  
    elif number2 == gn1:
        match = match + 1
        # Compare number3 with gn2 and gn3
        if number3 == gn2:
            match = match + 1
        elif number3 == gn3:
            match = match + 1
    elif number2 == gn2:
        match = match + 1
        # Compare number3 with gn1 and gn3
        if number3 == gn1:
            match = match + 1
        elif number3 == gn3:
            match = match + 1
    elif number2 == gn3:
        match = match + 1
        # Compare number3 with gn1 and gn2
        if number3 == gn1:
            match = match + 1
        elif number3 == gn2:
            match = match + 1
    elif number3 == gn1:
        match = match + 1
    elif number3 == gn2:
        match = match + 1
    elif number3 == gn3:
        match = match + 1
        
    return match


file_name, to_file = argv

number1 = int(raw_input("Please enter a number: "))
number2 = int(raw_input("Please enter a number: "))
number3 = int(raw_input("Please enter a number: "))

gn1 = randint(1,10)
gn2 = randint(1,10)
gn3 = randint(1,10)

print "{} {} {}".format(gn1,gn2,gn3)


to_fh = open(to_file, 'a')
line = "{} {} {}\n".format(gn1,gn2,gn3)
to_fh.write(line)
to_fh.close()

match = count_matches(number1, number2, number3, gn1, gn2, gn3)
             
if match == 0:    
    print "0/3 Maybe next time?"
elif match == 1:
    print "1/3 Oh well, at least you got your money back."
elif match == 2:
    print "2/3 Oh so close, big win!"
elif match == 3:
    print "3/3 Congratulations! You have won the jackpot!!!"             