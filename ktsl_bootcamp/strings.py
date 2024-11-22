"""
# STRING
A string is simply a collection or sequence of characters
that are enclosed either in single or double quotes.

Anything that is within the quote will be considered a string.
Therefore even if you have a number within a single or double
quote, it will be considered a string.
"""
# Example
'Python'
"Hello World"
"I'm very happy about learning Python 101"
'#3000'

# So we can store strings inside a variable
names = 'Ima, Edikan, Goodness, Mayen'

color = 'red'
amount = "$3000"


# INDEXING A STRING
"""
Indexing a string has to with using numbers to locate
and retrieve corresponding letters in a string

In Python this numbers called index starts from 0
so index 0 will give you the first letter of a string
index 1 will give the second letter of a string
index 3 will give the fourth letter of a string

To index into a string, you use [] at the end of the string
and put any number inside the [] to represent the index
"""
# Examples
sentence = "I'm doing good"
sentence[0] # will give us I, because in Python index starts from 0
sentence[1] # will give '
sentence[3] # will give a space, since a space is considered as being part of the string

# Classwork
special = "&%$^#@!"
special[2] # will give $
special[5] # will give @

# When you use a number that is bigger than the length of the string
# you will get an error called indexError
# For example
# special[12] # you will get index error. because the length of the string is not up to 12

# We can use len() to check the length of a string
len(special) # will give 7

# Classwork
"""
Create a variable that holds the name of any state in Nigeria
and then find the length of the name of the state.
"""
state = 'taraba'
len(state) # will give us 6

State = "akwaibom"
len(state) # will give us 8

"""
Create a variable and store the your favourite country you wish to
visit or live in and index to get the 4th letter of the name
"""
country = 'united state of america'
country[3] # will give t

fav = "netherlands"
fav[3] # will give h

country = 'finland'
country[3] # will give l

"""
what will the following code return
abia = 'lawson'
jos = 'lawan'
kano = 'sanusi'

abia[8]
jos[1]
kano[4]
"""
abia = 'lawson'
jos = 'lawan'
kano = 'sanusi'

# abia[8] # will give IndexError
jos[1] # will give a
kano[4] # will give s

"""
Supply the correct  index value for the following.
"""
continent = "south america"
continent[8] # will give e

bone = "scapula"
bone[5] # will give us l


# ASSIGNMENTS
"""
Find the letter at the 6th, 8th, 12th, 25th index of the following
"""
ocean = "pacific ocean"
mountain = 'mount kilimangaro'
place = "national park"

"""
From the following find which index gives the letter
"""
word = 'unscrupulous' # letter l
game = 'carom billiards' # letter d
plant = 'ashwagandha' # letter n

"""
Create 3 variables of different strings and find
the length of each of the strings, then find
the letter at the 1st, 3rd, and 9th index.
"""


# Functions with string
def first_index(word):
    """It returns the letter at the first index"""
    return word[0]

result = first_index("Python")
print(result)

item = "Water"
result = first_index(item)
print(result)

def any_given_index(word, index):
    """Should return the letter at the given index"""
    return word[index]

fruit = 'mango'
result = any_given_index(fruit, 3)
print(result)

### CLASSWORK
"""
Write a function that takes a word and returns
the letter at the second index.
"""
food = "spaghetti"
def second_index(food):
    """Returns the letter with the second index"""
    return food[1]

result = second_index(food)
print(result)

"""
Write a function that takes two arguments
a word and the index and returns the letter at
the given index
"""
def word_and_index(pet, index):
    """returns the letter at first index"""
    return pet[index]
pet = 'dog'
result = word_and_index(pet, 1)
print(result)

# Getting the last letter from a string
"""
In a situation where you don't know how long 
a string is but you want to return the last
letter of the string, you can achive this in two
way.

#1 - is to use negative index and in this case you
will use -1
#2 - you can use the len() function
"""
# 1 - using negative index
sentence = "I am learning programming"
result = sentence[-1] # will give you the last letter of the string
print(result)

result = sentence[-2]
print(result)

# 2 - using the len() function
length = len(sentence)
result = sentence[length - 1]
print(result)

result = sentence[length - 2]
print(result)


