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


def greet_me():
    name = "Yellow"
    age = 90
    state_of_origin = 'mars'

    return f"Hello {name}, you are {age} years old. You come from {state_of_origin}. Welcome here." 

print(greet_me())

def greet_specific_me(name, age, state):
    return f"Hello {name}, you are {age} years old. You come from {state}. Welcome here." 

print(greet_specific_me("Purple", 48, "Abia"))
print(greet_specific_me("Green", 180, "Jupiter"))
print(greet_specific_me("White", 10, "Womb"))

# Classwork
"""
Write a function that does not take any argument
the function will have a variable `age` and will
return `age` to the power of 2

tips: you use ** to raise a number to any power
in python.
"""
# age = int(input("What is your number: "))
def age():
    return age
print(age())

def age_square():
    age = 45
    return age**2

print(age_square())

"""
Write a function that takes two argument which 
will be any number of your choice and your
favourite color. then returns the color
multiplied by the number.
"""
def multiply_text(num, color):
    return num * color

print(multiply_text(3, "purple"))

"""
Write a function that takes 2 arguments, both of 
them numbers and multiply the one of the arguments
by 2 and then add the second argument to the result
of the first one.
"""
def numbers(val1, val2):
    result = val1 * 2
    return result + val2

print(numbers(8, 30))

"""
Write a function that takes 3 arguments, all of them
strings and return the addition of the length of the 
3 strings.
"""
def total_string(str1, str2, str3):
    return len(str1) + len(str2) + len(str3)
result = total_string("str1", "str2", "str3")
print(result)

def rules(a, b, c):
    return len(a) + len(b) + len(c)

print(rules("stand", "sit", "kneel"))


### ASSIGNMENT ON FUNCTIONS
"""
1. Write a function that takes no argument,
the function will have a variable that store
the name of any country and returns a sentence
with the name of the country.
"""
def name_of_country():
    nation = "Nigeria"
    return f"You are from {nation}"
print(name_of_country())

"""
2. Write a function that takes 2 arguments both of them
numbers and multiplies each of the number by 2 then add
both of them and return the answer.
"""
def add_two_nums(num1, num2):
    r1 = num1*2
    r2 = num2*2
    result = r1 + r2
    return result
print(add_two_nums(5,7))

"""
3. Write a function that takes one argument which will be
a text and returns the text in capital letters
"""
def text_sol(animal):
    return animal.upper()
print(text_sol("giraffe"))

# ASSINGMENTS II - FUNCTIONS
"""
1. Write a function that takes three arguments name, age, hobby
and create 3 variables new_name, new_age, new_hobby in the
function.
new_name will be the name but starts with a capital letter
new_age will be the age raised to 5
new_hobby will be hobby in uppercase letters
Then return a sentence with the three new variables
"""

"""
2. Write a function that takes 2 arguments both of them numbers
create 3 variables inside the function.
the first new variable will take argument 1 * 6
the second new argument will take argument 2 % 2
then the third varible will take first new varible + second new variable
then return third new variable. 
"""