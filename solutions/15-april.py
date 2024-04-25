"""
# Question #1
-----------------------------------------------------------------
Write a function that asks a user for his first name and then his 
last name and print last name before first name.
------------------------------------------------------------------
"""

# ANSWER1


def print_first_name(first_name):
    print(first_name)


def print_last_name(last_name):
    print(last_name)


my_first_name = input("what is your first name?")
my_last_name = input("what is your last name?")
print_last_name(my_last_name)
print_first_name(my_first_name)


"""
Question #2
-----------------------------------------------------------------
# A function with no return value
-----------------------------------------------------------------
A function that does not return any value.
This function will return None - A special data type in Python 
used to indicate that things are empty or that they returned 
nothing.

# Wirte a function that takes your name and PRINTS "Welcome John". 
If your name is "John" for example.
-------------------------------------------------------------------
"""


# ANSWER 2
def say_welcome(name):
    print("welcome", name)


name = input("what is your name?")
print("welcome", name)



"""
Question #3
------------------------------------------------------------------
The principle of code reuse achived with functions. Functions helps
in reducing code repeatation.
------------------------------------------------------------------
# Convert the following code into a function called `lucky_number`.
# The function will take only one argument, `name`.
name = "Keme"
number = len(name) * 7
print("Hello " + name + ". Your lucky number is " + str(number))
"""

"""
Question #4
------------------------------------------------------------------
Identify the repeated pattern in the code below and replace it with
a function called month_days, that receives the name of the month 
and the number of days in that month as arguments.
june_days = 30
print("June has " + str(june_days) + " days.")
"""
