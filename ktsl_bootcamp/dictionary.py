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
