# TUPLE
"""
A tuple is a collection of similar elements just like a list.
The primary difference between a tuple and a list is that a tuple
cannot be modified once it is created.

So we say that a tuple is an ordered, immutable data structure.
By being ordered, it means you can index into a tuple.
By being immutable it means you cannot directly modify an item of
a tuple after it has been created.

You can create a tuple by using () or a the constructor tuple().
"""
# A tuple of numbers
numbers = (1, 5, 8)
print(type(numbers))

# An empty tuple
ages = ()

# Using the constructor
fruits = tuple()

# CLASSWORK
"""
Create a tuple of 5 fruits using a tuple constructor.
"""
fruits = tuple(["orange", "kiwi", "strawberry", "mango", "pawpaw"])
print(fruits)

# Can you create a tuple of 3 names not using the constructor
names = ("goody", "ima", "azure")
print(names)

# TUPLE CHARACTERISTICS
""""
1. Ordered: Tuples maintain the order of elements
2. Immutable: Tuples cannot be modified or changed after it has been created
3. Allow duplicates: They can contain duplicate values
"""
# ORDERED
"""
Because tuples are ordered we can index into the tuple.
"""
names[0]
names[2]

# IMMUTABLE
"""
You cannot change the value of a tuple
"""
# names[1] = 'pal' # will throw an error

# ALLOW DUPLICATES
names = ("pal", "son", "pal", "lam", "pal")
print(names)

# TUPLE CAN ALLOW DIFFERENT DATA TYPES
person = ("william", 90, "male", ["reading", "cooking", "dancing"])
print(person)

# ACCESSING DATA FROM A TUPLE
# CLASSWORK
"""
Access the list of hobbies from the person tuples.
"""
print(person[3])

"""
Since a tuple is ordered, using index will help you access
the items of the tuple.
"""
# CLASSWORK
"""
Create a tuple of 6 animals and access the 2nd and 3rd item together.
"""
animals = ("goat", "sheep", "dog", "cat", "lion", "cow")
print(animals[1:3])

animals = ("dog", "cat", "snake", "skunk", "kiwi")
second_and_third = animals[1:3]
print(second_and_third)

# ITERATING OVER A TUPLE USING FOR LOOP
# CLASSWORK
"""
Create a tuple of 5 colors
and print only colors that are more than 3 letters
and have letter `e` in the name
"""
colors = ("blue", "red", "brown", "white", "yellow")
for color in colors:
    if len(color) > 3 and "e" not in color:
        print(color)