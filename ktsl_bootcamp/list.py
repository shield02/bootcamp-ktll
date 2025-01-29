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

books= [
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