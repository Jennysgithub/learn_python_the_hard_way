hairs = ["brown", "blond", "red"]
eyes = ["brown", "blue", "green"]
weights = [1, 2, 3, 4]

# To get the number of elements in a list,
# we use the len function
# Example:
# l = ['a', b']
# len(l) is 2
number_of_hair_colors = len(hairs)
number_of_eye_colors = len(eyes)
number_of_weights = len(weights)

print "Number of hair colors: {}".format(number_of_hair_colors)
print "Number of eye colors: {}".format(number_of_eye_colors)
print "Number of weights: {}".format(number_of_weights)

# Every element in a list, has a position in the list.
# Positions start at 0 (not 1).
# The position of an element in a list is usually referred to as
# the index of the element.
# For example:
# Given this list:
# l = ['a', 'b', 'c']
# 'a' is at position/index 0
# 'b' is at position/index 1
# 'c' is at position/index 2

print "First hair color is: {}".format(hairs[0])
print "Second hair color is: {}".format(hairs[1])
print "Third hair color is : {}".format(hairs[2])

# In general, for a list of n elements,
# the position/index of the last element is n-1
# Example:
# For a list of 5 elements (n=5),
# the position/index of the last element is 4 (5-1).

# Common operations on a list:

# Operation # 1
# Add an element to the end of a list. For that, we use the append function.
# List objects have an append function that can be used to add an element to the end of a list.
# Example:
# Create a list of fruits:
fruits = ['Peach', 'Banana', 'Mango']
print fruits # Print the list
number_of_fruits = len(fruits)
print "Number of fruits: {}".format(number_of_fruits) # This should print 3
# Add a new fruit to the end of the list.
fruits.append('Pear') # Add a new element called 'Pear' to the end of the fruits list
print fruits # Print the list
number_of_fruits = len(fruits)
print  "Number of fruits: {}".format(number_of_fruits) # This should print 4

# Operation # 2
# Add an element in any position of a list (not just at the end).
# List objects also have a function called insert that can be used to add an element in any position of a list.
# the insert function takes two arguments:
#     argument #1: The index/position where we want to insert the element.
#     argument #2: The value of the element that we want to insert.
# Example:
# Create a list of foreign languages:
foreign_languages = ['English', 'Russian', 'Spanish']
print foreign_languages
# Insert a new foreign language called 'Italian' at the beginning of the list
foreign_languages.insert(0, 'Italian')
print foreign_languages # This should print ['Italian', 'English', 'Russian', 'Spanish']
# Insert a new foreign language called 'French' after 'English'.
# Notice that 'English' is at position # 1 in the list. Therefore, since we want
# to insert 'French' after English, it means that 'French' should be at position # 2
foreign_languages.insert(2, 'French')
print foreign_languages # This should print ['Italian', 'English', 'French', 'Russian', 'Spanish']

# Operation # 3
# Check if an element exists in a list.
# Example:
# Create a list of states
states = ['New York', 'New Jersey', 'Florida', 'Maine', 'California', 'Nevada', 'Utah']
# To check if a value exists in a list, we use the 'in' operator.
# in is an operator that returns True or False.
# To use the 'in' operator, put what you are looking for on the left side of 'in'
# and where you are looking for it on the right side of 'in'
vermont_in_states = 'Vermont' in states
print "Vermont is in states: {}".format(vermont_in_states)
maine_in_states = 'Maine' in states
print "Maine is in states: {}".format(maine_in_states)

# Operation # 4
# Get the position of an element in a list.
# List objects have an 'index' function which returns the index/position of an element in a list.
# If the element does not exist, then a ValueError exception is raised.
# Example:
# Create a list of car types.
cars = ['Mercedes', 'BMW', 'Audi']
# Get the position/index of 'BMW'
bmw_index = cars.index('BMW')
print "BMW is at position # {}".format(bmw_index) # Should be at position # 1

# Operation # 5
# Delete an element from a list.
# There are two ways of deleting an element from a list.
# If we know the index/position of the element, then we can use the 'del' function.
# If we want to delete based on just the value of the element, then we can use the list objects's
# remove function.
# Example:
# Create a list of TV Shows.
tv_shows = ['Friends', 'Fringe', 'Sex and the City', 'Big Bang Theory', 'Game of Thrones']
print tv_shows
# Delete the 3rd element from the list (the 3rd element is at position 2).
del tv_shows[2] # This should delete 'Sex and the City' from the list
print tv_shows # This should print ['Friends', 'Fringe', 'Big Bang Theory', 'Game of Thrones']
# Delete 'Fringe' from the list
tv_shows.remove('Fringe')
print tv_shows # This should now print ['Friends', 'Big Bang Theory', 'Game of Thrones']

# Operation # 6:
# Order a list.
# List objects have a 'sort' function that can be used to sort/order the list.
# Example:
# Create a list of animals
pets = ['Snake', 'Bunny', 'Crocko', 'Cat', 'Dog', 'Pig']
print pets
# Sort the list alphabetically
pets.sort()
print pets # This should print ['Bunny', 'Cat', 'Crocko', 'Dog', 'Pig', 'Snake']

# Operation # 7:
# Reverse the order of elements in a list.
# Create a list of sports
sports = ['Baseball', 'Football', 'Basketball', 'Soccer', 'Tennis']
print sports
sports.reverse()
print sports # Should print ['Tennis', 'Soccer', 'Basketball', 'Football', 'Baseball']