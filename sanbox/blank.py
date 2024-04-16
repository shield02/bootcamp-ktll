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


def lucky_number(name):
    name = 'keme'
    number = len(name) * 7
    print(f'Hello {name}. Your lucky number is {number}')


name = 'Keme'
lucky_number(name)


def month_days(name_month, number_days):
    name_month = 'June'
    number_days = '30'
    print(f'{name_month} has {number_days} days')


name_month = 'June'
number_days = '30'
month_days(name_month, number_days)


def print_full_name():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print(last,  first)


print_full_name()











