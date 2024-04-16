"""
# Question #1
-----------------------------------------------------------------
Write a function that asks a user for his first name and then his 
last name and print last name before first name.
------------------------------------------------------------------
"""


# Solution 1
def print_full_name(first_name, last_name):
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print(last,  first)


my_first_name = 'Uduak'
my_last_name = 'Eti-mfon'
print_full_name(my_first_name,  my_last_name)


# Another example
def print_fuul_name(first_name, last_name):
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print(last,  first)


my_first_name = 'Gods-will'
my_last_name = 'Grace'
print_fuul_name(my_first_name, my_last_name)


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


# Solution 2
def print_name(name):
    print('Welcome', name)


my_name = 'Uduak'
print_name(my_name)


def print_nom(nom):
    print('Welcome', nom)


my_nom = 'Gods-will'
print_nom(my_nom)


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


# Solution 3
def lucky_number(name):
    word = 'Hello'
    sentence = word + ' ' + name + ','
    phrase = 'Your lucky number is '  
    s = str(number)
    message = phrase + s
    print(sentence, message)


name = 'Keme'
number = len(name) * 7
lucky_number(name)

"""
Question #4
------------------------------------------------------------------
Identify the repeated pattern in the code below and replace it with
a function called month_days, that receives the name of the month 
and the number of days in that month as arguments.
june_days = 30
print("June has " + str(june_days) + " days.")
"""


# Solution 4
def month_days(name_month, number_days):
    print(name_month, number_days)


the_name_month = 'June has'
the_number_days = '30 days'
month_days(the_name_month, the_number_days)
