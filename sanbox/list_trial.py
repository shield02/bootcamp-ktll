favourites = ['television', 'shoes', 34, 'hair', 12]
favourites[1:4]
print(favourites[1:4])

dishes = ['white_soup', 'ekpang_nkukwo', 'fried_rice', 'chin_chin', 'beans']
dishes[1] 
print(dishes[1])  # This prints out the second item in the list.
print(dishes[4])  # This prints out the fifth element in the list.
print(dishes[::2])  # This prints out the first, third and fifth elements in the list.
print(dishes[:])  # This prints out the whole list

# CONCATENATION OF LISTS
# Example 1
items1 = ['bags', 'shoes', 'clothes']
items2 = ['wigs', 'jewellery', 'perfumes']
items3 = ['body_cream', 'polish', 'cortex']
items = items1 + items2 + items3
print(items)

# Example 2
first_destination = ['Maldives', 'Paris', 'Johannesbourg']
second_destination = ['Australia', 'Germany', 'United_Arab_Emirates']
third_destination = ['Abuja', 'Togo', 'Benin_Republic']
total_destination = first_destination + second_destination + third_destination
print(total_destination)

# Adding to a list
favourite_colours = ['blue', 'lilac', 'peach', 'champagne_gold']
favourite_colours.append('emerald_green')
print(favourite_colours)

female_names = ['Uduak', 'Janet', 'Mary', 'Priscilla', 'Mirabel']
female_names.append('Glory')
print(female_names)

# Inserting an item at a given position
feeling = ['sad', 'happy', 'angry', 'restless', 'paranoid']
feeling.insert(3, 'excited')
print(feeling)

books_of_the_bible = ['Genesis', 'Revelations', 'Psalms', 'Colossians', 'Malachi']
books_of_the_bible.insert(0, 'Matthew')
print(books_of_the_bible)

# Modifying an element by using the index of the element
household_items = ['television', 'washing_machine', 'fridge', 'radio', 'furniture']
print(household_items)
print(household_items[1])
household_items[1] = 'couch'
print(household_items)
print(household_items[1])

devices = ['phone', 'home_theater', 'decoder', 'modem', 'mp3']
print(devices)
print(devices[3])
devices[3] = 'headset'
print(devices)
print(devices[3])

# Removing an item from the list
foot_wears = ['sneakers', 'slippers', 'sandals', 'high_heel', 'cover_shoes']
print(foot_wears)
foot_wears.remove('sneakers')
print(foot_wears)

phone_brands = ['samsung', 'itel', 'infinix', 'gionee', 'oppo', 'redmi']
print(phone_brands)
phone_brands.remove('gionee')
print(phone_brands)

# Returns the number of times an element appears in a list
social_media = ['facebook', 'instagram', 'whatsapp', 'linked_in', 'tik_tok']
print(social_media)
social_media = ['facebook', 'instagram', 'tik_tok', 'whatsapp', 'tik_tok']
print(social_media)
social_media.count('tik_tok')
print(social_media.count('tik_tok'))

# Sort the items of the list in place
domestic_animals = ['goat', 'dog', 'cat', 'cow', 'donkey', 'chicken']
print(domestic_animals)
domestic_animals.sort(key=None, reverse=False)
print(domestic_animals)

languages = ['french', 'english', 'portuguese', 'german', 'spanish']
print(languages)
languages.sort(key=None, reverse=False)
print(languages)

# Reverse the elements of a list in place
classes_of_food = ['proteins', 'carbohydrates', 'vitamins', 'fats_and_oil']
print(classes_of_food)
classes_of_food.reverse()
print(classes_of_food)

body_parts = ['head', 'shoulders', 'knees', 'toes', 'hands', 'legs']
print(body_parts)
body_parts.reverse()
print(body_parts)

# Search the lists and find elements
body_systems = ['digestive', 'reproductive', 'respiratory', 'excretory']
print(body_systems)
body_systems.index('excretory')
print(body_systems.index('excretory'))

words = ['halleluyah', 'amen', 'victory', 'power', 'glory']
print(words)
words.index('victory')
print(words.index('victory'))

# Adding multiple items to a list. 'Use .extend'
vegetables = ['carrot', 'peas', 'cabbage', 'lettuce', 'pepper']
print(vegetables)
vegetables.extend(['onion', 'egg_plant'])
print(vegetables)

health_professions = ['nursing', 'optometry', 'radiography', 'dentistry']
print(health_professions)
health_professions.extend(['pharmacy', 'micro_biology'])
print(health_professions)

# Removing an item in a specific position. 'Use .pop()'
states = ['Abia', 'Ondo', 'Lagos', 'Oyo', 'Edo', 'Imo']
print(states)
states.pop(2)
print(states)

countries = ['England', 'Iraq', 'Chad', 'Niger', 'Japan', 'Qatar']
print(countries)
countries.pop(4)
print(countries)

# To remove all items in a list. 'Use .clear()
national_defence = ['army', 'navy', 'police', 'marines', 'air_force', 'sss']
print(national_defence)
national_defence.clear()
print(national_defence)

tastes = ['sweet', 'bitter', 'spicy', 'salty', 'bland', 'sour']
print(tastes)
tastes.clear()
print(tastes)

"""
Question #2
----------------------------------------------------------------------
Using the list ['Alice', 'was', 'not', 'a', 'bit', 'hurt'], construct the
following lists:
(a) ['not', 'a', 'bit', 'hurt']
(b) ['Alice', 'was', 'hurt']
(c) ['Alice', 'hurt', 'a', 'bit']
(d) ['a', 'bit', 'hurt', 'Alice', 'not']
"""
phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [2, 3, 4, 5]
phrases = [phrases[i] for i in order]
print(phrases)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [0, 1, 5]
phrases = [phrases[i] for i in order]
print(phrases)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [0, 5, 3, 4]
phrases = [phrases[i] for i in order]
print(phrases)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [3, 4, 5, 0, 2]
phrases = [phrases[i] for i in order]
print(phrases)


"""
Question #3
------------------------------------------------------------------------
Use only pop and append functions to turn the list ['many', 'a', 'strange', 'tale']
into ['many', 'a', 'tale']
"""
words = ['many', 'a', 'strange', 'tale']
words.pop(2)
print(words)

"""
Question #4
------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers from 1 to 100
with 100 inclusive.
"""
numbers = range(1,101)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

"""
# Question #5
-------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers raised to the
second power.
"""
# Solution. 'Using even numbers from 0 to 200'
numbers = range(0,200,2)
squared_number = [num * num for num in numbers]
print(squared_number)

"""
Question #6
-------------------------------------------------------------------------
Using list comprehension, create a list of only vowel letters from the list
of all the letters A-Z.
"""

import string
alphabets = string.ascii_uppercase
print(alphabets)
vowels = ['A', 'E', 'I', 'O', 'U']
V = [alph for alph in alphabets if alph in vowels]
print(V)










