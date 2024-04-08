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


