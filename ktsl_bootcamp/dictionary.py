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

# CLASSWORK
"""
Create a dictionary of three countries and their capital and
print out the dictionary.
"""
country_capitals = {
    "Japan": "Tokoyo",
    "Ghana": "Accra",
    "Cameroun": "Yaunde",
}

print(country_capitals)

# ADDING AN ITEM TO A DICTIONARY
"""
To add an item to a dictionary you can provide a new key and
assign a value to the key.
"""
country_capitals["Southafrica"] = "johannesburg"
country_capitals["Japan"] = "Tokyo"
country_capitals["Nigeria"] = "Abuja"

# ACCESSING THE ITEMS OF A DICTIONARY
"""
You can access the items of a dictionary by using the index method
or by using the get() method.
"""
# Examples using the index method
"""
Using the index method has to do with writing the name of dictionary
variable with [] and providing any valid key inside the [].
"""
print(country_capitals["Cameroun"])
print(country_capitals["Nigeria"])

# Examples using the get() method
"""
Using the get method allows you provide a default value incase the key
provided doesn't exist in the dictionary.
"""
print(country_capitals.get("Japan", "We don't have this country yet in our dictionary."))
print(country_capitals.get("Brazil", "We don't have this country yet in our dictionary."))

# print(country_capitals["Niger"])

# ASSIGNMENT
"""
Create a dictionary of 5 countries and their population.

Write a function that takes a country and a dictionay as the argumnets
and if the country is in the dictionary return the corresponding population
if it is not return a default value in the format, "The country {this should be the 
name of the country that was provided as the argumnet} is not yet covered."
"""
countries = {"ghana": 550, "algeria": 200, "nigeria": 720, "mali": 130}

def africa(country, dictionary):
    return dictionary.get(country, f"The country `{country}` is not yet covered.")

result = africa("ghana", countries)
print(result)

result = africa("mali", countries)
print(result)

result = africa("cameroun", countries)
print(result)

# USING THE INDEX METHOD
"""
Using the index method you will add [] to the variable
and provide any value as the key
"""
dict_item = countries['algeria']
print(dict_item)

# REMOVING ITEM FROM A DICTIONARY
"""
We can remove an itm from a dictionary using the del statement.
"""
# Example
states_and_capitals = {
    "akwa-ibom": "uyo",
    "abia": "umahia",
    "buchi": "buchi",
    "imo": "owerri"
}

# We can delete the abia item
del states_and_capitals["abia"]
print(states_and_capitals)

# CHANGE THE VALUE OF AN ELEMENT IN A DICTIONARY
states_and_capitals["buchi"] = "buuchi"
print(states_and_capitals)

"""
# CLASSWORK
Create a dictionary for countries and their popluations.
1. Then delete on of the elements
2. Update one of the elements
"""
population = {
    "zimbabwe" : 70,
    "algeria": 100,
    "nigeria": 1000
}
del population["algeria"]
print(population)

population["zimbabwe"] = 850
print(population)

# LOOPING OVER A DICTIONARY
"""
Looping is also known as iteration.

A dictionary is an ordered collecting of items, therefore it
maintains the order of its items.

We can iterate through a dictionary keys one after the other using
a for loop.
"""
# Create a dictionary of 5 elements for staff and their salary
staff_salaries = {
    "John Ekpo": 50000,
    "Jane Asabor": 60000,
    "Bob Ntuen": 55000,
    "Alice Iyak": 70000,
    "Mike Etidot": 45000
}

# This will give you just the keys
for key in staff_salaries:
    print(key)

# We use the key to index into the dictionary and get the value
for key in staff_salaries:
    print(f"Key: {key} - Value: {staff_salaries[key]}")

# We use a dictionary method to get the key
for key in staff_salaries.keys():
    print(f"Key: {key}")

# We use a dictionary method to get the value
for value in staff_salaries.values():
    print(f"Values: {value}")

# We need both key and value at the same time
for key, value in staff_salaries.items():
    print(f"Key: {key} - Value: {value}")

# CLASSWORK
# Create a dictionary of 5 items and loop over it using the keys() and values() method
age = {
         "Greatness" : 7,
         "Gospel" : 6,
         "Gracefield" : 4,
         "Jesse" : 2,
         "Olivia" : 1,
        }

for key, value in age.items():
    print (f"Key:{key} - Value:{value}")


# CLASSWORK
"""
Create a dictionary of companies with their estimated net worth.
And loop over it to print "key - value"
"""
x = {
    "coca_cola" : 80000,
    "exxon_mobil" : 20000,
    "gopius" : 172000,
    "unilever" : 58000,
    }

for key, value in x.items():
     print (f"Key:{key} - Value:{value}")

# DICTIONARY MEMBERSHIP TEST
"""
We can check wheather a key is in the dictionary using the in and not in operators

The in operator checks wheather a key exists in a dictionary and does not check
wheather a value exist or not.
"""
print("coca_cola" in x)
print("pepsi" not in x)

# PTYHTON DICTIONARY METHODS
"""
There are common functions that are used with dictionary in Python
They include, pop, update, keys, values, items, copy etc

pop - removes the item with the specified key
copy - creates a copy of the dictionary
"""
# POP EXAMPLE
# item = x.pop("coca_cola")
# print(item)
print(x)

item = x.pop("pepsi", "facebook")
print(item)
print(x)

# COPY EXAMPLE
new_x = x.copy()

print(x)
print(new_x)

item = new_x.pop("coca_cola")
print(new_x)
print(x)
    