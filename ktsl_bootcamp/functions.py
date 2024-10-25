"""
FUNCTION
A function is a group of Python code that is written to
perform specific task.

To create or define a function you use the `def` key word, 
followed by the function name and argument(s) is any.

For example, you can write a function that will always multipy
a number by itself and returns the result.

A function may take argument(s). Argument(s) may be 1 or more
for a particular function.

Argument can be positional or key-word arguments and are placed inside 
`()`.
Positional arguments are considered based on the position it was specified
when the function was created.
Key-word arguments are specified as follows argument=value, and do
not need to follow the position it was specified when the function was created.

You must follow these rules in naming a function.
1. use only a-z or A-Z or 0-9
2. must not contain spaces but can use `_` in place of a spcae
3. don't start a name with a number but you can include a number
in other places of the function name
4. function names must be self descriptive
5. don't use python reserved words as your function name
6 don't start a name with captital letter. It is recommended that you
use only small letters for the name
"""
# this function takes no argument
def say_hello():
    print("hello")

# this is how to define a function
def multiply_by_self(number): # parameter(s)
    result = number * number
    return result

# Scope
fruit = "orange" # fruit is defined in the global scope
def cheer_my_fruit_3_times(number):
    cheered_times = fruit * number # cheered_times is scoped inside the function
    return cheered_times

cheers = cheer_my_fruit_3_times(3)
print(cheers)

# print(cheered_times)

# after creating a function you will call the function and provide any number
# of argument(s) that it was defined with

# this is how you call or use the function
result = multiply_by_self(90) # global variable
print(result)

# Write a function that will take your first name and multipy
# it ny 3.
def multipy_name_by_3(firstname):
    res = firstname * 3
    return res

result = multipy_name_by_3("ima") # argument(s)
print(result)

# Classwork
"""
Write a function that takes no argument
and prints your favourite meal.
"""
# Edikan's Solution
def favorite_meal():
    print(favorite_meal)

favorite_meal()

# Ima-Abasi's Solution
def favourite_meal(fufu):
    result = favourite_meal
    return result

print(favourite_meal("fufu"))

# Correction
def fav_meal():
    print("fufu")
fav_meal()

"""
Write a function that takes 1 argument
that will be a number. The function
will return the remainder when the argument
is divided by 3.
"""
def my_dogs_age(age):
    dog_age = age % 3
    return dog_age

res = my_dogs_age(9)
print(res)

res = my_dogs_age(14)
print(res)

res = my_dogs_age(55)
print(res)

"""
Write a function that takes one argument
that will be a text and returns the number
of letters in the text.
"""
def my_maiden_name(name):
    my_maiden_name = len(name)
    return my_maiden_name

res = (len("ekong"))
print(res)

def number_of_letters(text):
    return len(text)

print(number_of_letters("Friday is a good day"))
