"""
Question #1
-------------------------------------------------------------------
Research 10 methods used with dictionary in python and show at least
two examples of each of the methods.
"""

# Dictionary methods
# 1 .clear() removes all the elements from the dictionary
bio_data = {'name': 'Udy', 'age': 50, 'height': 1.79, 'tall': True, 'weight': 'unknown'}
print(bio_data)
bio_data.clear()
print(bio_data)

family = {'name': 'Eti_mfons', 'parents': 2, 'children': 5, 'residence': 'Calabar', 'religion': 'Christianity'}
print(family)
family.clear()
print(family)

# 2 .fromkeys() returns a dictionary with the specified keys and values
favorites = {}.fromkeys(['drink'], 'sprite')
print(favorites)

likes = {}.fromkeys(['food'], 'beans')
print(likes)

# 3 .get() returns the value of the specified key
fav_meal = {'name': 'yam', 'mode': 'frying', 'substitute': 'potato'}
fav_meal.get('substitute')
print(fav_meal.get('substitute'))

course = {'title': 'Econs', 'difficult': False, 'lecturer': 'Nyong', 'grade': 'B'}
course.get('difficult')
print(course.get('difficult'))

# 4 .items() returns a list containing a tuple for each key value pair
flower = {'type': 'hibiscus', 'colour': 'red', 'fragrance': 'mild', 'edible': True}
flower.items()
print(flower.items())

numbers = {'a': 12, 'b': 20, 'c': 25, 'd': 36}
numbers.items()
print(numbers.items())

# 5 .keys() returns a list containing the dictionary's keys
fav_meal = {'name': 'yam', 'mode': 'frying', 'substitute': 'potato'}
fav_meal.keys()
print(fav_meal.keys())

course = {'title': 'Econs', 'difficult': False, 'lecturer': 'Nyong', 'grade': 'B'}
course.keys()
print(course.keys())

# 6 .values() returns a list of all the values in the dictionary
bio_data = {'name': 'Udy', 'age': 50, 'height': 1.79, 'tall': True, 'weight': 'unknown'}
bio_data.values()
print(bio_data.values())

family = {'name': 'Eti_mfons', 'parents': 2, 'children': 5, 'residence': 'Calabar', 'religion': 'Christianity'}
family.values()
print(family.values())

# 7 .pop() removes the element with the specified key 
student = {'school':'OUSS', 'class': 'SS1', 'field': 'Arts', 'age': 14, 'smart': False}
print(student)
student.pop('age')
print(student)

state = {'name': 'Imo', 'zone': 'SE', 'number': 15, 'language': 'igbo', 'tribalistic': True}
print(state)
state.pop('number')
print(state)

# 8 .popitem() removes the last inserted key value pair
student = {'school':'OUSS', 'class': 'SS1', 'field': 'Arts', 'age': 14, 'smart': False}
print(student)
student.popitem()
print(student)

state = {'name': 'Imo', 'zone': 'SE', 'number': 15, 'language': 'igbo', 'tribalistic': True}
print(state)
state.popitem()
print(state)

# 9 .update() updates the dictionary with the specified key value pair
digits ={1: 'abc', 2: 'bcd', 3: 'cde', 4: 'def', 5: 'efg'}
print(digits)
digits.update({6: 'fgh'})
print(digits)

bio_data = {'name': 'Udy', 'age': 50, 'height': 1.79, 'tall': True, 'weight': 'unknown'}
print(bio_data)
bio_data.update({'dislike': 'stupidity'})
print(bio_data)

# 10 .copy() returns a copy of the dictionary
numbers = {'a': 12, 'b': 20, 'c': 25, 'd': 36}
print(numbers)
nums = numbers.copy()
print(nums)

digits ={1: 'abc', 2: 'bcd', 3: 'cde', 4: 'def', 5: 'efg'}
print(digits)
digs = digits.copy()
print(digs)

"""
Qusetion #2
-------------------------------------------------------------------
Given a dictionary `file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}`
add a new key `csv` with a value 13 to the dictionary without using any
of the dictionary methods and print the new dictionary.
"""

# Solution
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts['csv'] = 13
print(file_counts)

"""
Question #3
-------------------------------------------------------------------
Given a dictionary `file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}`
iterate over the dictionary and print the keys of the dictionary.

N/B: you may use any of the dictionary methods to achieve this.
"""

# Solution
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(key)

"""
Question #4
-------------------------------------------------------------------
Given a dictionary `file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}`
iterate over the dictionary and print the values of the dictionary.

N/B: you may use any of the dictionary methods to achieve this.
"""

# Solution
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(file_counts[key])

"""
Question #5
-------------------------------------------------------------------
Given a dictionary `file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}`
iterate over the dictionary and print both the keys and the values of 
the dictionary.

N/B: you may use any of the dictionary methods to achieve this.
"""

# Solution
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(key, file_counts[key])

"""
Question #6
-------------------------------------------------------------------
Create a dictionary of at least 5 grocery items and their respective
prices as float data type.
Write a function that returns the total price of all the grocery
items in a dictionary. The function will take a dictionary as argument.
Use the dictionary you created above to run the function.
"""
# Solution
grocery = {'bread': 1000.55, 'chicken': 3566.95, 'eggs': 799.50, 'cereal': 433.42, 'pasta': 233.66}


def total_price(groceri):  # function that returns the total price of all grocery items
    total = 0
    for k in groceri:
        total += groceri[k]
    return total


groceri = grocery 
print(total_price(groceri))

"""
Question #7
--------------------------------------------------------------------
Write a function that receives a dictionary which contains email domain
names as keys and a list of users as values and returns a list that contains
complete email address of all the users.
You can use this dictionary:
domain_users = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
                "yahoo.com": ["barbara.gordon", "jean.grey"], 
                "hotmail.com": ["bruce.wayne"]}
Example: your function should return a list with `clark.kent@gmail.com` as one
of the elements.
"""


# Solution
def complete_email_addresses(domain_users):
    email_addresses = []
    for domain, users in domain_users.items():
        for user in users:
            email_addresses.append(f'{user}@{domain}')
    return email_addresses
    
             
domain_users = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
                "yahoo.com": ["barbara.gordon", "jean.grey"], 
                "hotmail.com": ["bruce.wayne"]}        

print(complete_email_addresses(domain_users))

"""
Question #8
---------------------------------------------------------------------
Write a function that takes any string and returns a dictionary where
the keys are each letter present in a string and the values are how many
times each letter is present in the string.

Example: if the string `pyyyytthoonnn` is given to the function it will return
{'p': 1, 'y': 4, 't': 2, 'h': 1, 'o': 2, 'n': 3}
"""


# Solution
def count_letters(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


print(count_letters('pyyyytthoonnn'))
