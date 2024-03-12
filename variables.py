"""
# VARIABLES
----------------------------------------------------------------
A variable is a memory location where data can be stored.
Data could be of any data type we have discussed. 
    - integers, strings, boolean, None
    - list, tuple, set, dictionary
To assign a value (data) to a variable use "="

# RULES ON DECLEARING A VARIABLE NAME
----------------------------------------------------------------
1. Variables must start with and alphabet
2. Variable must not start with a number
3. Variable must not contain space but rather use `_` to join two words
4. Variable must not start with a capital letter
5. Variable can start with `_`
6. Variable can contain numbers or end with a number
"""

# Example of variables
name = "Uduak"
print("The value of the var name is", name)
age = 120
gender = "female"
language_learned = "I am learning python language"
child1 = "Gabrial"
_parent = "Father" # object oriented programming - class
old = True
name1 = "Itoro"
print("The value of the var name is", name1)

first_number = 50
next_number = 28
result = first_number + next_number
print(result)

# We can check the type of value stored in a variable
print(type(name)) # this will check the data type of the value stored in the variable called name
print(type(next_number)) # this will check the data type of the value stored in the variable called next_number
print(type(old)) # this will check the data type of the value stored in the variable called old

print() # the () is there because it is a function
type() # the () is there because it is a function
name # there is no () because it is just a variable
