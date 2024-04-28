"""
# Question #1
-----------------------------------------------------------------
Write a function that asks a user for his first name and then his 
last name and print last name before first name.
------------------------------------------------------------------
"""


def full_name(first_name, last_name):  
    def full_name(): 
    first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
    print(last_name, first_name)


first_name = "itoro"
last_name = "eti-mfon"
full_name(first_name, last_name)




"""
Question #2
-----------------------------------------------------------------
# A function with no return value
-----------------------------------------------------------------
A function that does not return any value.
This function will return None - A special data type in Python 
used to indicate that things are empty or that they returned 
nothing.

# Write a function that takes your name and PRINTS "Welcome John". 
If your name is "John" for example.
-------------------------------------------------------------------
"""

def greet(name):
    print("Welcome", name)

greet("Itoro")


#I have not finished this, and will probably get back to it later. Ignore for now