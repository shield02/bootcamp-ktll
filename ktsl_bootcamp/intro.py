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
                    int + float = float
                    int + "string" = Error (not possible)
                    float + float = float
                    string + string = string
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


