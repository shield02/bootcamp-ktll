'''
Using the for loop and while loop, print out the following
Even numbers from 0 to 50
Odd numbers from 0 to 50
Integers and their squares #integers between 0 and 20
'''

# Even numbers from 0 to 50
# Using while loop
number = 1
while number <= 50:
    if number % 2 == 0:
        print('Even', number)
    number = number + 1

# Using for loop
for e in range(0,51,2):
    print(e)

# Odd numbers from 0 to 50
# Using while loop
number = 1
while number <= 50:
    if number % 2 != 0:
        print('Odd', number)
    number = number + 1

# Using for loop
for o in range(1,50,2):
    print(o)

# Integers and their square. Integers between 0 and 20
# While loop
number = 0
while number <= 20:
    print('num', number) 
    print(number * number)
    number = number + 1

# Using for loop
for o in range(0,20,1):
    print(o)
    print(o*o)

'''
Loop through numbers 1 - 20
For 4 and 13, print "x is unlucky"
For even numbers, print "x is even"
For odd numbers, print "x is odd"
'''
# Using for loop
for y in range(1,21,1):
    if y % 2 == 0:
        print('x is even', y)
    elif y % 2 != 0:
        print('x is odd', y)

# Using while loop
number = 1
while number <= 20:
    if number % 2 == 0:
        print('x is even', number)
    elif number % 2 != 0:
        print('x is odd', number)
    number = number + 1

# Write out a programme to print multiplication table of a given number
n = 3
for i in range(1,13,1):
    product = n * i
    print(product)

n = 5
for r in range(1,13,1):
    product = n * r
    print(product)

# Write a program to print first 10 even numbers in reverse
# Using for loop
for e in range(20,1,-2):
    print(e)

