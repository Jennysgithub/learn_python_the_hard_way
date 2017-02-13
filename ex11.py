print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're {} old, {} tall and {} heavy.".format(age, height, weight)

print "THIS IS A TEST"
print age * 10 # If age == 32, it will print 32323232323232323232
print int(age) * 10 # If age == 32, it will print 320