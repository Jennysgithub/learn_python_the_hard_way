def ask_for_name():
    persons_name = raw_input("Please enter a person's name:")
    return persons_name
    
def ask_for_age(name):
    age = int(raw_input("How old is {}? ".format(name)))
    return age

# Person 1
person_1_name = ask_for_name()
person_1_age = ask_for_age(person_1_name)

# Person 2
person_2_name = ask_for_name()
person_2_age = ask_for_age(person_2_name)

if person_1_age > person_2_age:
    print "{} is older than {}".format(person_1_name, person_2_name)
    
elif person_1_age < person_2_age:
    print "{} is older than {}.".format(person_2_name, person_1_name)  
    
else:
    print "{} and {} are the same age.".format(person_1_name, person_2_name)     
