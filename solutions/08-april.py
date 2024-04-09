"""
Question #1
----------------------------------------------------------------------
Research 10 methods used with list object operations and show at least
two examples of each of the methods.
"""

# List methods to add : Append, Extend, Insert

# append adds an item to the end of the list

colours = ["lilac", "red", "grey", "white"]
colours.append("black")
print(colours)

# Extend adds all items of one list in another list

languages = ["french", "spanish", "german"]
more_langauges = ["russian", "english"]
languages.extend(more_langauges)
print(languages)

# Insert, inserts an item at a specific position

objects = ["pencil", "eraser", "notebook"]
objects.insert(0, "whiteboard")
print(objects)

# List methods to remove: Clear, Pop, Remove

# Clear removes all items from the list

names = ["John", "Jacob", "Smith"]
names.clear()
print(names)

# Pop removes an item at a specified index

countries = ["Korea", "France", "Namibia", "Australia"]
countries.pop(2)
print(countries)

# Remove; here, we provide an item/value that we want to remove; not an index

items = ["umbrella", "socks", "shoes", "trousers"]
items.remove("shoes")
print(items)

# List methods: Index, Count, Sort, Reverse 

# Index finds the position of a given item in a list
# It also returns the first occurrence of the matching element

room = ["mirror", "wardrobe", "bed", "dresser", "bed"]
index = room.index("bed")
print(index)

# Count accepts a single input and outputs the number of times the input occurs 

animals = ["rabbit", "cat", "dog", "rabbit", "dog", "mouse", "rabbit"]
num_of_counts = animals.count("rabbit")
print(num_of_counts)

# Sort is used to sort the items of a list in place

list_one = ["perfume", "mist", "diffuser", "candles"]
list_one.sort()
print(list_one)

# Reverse; it reverses the element of a list in place

list_two = ["world", "earth", "universe", "atmosphere"]
list_two.reverse()
print(list_two)



"""
Question #2
----------------------------------------------------------------------
Using the list ['Alice', 'was', 'not', 'a', 'bit', 'hurt'], construct the
following lists:
(a) ['not', 'a', 'bit', 'hurt']
(b) ['Alice', 'was', 'hurt']
(c) ['Alice', 'hurt', 'a', 'bit']
(d) ['a', 'bit', 'hurt', 'Alice', 'not']
"""

sentence = ["Alice", 'was', 'not', 'a', 'bit', 'hurt']
sentence_one = [2, 3, 4, 5]
sentence = [sentence[x] for x in sentence_one]
print(sentence)


sentence = ["Alice", 'was', 'not', 'a', 'bit', 'hurt']
sentence_two = [0, 1, 5]
sentence = [sentence[x] for x in sentence_two]
print(sentence)

sentence = ["Alice", 'was', 'not', 'a', 'bit', 'hurt']
sentence_three = [0, 5, 3, 4]
sentence = [sentence[x] for x in sentence_three]
print(sentence)

sentence = ["Alice", 'was', 'not', 'a', 'bit', 'hurt']
sentence_four = [3, 4, 5, 0, 2]
sentence = [sentence[x] for x in sentence_four]
print(sentence)



"""
Question #3
------------------------------------------------------------------------
Use only pop and append functions to turn the list ['many', 'a', 'strange', 'tale']
into ['many', 'a', 'tale']
"""

phrase = ["many", "a", "strange", "tale"]
phrase.pop(2)
print(phrase)




"""
Question #4
------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers from 1 to 100
with 100 inclusive.
"""

integers = range(1, 101)
even_numbers = [number for number in integers if number % 2 == 0]
print(even_numbers)


"""
# Question #5
-------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers raised to the
second power.
"""

integers = range(0, 101)
even_squares = [number ** 2 for number in integers if number % 2 == 0]
print(even_squares)


"""
Question #6
-------------------------------------------------------------------------
Using list comprehension, create a list of only vowel letters from the list
of all the letters A-Z.
"""
import string

alphabets = string.ascii_uppercase
vowels = ["A", "E", "I", "O", "U"]
alpha_two = [letter for letter in alphabets if letter in vowels]
print(alpha_two)
