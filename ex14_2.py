

from sys import argv

program_name, user_name = argv

blue = '\t*' # \t means tab (4 spaces)

print "What is your name fellow?"
name = raw_input()

print "{}, welcome to my new amazin program!".format(name)

print "What is your favourite number {}?".format(name)
number = raw_input()

print "Here is {} kisses for you, {}.".format(number, name)

print "What is your favourite animal?"
animal = raw_input(blue)

print "What is you second favourite animal?"
animal_1 = raw_input(blue)

print "{} plus {} equal love".format(animal, animal_1)



