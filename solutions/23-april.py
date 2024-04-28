"""
# Question #1
------------------------------------------------------------------
Research 10 methods used with tuples in python and show at least
two examples of each of the methods.
"""

# ANSWER
# 1. Count()
from pickletools import pytuple


print("count")
work = ("p", "r", "o", "g", "r", "a", "m", "e", "r")
count = work.count("r")  # count the number of times r appears
print(count)

count = work.count("p")  # count number of times 'p' appears
print(count)

# 2. index ()
print("index")
work = ("p", "r", "o", "g", "r", "a", "m", "e", "r")
index_position_g = work.index("g")  # getting index position of 'g'
print(index_position_g)

index_position_o = work.index("o")
print(index_position_o)

# 3. len()
print("length")
work = ("p", "r", "o", "g", "r", "a", "m", "e", "r")
fruit = ("apple", "mango", "orange", "guava")
len_fruit = len(fruit)
print("length of fruit:", len_fruit)

len_work = len(work)
print("length of work is:", len_work)

# 4. sorted()
print("sorted......")
fruit = ("apple", "mango", "orange", "guava")
sorted_fruits = sorted(fruit)
print(sorted_fruits)

fruit = ("apple", "mango", "orange", "guava")
sorted_fruits = sorted(fruit, reverse=True)  # sorts in reverse order
print(sorted_fruits)

numbers = ("34", "7", "44", "9", "29", "2", "109")
sorted_number = sorted(numbers)
print(sorted_number)  # im a bit confused at how it sorted though

sorted_number2 = sorted(numbers, reverse=True)
print(sorted_number2)

# 5. max()
numbers = ("34", "7", "44", "9", "29", "2", "109")
max_num = max(numbers)
print(max_num)  # i dont understand why the answer is 9?

digits = (8, 9, 23, 54, 89, 785)
print(max(digits))

fruit = ("apple", "mango", "orange", "guava")
max_fruit = max(fruit)
print(max_fruit)

# 6. min()
numbers = ("34", "7", "44", "9", "29", "2", "109")
min_num = min(numbers)
print(min_num)  # i dont also understand why the output is 109?

digits = (8, 9, 23, 54, 89, 785)
print(min(digits))

fruit = ("apple", "mango", "orange", "guava")
min_fruit = min(fruit)
print(min_fruit)

# 7. sum()
digits = (8, 9, 23, 54, 89, 785)
print(sum(digits))

# 8. tuple()
print("tuple....")
subject = "psychology"
sub = tuple(subject)
print(sub)

tup = tuple()
print("output:", tup)


"""
# Question #2
------------------------------------------------------------------
Research 10 methods used with sets in python show at least
two examples of each of the methods.
"""
# ANSWER
print("SETSSSSSSSSSSSSSSSS")

# 1. add()
print("add")
fruits = {"apple", "banana", "cherry", "pineapple"}
fruits.add("orange")
print(fruits)

items = {"cloth", "shoes", "bags", "wigs"}
items.add("lipgloss")
print(items)

# 2.clear()
print("clear")
fruits = {"apple", "banana", "cherry", "pineapple"}
fruits.clear()
print(fruits)

number = {"44", "66", "77", "654"}
number.add(4)
print(number)

# 3.copy()
print("copy")
fruits = {"apple", "banana", "cherry", "pineapple"}
fruits.copy
print(fruits)

number = {"44", "66", "77", "654"}
number.copy
print(number)

# 4.difference()
print("difference")
x = {"apple", "banana", "cherry", "pineapple"}
y = {"google", "microsoft", "apple", "oraimo"}
z = x.difference(y)
print(z)

a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
my_set = a - b  # "- " can be used as a shortcut for difference
print(my_set)

a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
c = {"lion", "hippo", "zebra"}
my_set = c - b - a
print(my_set)

# 5. discard()
print("discard")
fruits = {"apple", "banana", "cherry", "pineapple"}
fruits.discard("banana")
print(fruits)

# 6. pop()
print("poppppppp")
fruits = {"apple", "banana", "cherry", "pineapple"}
fruits.pop()
print(fruits)

b = {"antelope", "dog", "snake", "pig", "goat"}
b.pop()
print(b)

# 7. union()
print("union")
a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
d = a.union(b)
print(d)

x = {"apple", "banana", "cherry", "pineapple"}
y = {"google", "microsoft", "apple", "oraimo"}
z = x | y  # "|" can be used as shortcut for union()
print(z)

# 8. update()
print("update")
x = {"apple", "banana", "cherry", "pineapple"}
y = {"google", "microsoft", "apple", "oraimo"}
x |= y
print(x)

a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
c = {"lion", "hippo", "zebra"}
a.update(b, c)
print(a)

a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
c = {"lion", "hippo", "zebra"}
a |= b | c

# 9. intersection()
print("intersection")
a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
d = a.intersection(b)
print(d)

x = {"apple", "banana", "cherry", "pineapple"}
y = {"google", "microsoft", "apple", "oraimo"}
z = x & y  # & can be used as a shortcut
print(z)

# 10. intersection_update()
print("intersection_update")
a = {"dog", "cat", "lion", "pig", "sheep"}
b = {"antelope", "dog", "snake", "pig", "goat"}
a.intersection_update(b)
print(a)

x = {"apple", "banana", "cherry", "pineapple"}
y = {"google", "microsoft", "apple", "oraimo"}
x &= y
print(x)


"""
# Question #3
------------------------------------------------------------------
Write a function that takes a list of numbers and returns only the
uniques numbers in the list.
"""


# ANSWER 3
print('unique list')


def unique_list(numbers):
    return set(numbers)


numbers = ["2", "3", "6", "7", "3", "6", "4", "2", "10"]

print(unique_list(numbers))





"""
# Question #4
------------------------------------------------------------------
Return the value 20 from the tuple below:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

N/B: you do not need to write a function for this question
"""
# ANSWER
print("4444444444")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1])


"""
# Question #5
------------------------------------------------------------------
Unpacking of values in a tuple.
If a tuple has 4 values, it can be unpacked by declearing four
variables and assigning the tuple to it.

Unpack the values of the tuple into 4 variables and print them out.
tuple2 = (3, 10, 45, 78)
"""
# ANSWER
tuple2 = (3, 10, 45, 78)
w, x, y, z = tuple2
print("w:", w, "x:", x, "y:", y, "z:", z)


"""
# Question #6
------------------------------------------------------------------
Create a tuple that has 4 tuples in it. Each of the tuples in the
main tuple will have a name and age as it's items.
"""

"""
# Question #7
------------------------------------------------------------------
Write a function that takes two sets and returns a new set of identical
elements from the two sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Your function will return {30, 40, 50}
N/B: a set is unordered and immutable so your order might be different.
"""
# ANSWER
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)


"""
# Question #8
------------------------------------------------------------------
Write a function called `calculation` that takes any number integers
values as positional arguments and returns a tuple of the addition
of the values and subtraction of the values.
If only one value is given return a tuple of just that value.
"""
