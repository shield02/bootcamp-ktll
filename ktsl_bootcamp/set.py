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

# CLASSWORK
"""
Create an empty set and add only even numbers 
between 1 and 1000 to it
"""
nums = set()
# Approach using add()
for num in range(1, 1000):
    if num % 2 == 0:
        nums.add(num)
print(nums)

# Another approach using update()
even_nums = [num for num in range(1, 1_000) if num % 2 == 0]
nums.update(even_nums)

# FINDING THE LENGTH OF A SET
"""
You can find the length of a set by using the len()
function
"""
set_length = len(nums)
print(set_length)

# REMOVE AN ELEMENT OF A SET
"""
To remove one element of a set, we use the discard() function
"""
programming_languages = {"Python", "Java", "PHP", "Go", "Kotlin", "Swift"}
print(f"Set before item removed: {programming_languages}")
programming_languages.discard("Go")
print(f"Set after item is removed: {programming_languages}")

# SORTING A SET
"""
A set can be sorted using the sorted() function. The function returns
a new sorted list from the elements in the set.
N/B: that it will not sort the set itself
"""
new_sorted_set = sorted(programming_languages)
print(new_sorted_set)

# CLASSWORK
"""
Write a program that will take items from a list and use
those items to create a set that is less than equal to
5 elements.

The list will have 7 string elements.
"""
list_colors = ['red', 'green', 'white', 'red', 'blue', 'white', 'brown', 'yellow', 'lemon', 'black']
set_colors = set()
index = 0
while len(set_colors) < 5:
    list_item = list_colors[index]
    set_colors.add(list_item)
    index = index + 1
    print(f"The item from list is, {list_item} and the length of the set is: {len(set_colors)}")
print(f"The full set is: {set_colors}")

# ENUMERATE
"""
The enumerate function adds a counter to an iterable and returns it
as part of the enumerate object.
Example:
list_of_colors = ['red', 'blue']
When you use enumerate with the list of colors, it will produce something
like this: (0, 'red'), (1, 'blue')
"""
enum_list_colors = enumerate(list_colors)
print(list(enum_list_colors))

enum_set1 = set()
for index, _ in enumerate(list_colors):
    item = list_colors[index]
    if len(set_colors) < 5:
        enum_set1.add(item)
    else:
        break
print(f"The full set is: {set_colors}")

enum_set2 = set()
for _, color in enumerate(list_colors):
    if len(set_colors) < 5:
        enum_set2.add(color)
    else:
        break
print(f"The full set is: {set_colors}")

# SET OPERATIONS
"""
Ptyhon provides some built-in methods that is used to perform some mathematical
set operations like Union, Intersection, Subtraction etc.

# UNION OF TWO SETS
---------------------------------------------------------------------------------
The union of two sets A and B includes all the elements of A and B.

We can use | or the union() to perform the union of two sets.
"""
# Example
a = {1, 5, 9, 2}
b = {2, 8, 7, 3}

# Performing a union of two sets using |
a_union_b = a | b
print(f"The union of two sets using |: {a_union_b}")

# Performing a union using the constructor
a_union_b_constructor = a.union(b)
print(f"The union of two sets using constructor: {a_union_b_constructor}")

# CLASSWORK
"""
Create two sets made up off strings and union the two sets using
the constructor.
"""
a = {"car", "ball", "doll"}
b = {"car", "bike", "puzzle"}

put_together = a.union(b)
print(put_together)

# INTERSECTION OF SETS
"""
The intersection of two sets includes only elements that common among
the two sets.

To perform the intersection of two sets in Python you use the & or the
intersection() constructor.
"""
a = {1, 5, 9, 2}
b = {2, 8, 7, 3}

a_intersect_b = a & b
print(f"The intersection using &: {a_intersect_b}")

# CLASSWORK
"""
Create two sets made up off strings and intersect the two sets using
the constructor.
"""
a = {"car", "ball", "doll"}
b = {"car", "bike", "puzzle"}
common_toys = a.intersection(b)
print(f"Intersected set using constructor: {common_toys}")

# CLASSWORK
"""
Write a function to create a new set that contains the identical items from two given sets.

Return the identical elements in the two given sets.
For inputs with sets {1, 2, 3, 4} and {3, 4, 5, 6}, the return value should be either {3, 4} or {4, 3}.
"""
def identical_items():
    pass

a = {1,2,3,4}
b = {3,4,5,6}

def identical_items(set_1, set_2):
    result = set_1 & set_2

    return result

print(identical_items(a,b))


# DIFFERENCE BETWEEN TWO SETS
"""
The difference between two sets A and B includes element is A that are
not present in B.

You can use - or the difference constructor to perform the set difference.
"""
a = {1,2,3,4}
b = {3,4,5,6}

set_difference = a - b
print(F"Set difference using -: {set_difference}")

set_difference_with_const = a.difference(b)
print(f"Set difference with constructor: {set_difference_with_const}")

# CLASSWORK
"""
If I have two sets and I want to get all the elements of both sets
in one new set, write a function that can always do that for me.
"""
even = {2,4,6,8,10}
odd = {1,3,5,7,9}

def first_ten(a,b):
     result = a.union(b)
     return result 

print(f"The union of two sets: {first_ten(even,odd)}")


"""
Write a function that takes two sets and returns only the items
that are in the second set passed in the argumnet that are not
in the first set.
"""
