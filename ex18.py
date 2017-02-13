# This function takes a username as an argument and prints the string:
# Hello <username>
def say_hello(username):
    print "Hello {}".format(username)

def get_greeting(username):
    return "Greetings there, {}".format(username)

print "Hey There!"

# Calling the say_hello function
say_hello("Joel")

# Jenny is calling it now
say_hello("Jenny")

greeting_for_joel = get_greeting("Joel")
greeting_for_jenny = get_greeting("Jenny")

print greeting_for_joel
print greeting_for_jenny

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: {}, arg2: {}".format(arg1,arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: {}, arg2: {}".format(arg1,arg2)

# this one just takes one argument
def print_one(arg1):
    print "arg1: {}".format(arg1)
    
# this one takes no arguments
def print_none():
    print "I got nothing"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()