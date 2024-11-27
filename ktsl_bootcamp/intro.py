# -- Data types --

# Numeric
# Integers
12
200
-45

# Floats
1.3
5.9

# Complex
2 + 3j

# SEQUENCE
# List
[1,2,5,"red",True]

# Tuple
(34, 67)

# Set
{2,3,7,9}


# BOOLEAN
True
False

# Text (String)
"double quotes"
'single quotes'

# MAPPING
# Dictionary
{"key": "vlaue", "key": "value"}

# Binary
bytes # immutable
bytearray # mutable


"""
Primitive Data Types
-----------------------------------------------------------------
These are data types that are always present in every computer.
They can be combined for various reasons and purpose.
They are not derived.

int, string, float, bool, None

Data type describes a data.
It is used to determine how the data is stored and processed.

Processing Data
---------------------------------------------
In processing data, we can do something like 
    - mathematical operations, 
    - cancatenation,
    - logical operations on data
    - changing from one type to another aka casting
"""
# MATHEMATICAL OPERATIONS
"""
# Addition
--------------------------------------------------------------------------
So in adding two data types will sometimes result in the same data type 
or in a different data type

For example, add an int + int = int
                    int - int = int
                    int / int = float # (special case)
                    int * int = int
                    int % int = int # this is used to get only the remainder of a division

                    Each time you work with a float, your result will always be a float
                    There is no exception for it
                    int + float = float
                    int + "string" = Error (not possible)
                    float + float = float

                    string + string = string (concatenation or join or put together or link or concat)

        You can check for equality using == because single equal sign = has been preserved for assignment
        Meaning you use = to assign a value to a variable.
        Anytime you perform comparison, you will have a boolean which either True or False.
        You can compare using ==, <, >, =<, =>

        What is a variable?
        A variable can be thought of as a container that holds something.
        You can store anything inside a variable.
        The variable will be on the left side of = while the value will be on the right side
        Example: color = "red", age = 64
        From the examples above, we have 2 variables
        First is `color` and it holds the a string value "red"
        Second is `age` and it holds an int value 64

        How can we name a variable?
        Every variable in Python must follow these rules:
        1. Must start with a letter.
        2. Must not contain any space but you can use `_` in place of a space
        3. Must not start with a number or capital letter
        4. Must not be a Python reserved word for example `float` or `class` or `def`
        5. It is generally accepted in the Python community that variable names should be small letters all through.


        
        

"""
2 + 2 # = int
2 + 3.3 # = float
3.0 + 4.5 # = float
"string" + "string" # = string

"88"

[18, 89.4, "red", True, "king"]

months = ["Jan", "Feb", "Mar", "Oct"]
for month in months:
    print(month)

fruits = ["mango", "apple", "cucumber", "orange", "banana"]
for fruit in fruits:
    print(fruit)

"""
# ASSIGNMENT FOR OCT 9
---------------------------
# INSTRUCTIONS
DO NOT WRITE ANYTHING INSIDE THIS FILE PLEASE
TAKE ALL YOUR WORK TO THE SAND BOX
THE FILE YOU WANT TO SOLVE THIS INSIDE SHOULD BE
CALLED oct_09_soln.py
--------------------------------
1. Create a variable and store your first name as the value
2. Create another variable and store your last name as the value
3. Create another variable and store your favorite number
4. What is the data type of int * int
5. What is the result and data type of "int" + "string"
"""

