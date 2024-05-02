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






