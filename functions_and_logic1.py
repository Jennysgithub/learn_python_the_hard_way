def ask_for_name():
    persons_name = raw_input("Please enter a person's name:")
    return persons_name
    
def ask_for_age():
    name = ask_for_name()
    age = int(raw_input("How old is {}?".format(name)))
    return age 


person1 = ask_for_age()
person2 = ask_for_age()


if person1 > person2:
    print "{} is older than {}".format(name1, name2)
    
if person1 < person2:
    print "{} is older than {}.".format(name1, name2)  
    
if person1 == person2:
    print "{} and {} are the same age.".format(name1, name2)     

    