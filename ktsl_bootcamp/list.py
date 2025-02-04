# LIST
"""
A list is one of data structures in Python. You use a
list when the data you are working with can be represented
as items.

So you can think of a list as having one or more items.

To create a list you use [] or the list constructor list().
N/B that when you pass another data structure into the
list constructor, it will be converted to a list structure.
"""
# Examples of list
list_of_names = ['patrick', 'raymond', 'luke', 'kimberly', 'okon', 'ayo', 'adamu']
fruits = ['grape', 'apple', 'mango', 'pineapple']
colors = list() # will create an empty list
cities = [] # this will also create and empty list

"""
# Classwork
Create a list of 5 books you have read.
"""
tuple_keys = ('in', 'pol', 'lik')
list_keys = list(tuple_keys)
print(list_keys)

# Solution
books_read = [
    "checklist", 
    "into the uncut grass", 
    "life work", 
    "the fourth dimension", 
    "new creation realities"
    ]

books = [
    "anatomy", 
    "pharmacology", 
    "emdex", 
    "bnf", 
    "pharmacognosy"
    ]

"""
Since a list is a sequence of items we can loop over
the list and act on one item at a time.
"""
# Assignment
"""
Create a list of strings of 10 items and print only the
strings that have length more than 5 using a for loop.
"""
colors = ['orange', 'red', 'yellow', 'green', 'blue', 
          'indigo', 'violet', 'brown', 'white', 'black']
for c in colors:
    if len(c) <= 5:
        continue
    print(c)

items = ["books",
          "toys", 
          "blankets",
         "crayons", 
         "cellphones", 
         "wigs", 
         "jukeboxes", 
         "bags", 
         "shoes", 
         "pills"]

for item in items:
    if len(item) > 5:
        print(item)

"""
Using a WHILE loop with a list.

It is possible to also use a WHILE loop
with a list because the list is indexed.
i.e. the list has indices. 

The first element of a list has index = 0
and the second element has index = 1 and so on

So therefore, we say that a list is an ordered
sequence of elements or items.
"""
index = 0
while index < len(items):
    print(items[index])
    index += 1

# ONE CHARACTERISTICS OF A LIST IS THAT IT IS ORDERED
# So we can index into a list to get each of the items
# Example
print(colors[0])
print(items[5])

# You can even slice a list
# Example
print(items[2:8])
print(colors[1:9])

# Exercise
"""
Create a list of 8 items and extract only the 6th item.
Create a list of 8 items and extract from the 3rd item to the 7th item.
"""
animals = ["cat", "dog", "sheep", "pig", "goat", "turkey", "cow", "elephant", "zebra"]
print(animals[5])
print(animals[2:7])

my_fruits = ['apple', 'banana', 
             'cherry', 'dates', 'elderberry', 
             'figs', 'grapes', 'pears']
print(my_fruits[5])
print(my_fruits[2:7])

# ANOTHER CHARACTERISTICS OF LIST IS THAT
# A LIST IS MUTABLE - meaning that we can change
# or modify an item in a list
# Example
print(animals)
animals[1] = "lion"
print(animals)

print(animals)
animals[-2] = ['hen', 'fish']
print(animals)

# A list can contain more than one type of data
# So you can have a number, a string, a list, a tuple
# all inside one list
# Example:
mixed_list = ['hen', 90, 'water', 'pot', ['plate', 'fork'], ('156354', '9856352')]
print(mixed_list)

# ANOTHER CHARACTERISTICS OF A LIST IS THAT IT ALLOWS DUPLICATES
# Example
duplicates_items_list = [3, 8, 'people', 2, 'workshop', 3, 'people']
print(duplicates_items_list)

# ADDING ITEMS TO THE END OF A LIST
"""
Here we can add a single new item to the end of a list.
To be able to do that we use a list method known as append.
"""
# Example
print(my_fruits)
# We can add new item at the end of the list `my_fruits`
my_fruits.append('kiwi')
print(my_fruits)

# ADDING ITEMS TO A LIST AT A SPECIFIC INDEX
"""
We can add a new item to a list at a specified index.
To be able to do that we use a list method known as insert.
"""
print(my_fruits)
my_fruits.insert(3, 'pawpaw')
print(my_fruits)

# CLASSWORK
"""
Create a list of 5 items and add a new items at the 4th index.
Create a list of 3 items and add a new item at the end of the list.
"""
subjects = ['maths', 'english', 'geography', 'computer', 'biology']
print(subjects)
subjects.insert(4, 'chemistry')
print(subjects)
cars = ['toyota', 'mercedes', 'lexus']
print(cars)
cars.append('hunda')
print(cars)

# FINDING THE LENGTH OF A LIST
list_len = len(cars)
print(list_len)

# REMOVE AN ITEM FROM A LIST
"""
To remove an item from a list you can use the remove method.
"""
# Example
numbers = [1, 6, 3, 9, 2, 7]
print(numbers)
numbers.remove(3)
print(numbers)

# How can we remove more than one item in a list
"""
To remove more than one item in a list, we use the del statement.
Notice it is not del method but a statement.
You can also use the del statement to delete the whole list.
"""
# Example
names = ['john', 'wick', 'jason', 'yellow', 'okon', 'peter']
# delete the item at index 1
print(names)
del names[1]
print(names)

# delete items from index 2 to 4
print(names)
del names[2:5]
print(names)

# delete the entire list
del names

# Changing the items of a list
"""
We can change the item of a list by assigning new value using the =
"""
# Example
names = ['john', 'wick', 'jason', 'yellow', 'okon', 'peter']

print(names)
names[3] = "king"
print(names)

# LOOPING OVER A LIST
"""
Since a list is ordered, we can loop over the list
and work with each item of the list at a time
"""
names = ['john', 'wick', 'jason', 'yellow', 'okon', 'peter']

reversed_names = []
for name in names:
    reversed_names.append(name)
    
print(reversed_names)

# LIST COMPREHENSION

