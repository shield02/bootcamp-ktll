"""
First, a set is a data structure in Python.
A set is a collection of unique data.
Meaning that a set cannot have duplicate values.
A set can have any number of items and they may be
of diffrent data types.

A set is unordered.

A set itself is mutable but it cannot contain mutable
elements like lists, sets, dictionary.

To create a set, we place any number of elements in a {},
separated by commas.
You can also create a set with the constructor.

This is important because, you cannot create and empty set
using {} because that will give you an empty dictionary instead
of an empty set.

So to get an empty set, you have to use the set constructor.

Key features of a set:
1. Unordered
2. Mutable
3. Has unique elements
"""
# Example of empty set
user_ids = set()
book_ids = set()

# Set with some elements
session_ids = {1, 3, 8, 9}
workers = {"akpan", "udo", "papa", 'okon'}

# Set of mixed elements
person = {'John', 90, 4500.00}

numbers = {1,2,3,1,5,8,3}
print(numbers)

# CLASSWORK
"""
Create a set of 5 numbers.
"""
num ={2, 4, 6, 8, 10}

# SET OPERATIONS
# Adding and Updating a set
"""
We can use .add() to add an item to a set.
"""
num.add(12)
print(num)

# CLASSWORK
"""
Create an empty set of colors and add 3 colors to it
"""
colors = {} # this will give you an empty dictionary not an empty set
print(type(colors))
# colors.add('blue', 'black', 'green')
# print (colors)

colors = set()
print(type(colors))
colors.add('red')
colors.add('green')
colors.add('black')
print(colors)

"""
So if you have more than one item and want to added it to
a set, you will use .update() to update the set.
You can store the items you want to add to the set in any
of list, tuple or set data structure and pass it to update().
"""
books = {"yellow sun"}
print(books)
more_books = ['business pro', 'purple times', 'night owl']
# We can update the books
books.update(more_books)
print(books)
