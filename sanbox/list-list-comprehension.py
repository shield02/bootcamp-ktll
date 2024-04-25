"""
LIST
------------------------------------
A list is a compound data structure in python
A list is that it is an ordered, mutable data structure
A list is ordered because its elements or numbers are indexed
This indexing starts from zero as usual in python
A list is said to be mutable because it can be modified or changed
This means that we can add, remove or modify elements of a list
after it has been defined
A list can be created by using []
A list can contain elements of different data types.
"""

# Example - we can create an empty list

empty_list = []  # type: ignore
# Example - we can create a list of colors
colors = ["red", "white", "blue", "brown", "black", "cyan"]
# so we can index into a list to get each element out
print(colors[0])  # will give you the first element of the list ; red
print(colors[3])  # will give you the fourth element of the list

# list of elements with different data types
heterogenous = [23, "male", "dark", "short", 6.7, False]
print(heterogenous[0])

# we can mutate a list
heterogenous[0] = 25
print(heterogenous[0])

# CLASSWORK
"""
Create a list of 5 items of your choice and print out the
second to the fourth element of the list
"""
fruits = ["apple", "banana", "mango", "orange", "pineapple"]
print(fruits[1:4])

print(type(fruits))  # this should tell you the data type of the variable
ans = fruits[1:4]

# list operations
# check the type of a variable
print(type(ans))

# check the length of a list
list_length = len(fruits)  # use the function len()
print(list_length)

print(fruits[4])

# check if a list contains certain elements using "in"
"rainbow" in fruits  # bool
if "mango" in fruits:
    print("there is a fruit called rainbow")
else:
    print("rainbow is not a fruit")

# we can remove elements of a list in a given position
print(fruits)
third_element = fruits.pop(3)  # pop removes and returns an element of a list
print(third_element)
print(fruits)

# add element to a list
fruits.append('guava')  # this will add the element at the end of the list
print(fruits)

# insert an element into a certain index
fruits.insert(1, 'pear')
print(fruits)

# loop over the elements of a list
for fruit in fruits:
    print(fruit)

eatable = []   
for fruit in fruits:
    if len(fruit) < 6:
        eatable.append(fruit)
print(eatable)

# LIST COMPREHENSION # only works with for loop
"""
A list comprehension is a construct that allows us to
create a list from a sequence or from another list.

#list comprehension syntax
[expression for value in iterable if condition]
    expression - is the value to be included in the new list that will be formed
    value is each of the elements in the iterable
    iterable is the sequence or the list itself
    if condition is optional
"""
eatable2 = [fruit for fruit in fruits]
print(eatable2)

eatable2 = [fruit for fruit in fruits if len(fruit) < 6]
print(eatable2)

# .insert, .append, .pop are called list operations

ages = [age for age in range(10)]
print(ages)

ages1 = []
for age in range(10):
    ages1.append(age)
print(ages1)


"""
# CLASSWORK
Create a list of names of 8 books. Then create another list
that only holds the books that have names shorter then 8.
"""
books = ['harry_porter','love_sounds','echoes','criminal','wasted','haunted','stress','scarred']
novel = [book for book in books if len(book) < 8]
print(novel)


