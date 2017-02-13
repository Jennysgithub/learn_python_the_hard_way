from random import randint

n1 = randint(1,100)
n2 = randint(1,100)
n3 = randint(1,100)
n4 = randint(1,100)
n5 = randint(1,100)
n6 = randint(1,100)
n7 = randint(1,100)
n8 = randint(1,100)
n9 = randint(1,100)
n10 = randint(1,100)

even = 0
odd = 0
 
if n1 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
     
if n2 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
             
if n3 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
     
if n4 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
          
if n5 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
     
if n6 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1

if n7 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
     
if n8 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
     
if n9 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1

if n10 % 2 == 0:
     even = even + 1
else:
     odd = odd + 1
          
print "You entered {} even numbers and {} odd numbers".format(even, odd)

if even > odd:
    print "Python likes even numbers more than odd numbers"
   
elif even < odd:
    print "Python likes odd numbers more than even numbers"
       
else: 
    print "Python likes even and odd numbers the same"







          
                       