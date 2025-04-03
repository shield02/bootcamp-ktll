"""
A dictionary is a collection of items similar to list,
tuple. The major difference a dictionary has with lists
and tuple is that a dictionary is made up of key-value
pair.

We create a dictionary by placing a "key: value " pair
inside a {} separating each item with a comma.
We can also create a dictionary using the dict()
constructor.

 Points to take note of when creating a dictionary.
 1. Dictionary keys must be immutable such as tuples
 integers, strings etc.
 2. Dictionary keys must be unique.
"""
# Example of a dictionary
names_and_grades = {
    "john": 65,
    "peter": 79,
    "tom": 96,
}

# CLASSWORK
"""
Create a dictionary of location and their longitude, latitude
values.
"""
location_long_lat = {
    "akpanandem": [32, 16], 
    "ukanafot": [25, 74], 
    "akansoko": [21, 54]
}

location_long_lat = {
    "uyo": (12, 180), 
    "ikono": (20, 52), 
    "abak": (50, 50)
}
