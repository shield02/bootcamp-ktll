"""
# Question #1
------------------------------------------------------------------
Research 10 methods used with tuples in python and show at least
two examples of each of the methods.
"""

# Solution
# Solution
# 1. count() returns the number of occurences of a specified element 
proteins = ('beef', 'eggs', 'beef', 'milk', 'beef', 'eggs', 'beans')
proteins.count('beef')
print(proteins.count('beef'))

milk_brands = ('peak', 'cow_bell', 'peak', 'dano', 'loya', 'dano', 'peak')
milk_brands.count('dano')
print(milk_brands.count('dano'))

# 2. index() returns the index of the first occurence of the specified element
school = ('teachers', 'students', 'cleaners', 'security', 'counsellors')
school.index('security')
print(school.index('security'))

stationery = ('books', 'pens', 'rulers', 'ink', 'folders', 'envelope')
stationery.index('folders')
print(stationery.index('folders'))

# 3. len() to find the length of a tuple
female_names = ('Uduak', 'Janet', 'Mary', 'Priscilla', 'Mirabel')
len(female_names)
print(len(female_names))

feeling = ('sad', 'happy', 'angry', 'restless', 'paranoid', 'excited')
len(feeling)
print(len(feeling))

# 4. sorted() returns a new tuple with the elements arranged in ascending order
favourite_colours = ('blue', 'lilac', 'peach', 'champagne_gold')
sorted(favourite_colours)
print(sorted(favourite_colours))

books_of_the_bible = ('Genesis', 'Revelations', 'Psalms', 'Colossians', 'Malachi')
sorted(books_of_the_bible)
print(sorted(books_of_the_bible))

# 5. min() returns the smallest element in a tuple
foot_wears = ('sneakers', 'slippers', 'sandals', 'high_heel', 'cover_shoes')
min(foot_wears)
print(min(foot_wears))

phone_brands = ('samsung', 'itel', 'infinix', 'gionee', 'oppo', 'redmi')
min(phone_brands)
print(min(phone_brands))

# 6. max() returns the largest element in a tuple
social_media = ('facebook', 'instagram', 'whatsapp', 'linked_in', 'tik_tok')
max(social_media)
print(max(social_media))

mens_outfit = ('trouser', 'shirt', 'shorts', 'tie', 'polo')
max(mens_outfit)
print(max(mens_outfit))

# 7. tuple() converts an iterable object into a tuple
domestic_animals = ['goat', 'dog', 'cat', 'cow', 'donkey', 'chicken']
tuple(domestic_animals)
print(tuple(domestic_animals))

languages = ['french', 'english', 'portuguese', 'german', 'spanish']
tuple(languages)
print(tuple(languages))

# 8. tuple() to create an empty tuple 
empty = tuple()
print(empty)

nada = tuple()
print(nada)

# 9. sum() adds up the values in a tuple and gives the result
nums = (9, 13, 22, 30, 45)
sum(nums)
print(sum(nums))

numbers = (2, 4, 8, 12, 16, 32)
sum(numbers)
print(sum(numbers))

# 10. any() accepts iterable as an argument and returns true if any of the element in the iterable is true.
clothes = {'dress', 'skirts', 'shirts', 'trousers'}
print(clothes)
any(clothes)  # returns true if any element in clothes is true
print(any(clothes))

variety = {0, False, 0}
print(variety)
any(variety)  # returns false if no element in variety is true
print(any(variety))

"""
# Question #2
------------------------------------------------------------------
Research 10 methods used with sets in python show at least
two examples of each of the methods.
"""

# Solution
# 1. add() to add an element to the set
tastes = {'sweet', 'bitter', 'spicy', 'salty', 'bland', 'sour'}
print(tastes)
tastes.add('peppery')
print(tastes)

national_defence = {'army', 'navy', 'police', 'marines', 'air_force', 'sss'}
print(national_defence)
national_defence.add('interpol')
print(national_defence)

# 2. clear() removes all elements from the set
countries = {'England', 'Iraq', 'Chad', 'Niger', 'Japan', 'Qatar'}
print(countries)
countries.clear()
print(countries)

states = {'Abia', 'Ondo', 'Lagos', 'Oyo', 'Edo', 'Imo'}
print(states)
states.clear()
print(states)

# 3. pop() removes an element from the set
vegetables = {'carrot', 'peas', 'cabbage', 'lettuce', 'pepper'}
print(vegetables)
vegetables.pop()
print(vegetables)

health_professions = {'nursing', 'optometry', 'radiography', 'dentistry'}
print(health_professions)
health_professions.pop()
print(health_professions)

# 4. remove() removes a specified element from the set
vegetables = {'carrot', 'peas', 'cabbage', 'lettuce', 'pepper'}
print(vegetables)
vegetables.remove('cabbage')
print(vegetables)

health_professions = {'nursing', 'optometry', 'radiography', 'dentistry'}
print(health_professions)
health_professions.remove('optometry')
print(health_professions)

# 5. difference() returns a set containing the difference between two or more sets
breakfast = {'egg', 'milk', 'bread', 'butter', 'tomato', 'sardine', 'beans'}
brunch = {'yam', 'stew', 'beans', 'egg', 'tomato', 'butter', 'yoghurt'}
diff = breakfast.difference(brunch)
print(diff)

subjects = {'maths', 'english', 'yoruba', 'basic_tech', 'civic', 'counselling'}
courses = {'economics', 'statistics', 'maths', 'research', 'english', 'civic'}
diff = subjects.difference(courses)
print(diff)

# 6. intersection() returns a set that contains the items that exist in both sets.
subjects = {'maths', 'english', 'yoruba', 'basic_tech', 'civic', 'counselling'}
courses = {'economics', 'statistics', 'maths', 'research', 'english', 'civic'}
inter = subjects.intersection(courses)
print(inter)

breakfast = {'egg', 'milk', 'bread', 'butter', 'tomato', 'sardine', 'beans'}
brunch = {'yam', 'stew', 'beans', 'egg', 'tomato', 'butter', 'yoghurt'}
inter = breakfast.intersection(brunch)
print(inter)

# 7. isdisjoint() returns whether two items have an intersection or not
favourites = {'braids', 'sneakers', 'wigs', 'bags', 'cover_shoes', 'novels'}
buy_list = {'food_items', 'beverage', 'fabric', 'purse', 'mop'}
fb = favourites.isdisjoint(buy_list)  # Returns true if no element in favourites is present in buy_list
print(fb)

states = {'Edo', 'Bauchi', 'Kano', 'Oyo', 'Imo', 'Fct', 'Kogi'}
eastern_states = {'Abia', 'Enugu', 'Imo', 'Anambra', 'Ebonyi'}
is_in = states.isdisjoint(eastern_states)  # Returns false if an element in states is in eastern_states
print(is_in)

# 8. union() returns a set that contains all items from both sets excluding duplicates
multiples_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24}
multiples_3 = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36}
uni = multiples_2.union(multiples_3)
print(uni)

tubers = {'yam', 'coco_yam', 'water_yam', 'cassava', 'potatoes'}
snacks = {'meat_pie', 'cookies', 'chips', 'juice', 'ice_cream'}
uni = tubers.union(snacks)
print(uni)

# 9. issubset() returns whether another set contains this set or not
x = {1, 5, 9, 13}
y = {1, 10, 5, 13, 9, 4}
z = x.issubset(y)  # Returns true if all items in set x are present in set y
print(z)

a = {'u', 'v', 'w', 'x', 'y'}
b = {'z', 'q', 'w', 't', 'u'}
c = a.issubset(b)  # Returns false if all items in set a are not present in set b
print(c)

# 10. issuperset() returns whether this set contains another set or not
x = {1, 2, 3, 4, 5, 6}
y = {2, 4, 6}
z = x.issuperset(y)  # returns true if all items in set y are present in x
print(z)

a = {'w', 'a', 'd', 'e', 'z', 'x'}
b = {'z', 'y', 'e', 'd'}
c = a.issuperset(b)  # returns false if all items in set b are not present in set a
print(c)

"""
# Question #3
------------------------------------------------------------------
Write a function that takes a list of numbers and returns only the
uniques numbers in the list.
"""


# Solution
def take_list(numbers):
    return set(numbers)


numbers = [2, 4, 6, 8, 2, 3, 4, 2, 4, 6, 8, 3, 10, 8, 2]
print(take_list(numbers))


def take_lst(numbers):
    return set(numbers)


numbers = [10, 25, 30, 45, 25, 30, 55, 45, 10, 25, 45, 30, 55]
print(take_lst(numbers))

"""
# Question #4
------------------------------------------------------------------
Return the value 20 from the tuple below:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

N/B: you do not need to write a function for this question
"""

# Solution
tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
tuple1[1]  # This accesses the second element in the tuple which is the list
tuple1[1][1]  #This accesses the second element in the list inside the tuple
print(tuple1[1][1])

"""
# Question #5
------------------------------------------------------------------
Unpacking of values in a tuple.
If a tuple has 4 values, it can be unpacked by declearing four
variables and assigning the tuple to it.

Unpack the values of the tuple into 4 variables and print them out.
tuple2 = (3, 10, 45, 78)
"""

# Solution
tuple2 = (3, 10, 45, 78)
(a, b, c, d) = tuple2
print(a)
print(b)
print(c)
print(d)

"""
# Question #6
------------------------------------------------------------------
Create a tuple that has 4 tuples in it. Each of the tuples in the
main tuple will have a name and age as it's items.
"""

# Solution
bio_data = (('Uduak', 50), ('Edikan', 5), ('Emediong', 23), ('Itoro', 40))
print(bio_data)

"""
# Question #7
------------------------------------------------------------------
Write a function that takes two sets and returns a new set of identical
elements from the two sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Your function will return {30, 40, 50}
N/B: a set is unordered and immutable so your order might be different.
"""

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def take_sets():
    global set1
    global set2
    identical_set = set()
    for num in set1:
        if num in set2:
            identical_set.add(num)
    return identical_set
    

print(take_sets())

"""
# Question #8
------------------------------------------------------------------
Write a function called `calculation` that takes any number integers
values as positional arguments and returns a tuple of the addition
of the values and subtraction of the values.
If only one value is given return a tuple of just that value.
"""


# Solution
def calculation(*args):
    if len(args) == 1:  # Check if only one value is given
        return (args[0])  # If only one value, return a tuple of just that value
    
    addition = sum(args)  # Calculate the sum of all values
    subtraction = args[0] - sum(args[1:])  # Calculate the subtraction of all values except the first one
    return (addition, subtraction)


print(calculation(10, 5, 3))
print(calculation(10))