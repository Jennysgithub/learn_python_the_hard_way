from sys import exit 

number1 = int(raw_input("Please enter the number: "))
number2 = int(raw_input("Please enter the number: "))
number3 = int(raw_input("Please enter the number: "))
number4 = int(raw_input("Please enter the number: "))
number5 = int(raw_input("Please enter the number: "))
number6 = int(raw_input("Please enter the number: "))
number7 = int(raw_input("Please enter the number: "))
number8 = int(raw_input("Please enter the number: "))
number9 = int(raw_input("Please enter the number: "))
number10 = int(raw_input("Please enter the number: "))

even = 0
odd = 0

if number1 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
    
if number2 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
                    
if number3 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
if number4 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
                           
if number5 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
           
if number6 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if number7 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
if number8 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
       
if number9 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
    
if number10 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
        
print "You entered {} even numbers and {} odd numbers.".format(even,odd)    

if even > odd:
    print "It looks like you like even numbers more than odd numbers."
    
elif even < odd:
    print "It looks like you like odd numbers more than even numbers."    

else:
    print "It looks like you like even and odd numbers the same."