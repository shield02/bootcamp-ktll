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

# CLASSWORK
"""
Write a function to modify a tuple by adding an 
element at the end of the tuple.
Hint: You will need to convert the tuple to a list first.
"""
numbers = (1, 2, 3, 4)
def modify_a_tuple(tuple_elements, new_element):
    tupl_list = list(tuple_elements)
    tupl_list.append(new_element)

    return tuple(tupl_list)

result = modify_a_tuple(numbers, 5)
print(result)

# Because a tuple is immutable, we can do just two things with
# it. Those are, count the number of times an element of a tuple 
# is in a tuple and the second method, index, finds the index of
# an element in a tuple.
# The two tuple functions are count() and index()
count_result = numbers.count(1)
print(count_result)

colors = ('red', 'blue', 'green', 'lemon', 'orange', 'white', 'black', 'brown')
element_index = colors.index('white')
print(element_index)

"""
Write a function that finds the previous element before a
particular element in a tuple.
"""
def find_prev_element_in_tuple(tup, ele):
    if tup.index(ele) < len(tup):
        index = tup.index(ele)
        return tup[index-1] # the index - 1 is the way we find the prev elem

result = find_prev_element_in_tuple(colors, 'white')
print(result)

"""
Write a function that will return the next element of a tuple
only if the element is located after the third element. If it
is not after the third elemant return the string 
"Element is not after the third element"
"""
def next_element_in_tuple(tup, ele):
    index = tup.index(ele)
    if index < 2:
        return f"Element '{ele}' is not after the third element"
    return tup[index + 1]

result = next_element_in_tuple(colors, "blue")
print(result)

result = next_element_in_tuple(colors, "black")
print(result)

"""
Write a function that returns an element of a tuple
if the element appears more than 2 times.
"""
