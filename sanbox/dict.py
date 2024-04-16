# DICTIONARY
# To get the key-value pairs, use .items()
bio_data = {'name': 'Uduak', 'age': 32, 'weight': 'not_sure', 'height': 1.79}
print(bio_data)
bio_data.items()
print(bio_data.items())

data = {'nationality': 'Nigerian', 'state_of_origin': 'Akwa_Ibom, languages_spoken: 3'}
print(data)
data.items()
print(data.items())

# To access the keys in a dictionary, use .keys() or make use of a for loop
result = {'subjects_passed': 3, 'subjects_failed': 10, 'sociable': False, 'fluent_in_speaking': True}
print(result)
result.keys()
print(result.keys())

# Using a for loop
result = {'subjects_passed': 3, 'subjects_failed': 10, 'sociable': False, 'fluent_in_speaking': True}
print(result)
for k in result:
    print(k)

# To access the values in a dictionary, use .values()
shopping = {'no_of_veggies': 10, 'healthy': True, 'pastries': False, 'clothes_worn': 'shorts'}
print(shopping)
shopping.values()
print(shopping.values())

hair_salon = dict(braids=True, nice=False, outfits_worn='casual', hairstyles_made=10)
print(hair_salon)
hair_salon.values()
print(hair_salon.values())

# To get the values of a specific key, use .get()
holiday = {'travelling': True, 'bored': False, 'meals_eaten': 'thrice_daily', 'workout': False}
print(holiday)
holiday.get('meals_eaten') 
print(holiday.get('meals_eaten'))

school_pack = {'provisions': True, 'raw_food': '', 'clothing': 'all_sorts', 'utensils': False}
print(school_pack)
school_pack.get('utensils')
print(school_pack.get('utensils'))

# To create a dictionary from a set of comma separated values, use {}.fromkeys()
{}.fromkeys(['vacation'],'Maldives')
print({}.fromkeys(['vacation'],'Maldives'))

{}.fromkeys(['beach_outing','most_definitely'])
print({}.fromkeys(['beach_outing'],'most_definitely'))

# To remove a particular key value pair, use .pop()  # Check this later
desires = {'vacation_on_an_island': 'of_course', 'six_figure': 'cant_wait', 'have_children': 'Definitely'}
print(desires)
desires.pop('have_children')
print(desires)


# NESTED DICTIONARY
# Example 1
languages = {'french':{'practice': 'twice_daily', 'spoken': 'fluent'}, 'spanish': 'beginner', 'portuguese': False}
print(languages)
languages.keys()
print(languages.keys())


