""" Question #1
----------------------------------------------------------------------
Research 10 methods used with list object operations and show at least
two examples of each of the methods.
"""

# ANSWER 1
import string


my_needs = ["shoes", "clothes", "bags", "headset"]
months = ["january", "february", "march", "may"]

# method 1 : .insert() this allow you add an item to in a specific position
my_needs.insert(1, "make_up")
print(my_needs)

months.insert(3, "april")
print(months)
print("11111111111111111111111")


# method 2: .append() allows you add an item to the end of a list
my_needs.append("wigs")
print(my_needs)

months.append("june")
print(months)

print("22222222222222222222222222")

# method3: .pop() allows you remove an item from a specific position
# if you don't specify, the it removes the last item
my_needs.pop(4)  # this removes the 4th item
print(my_needs)

months.pop(3)
print(months)

print("33333333333333333333333")
# method 4: .reverse() reverses the order of your list
my_needs.reverse()
print(my_needs)

months.reverse()
print(months)

print("444444444444444444")
# method 5: .count() counts how many times an item appears in the list
shoes_count = my_needs.count("shoes")
print("number of shoes:", shoes_count)

may_count = months.count("may")
print("number of may:", may_count)

# let's add to shoes and then count
my_needs.insert(0, "shoes")
print(my_needs)
shoes_count = my_needs.count("shoes")
print("number of shoes:", shoes_count)

months.insert(0, "may")
print(months)
may_count = months.count("may")
print("number of may:", may_count)

print("5555555555555")

# method 6: .remove() removes a duplicate item
my_needs.remove("shoes")
print(my_needs)

months.remove("may")
print(months)

print("66666666666666666")

# method 7: .sort() sorts items
my_needs.sort()  # sorts in ascending order
print(my_needs)

months.sort()
print(months)

my_needs.sort(reverse=True)  # sorts in reverse order
print(my_needs)

months.sort(reverse=True)
print(months)

print("7777777777777777")
# method 8: . extend() extends your list by adding more items at once
fruits = ["mango", "paw_paw", "pineapple", "apple"]
print(fruits)
additional_fruits = ["orange", "avocado", "banana"]
print(additional_fruits)

fruits.extend(additional_fruits)
print(fruits)

names = ["paul", "innocent", "steven", "joseph"]
other_names = ["itoro", "ime", "uduak", "mfon"]
names.extend(other_names)
print(names)

print("888888888888888")

# method 9: .copy() makes a copy of the original
months = ["april", "february", "july", "may"]
copied_list = months.copy()
print(copied_list)

copied_list = names.copy()
print(names)

print("99999999")
# method 10: . clears() clears the list
months.clear()
print(months)

names.clear()
print(names)


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
# ANSWERS
list = ["Alice", "was", "not", "a", "bit", "hurt"]
del list[0:2]
print(list)

list = ["Alice", "was", "not", "a", "bit", "hurt"]
del list[2:5]
print(list)

list.pop(1)
add_list = ['a', 'bit']
list.extend(add_list)
print(list)


del list[2:4]; list.sort(reverse=True)
add_list.extend(list)
add_list.insert(4,'not')
print(add_list)


"""
Question #3
------------------------------------------------------------------------
Use only pop and append functions to turn the list ['many', 'a', 'strange', 'tale']
into ['many', 'a', 'tale']
"""
# ANSWER 3
print("answer 3")
story = ["many", "a", "strange", "tale"]
story.pop(2)
print(story)

"""
Question #4
------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers from 1 to 100
with 100 inclusive.
"""
# ANSWER 4
print("answer 4")
num = [x for x in range(1, 101) if x % 2 == 0]
print(num)
print("%%%%%%%%%%%%%%%%%%%%%%%%")

"""
# Question #5 
-------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers raised to the
second power.
"""
# ANSWER 5
num = [2**x for x in range(1, 11) if x % 2 == 0]
print(num)

print("@@@@@@@@@@@@@@@@@@@")


"""
Question #6
-------------------------------------------------------------------------
Using list comprehension, create a list of only vowel letters from the list
of all the letters A-Z.
"""
# ANSWER 6





