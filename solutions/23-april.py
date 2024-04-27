"""
# Question #1
------------------------------------------------------------------
Research 10 methods used with tuples in python and show at least
two examples of each of the methods.
"""

# Count() method returns the number of times a value is in a tuple

cities = ("Abuja", "Calabar", "Abuja", "Lagos", "Calabar")
count = cities.count("Abuja")
print(count)

fruits = ("mango", "banana", "mango", "apple", "mango", "orange")
count = fruits.count("apple")
print("Number of times 'apple' appears in tuple: ", count)


# Index() returns the index at which a value is found in a tuple. 
# It finds the first occurrence of a specified element

numbers = (1, 2, 3, 4, 5, 2, 1, 2)
index = numbers.index(2)
print(index)

items = ("pen", "paper", "pencil", "phone", "pen")
print(items.index("pen"))

# len() method returns the number of elements present in a tuple

tup = (22, 33, 54, 78, 22.5)
len_tup = len(tup)
print(len_tup)

words = ("diet", "supplement", "dietary")
print(len(words))

# sorted() takes a tuple as an input and returns a sorted list as an output
# it doesn't make any changes to the original tuple

countries = ("Nigeria", "Venezuela", "Philippines", "Congo")
srt = sorted(countries)
print(srt)

numbss = (22, 3, 45, 4, 2.4)
print(sorted(numbss))

# min() gives the smallest element in the tuple as an output
alphabets = ("a", "b", "c", "x", "z")
min_alpha = min(alphabets)
print(min_alpha)

names = ("Ally", "Benard", "Charles", "Zen", "Ocean")
print(min(names))

# max() gives the largest element as an output
alphabets = ("a", "b", "c", "x", "z")
max_alpha = max(alphabets)
print(max_alpha)

names = ("Ally", "Benard", "Charles", "Zen", "Ocean")
print(max(names))

# sum() gives the sum of the elements present in the tuple as an output

elements = (22, 3, 45, 4, 2, 56, 68, 75)
sum_ele = sum(elements)
print(sum_ele)

elements2 = (4, 3, 2, 1)
print(sum(elements2))

# any() returns True if any of the elements of a given iterable are True, else it returns False
input = (True, False)
input2 = any(input)
print(input2)

inp = (False, False, 0)
print(any(inp))

# all() returns True if all the items of a given iterable are True, else it returns False
lst = (6, 7, 8, 9)
print(all(lst))

lst2 = (0, 2, 4, 6)
print(all(lst2))

# tuple() is a built-in function that can be used to create a tuple
li = [1, 2, 3]
print(tuple(li))

my_tuple = [2.3, "balls", 9, "come"]
print(tuple(my_tuple))


"""
# Question #2
------------------------------------------------------------------
Research 10 methods used with sets in python show at least
two examples of each of the methods.
"""


# add() method adds a given element to a set

cutlery = {"knife", "fork", "cup"}
cutlery.add("spoon")
print(cutlery)

# to add to an empty set

hair = set()
# adding elements
hair.add("blonde")
hair.add("brunette")

print('hair_colours:', hair)

# copy() returns a shallow copy of the set

animals = {"pig", "chameleon", "lamb"}
animals.copy()
print(animals)

colours = {"grey", "yellow", "peach", "lilac"}
print(colours.copy())

# difference() returns a set that is the difference between two sets.
# the returned set contains item that exist only in the first set and not in both

x = {"apple", "papaya", "pineapple"}
y = {"strawberry", "lemons", "papaya"}
z = x.difference(y)
print(z)

# more than 2 sets
a = {"apple", "papaya", "pineapple"}
b = {"strawberry", "lemons", "papaya"}
c = {"cherry", "pineapple", "raspberry"}
d = a.difference(b,c)
print(d)

# discard() method removes the specified item from the set

p_words = {"prelude", "prominent", "predecessor", "position"}
p_words.discard("position")
print(p_words)

b_words = {"basic", "broadcast", "belch"}
b_words.discard("belch")
print("Set after discard:", b_words)

# intersection() returns a set that contains the similarity between two or more sets

p = {"a", "b", "c"}
q = {"c", "d", "e"}
r = {"f", "g", "c"}
result = p.intersection(q, r)
print(result)

s = {2, 3, 5}
t = {1, 3, 5}
print(s.intersection(t))

# isdisjoint() returns True if two sets don't have any common items between them. else, False

things1 = {"table", "chair", "book"}
things2 = {"stool", "television", "cap"}
print(things1.isdisjoint(things2))

A = {1, 2, 3}
B = {4, 5, 6}
C = {6, 7, 8}
print("A and B are disjoint:", A.isdisjoint(B))
print("A and C are disjoint:", B.isdisjoint(C))

# issubset() returns True if setA is the subset of setB, 
# i.e if all elements of setA are present in setB, else, False

subjects = {"French", "Furthermaths", "Music"}
subjects2 = {"French", "Furthermaths", "Music", "Biology", "Agric"}

print(subjects.issubset(subjects2))
print(subjects2.issubset(subjects))

# issuperset() method returns True if all items in the specified set are present in the original set, else, False

# to check if all items in music2 are present in music
music = {"piano", "violin", "guitar", "trumpet"}
music2 = {"trumpet", "piano"}
print(music.issuperset(music2))

# to check if all items in music are present in music2
print(music2.issuperset(music))

# union() method returns a new set that contains all items from original set
# the union of two given sets A and B is a set that consists of all the elements of A;
# and all the elements of B such that no element is repeated

continents = {"Africa", "Asia", "Europe"}
continents2 = {"Europe", "America"}
print(continents.union(continents2))

food = {"rice", "beans", "yam", "spaghetti"}
food1 = {"beans", "spaghetti", "potatoe", "soup"}
food2 = {"potatoe", "soup", "corn"}
print("Union of 3 sets is :", food.union(food1, food2))

# update() method updates the current set, by adding items from another set (or any other iterable)
# if an item is present in both sets, only one appearance of this item will be present in the updated set

careers = {"influencer", "tech", "lawyer", "artist"}
careers2 = {"footballer", "tech", "engineer", "influencer"}
careers.update(careers2)
print(careers)

lts = {"c", "d"}
lts2 = {"five", "bicycle"}
lts.update(lts2)
print(lts)



"""
# Question #3
------------------------------------------------------------------
Write a function that takes a list of numbers and returns only the
uniques numbers in the list.
"""

nums = [1, 2, 2, 3, 4, 5, 2, 3, 6, 5, 7, 5]
print(list(set(nums)))


"""
# Question #4
------------------------------------------------------------------
Return the value 20 from the tuple below:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

N/B: you do not need to write a function for this question
"""

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


"""
# Question #5
------------------------------------------------------------------
Unpacking of values in a tuple.
If a tuple has 4 values, it can be unpacked by declaring four
variables and assigning the tuple to it.

Unpack the values of the tuple into 4 variables and print them out.
tuple2 = (3, 10, 45, 78)
"""

tuple2 = (3, 10, 45, 78)
a, b, c, d = tuple2

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

identities = (("name", "Dinma", "age", 30), ("name", "Okon", "age", 40), ("name", "Peter", "age", 21), ("name", "Shola", "age", 12))
print(identities)


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

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 & set2)


"""
# Question #8
------------------------------------------------------------------
Write a function called `calculation` that takes any number integers
values as positional arguments and returns a tuple of the addition
of the values and subtraction of the values.
If only one value is given return a tuple of just that value.
"""


    