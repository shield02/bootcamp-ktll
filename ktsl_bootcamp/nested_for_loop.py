# NESTED FOR LOOP
"""
A nested for loop is a for loop inside a for loop
You will also need a sequence to be able to run a
nested for loop.
"""
# CONTINUE STATEMENT and BREAK STATEMENT
# We will use a normal for loop for this first
# continue will skip the loop at some point
for i in range(5):
    if i == 3:
        continue
    print(i)

print("------------------------------")
colors = ['green', 'blue', 'orange', 'red', 'black', 'pink']
for color in colors:
    if color == 'blue':
        continue
    print(color)

print("------------------------------")
# CLASSWORK
"""
Write a for loop that will never print even numbers
between 5 and 25.
"""
for num in range(5, 25):
    if num % 2 == 0:
        continue
    print(num)

print("------------------------------")
# BREAK STATEMENT
# break will end the loop abruptly, or exit the loop
for i in range(2, 14, 2):
    if i > 8:
        break
    print(i)

colors = ['green', 'blue', 'orange', 'red', 'black', 'pink']

print("------------------------------")
for c in colors:
    if len(c) == 3:
        break
    print(c)

print("------------------------------")
for c in colors:
    print(c)
    if len(c) == 3:
        break

print("------------------------------")

# CLASSWORK
"""
Write a for loop that print until it gets to 5
in a sequence of 1 to 15.
"""
for i in range (1, 15):
    if i > 5:
        break
    print (i)

print("------------------------------")

for i in range (1, 15):
    if i == 6:
        break
    print (i)

# NESTED LOOP EXAMPLE
# We will use a multiplication table

print("------------------------------")

# Let us do 5 times table
size = 12

for i in range(1, size + 1): # 1, 2, 3, 4, 5
    for j in range(1, size + 2): # 1, 2, 3, 4, 5, 6
        print(f'{i * j:4}', end=' ')
    print() # for a new line after each row

print("------------------------------")
for i in range(5):
    print(i, end=' ')

"""
# ASSIGNMENT
Create a variable that stores your name and using a for loop
print your name in 5 columns and 6 rows with 8 spaces between
each columns.
"""
print("------------------------------")

name = "Goodnews"
for w in range(6): # for rows (outer loop)
    for u in range(5): # for columns (inner loop)
        print(f"{name:12}", end=" ")
    print()

print("------------------------------")

name = "Imaabasi"

for i in range(6):
    for j in range(5):
        print(f"{name:14}", end=" ")
    print()

print("------------------------------")

# CLASSWORK
"""
Using a nested for loop create a matrix where
each element of the matrix is multipled by the
2.

Each element of the matrix is the addition of
the outer loop value with the inner loop value.
"""
for i in range(3):
    for u in range(5):
        print(f"{i},{u}", end="   ")
    print()

print("------------------------------")

for i in range(6):
    for u in range(6):
        print(f"{(i+u)*2:3}", end=" ")
    print()

print("------------------------------")

for left in range(7):
    for right in range(left, 7):
        # print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print(f"[{left}|{right}]", end=" ")
    print()

print("------------------------------")

teams = [ 'Dragon', 'Wolves', 'Pandas', 'Unicorns' ]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")

# print("------------------------------")

# val = 65
# for i in range(0,5):
#     for j in range(0, i+1):
#         ch = chr(val)
#         print(ch, end=' ')
#         val = val+1
#     print()

# print("------------------------------")

# output = input('What is your name?: ')
# for x in range(5):  # for 5 rows
#     for y in range(3):  # for 3 columns
#         print(f"{output:8}", end=" ")
#     print()

print("------------------------------")

# CLASSWORK
""""
Using a while loop, print out each letter of a
string but if the letter is a vowel, print it in
capital letter.
"""
word = 'elephant'
counter = 0
while counter < len(word):
    letter = word[counter]

    if letter in 'aeiou':
        print(letter.upper(), end=" ")
    else:
        print(letter.lower(), end=" ")
    counter += 1
print()

print("------------------------------")
for letter in word:
    if letter in 'aeiou':
        print(letter.upper(), end=" ")
    else:
        print(letter.lower(), end=" ")
print()

print("------------------------------")

num = 0
string = ("evangeline")
while num < len(string):
    char = string[num]

    # Check if the character is a vowel
    if char.lower() in 'aeiou':
        # Print the vowel in capital letters
        print(char.upper())
    else:
        # Print the non-vowel character as is
        print(char)
    
    # Increment the num variable
    num += 1