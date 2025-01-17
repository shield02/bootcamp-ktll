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
size = 5

for i in range(1, size + 1): # 1, 2, 3, 4, 5
    for j in range(1, size + 2): # 1, 2, 3, 4, 5, 6
        print(f'{i * j:4}', end=' ')
    print() # for a new line after each row

print("------------------------------")
for i in range(5):
    print(i, end=' ')

"""
Using a nested a for loop, create a 12 times addition table.
"""

