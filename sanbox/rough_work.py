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

# Using while loop
number = 20
while number > 1:
    if number % 2 == 0:
        print('R even', number)
    number = number - 1

# Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)

# Print numbers divisible by 3 or 5 from 1 to 20 using a for loop
for num in range(1,21):
    if num % 3 == 0 or num % 5 == 0:
        print(num)
'''
Print a list of squares of numbers from 1 to 10
Using while loop
Using for loop
'''

number = 1
while number <= 10:
    num_2 = number * number
    print(number, num_2)
    number = number + 1

'''
Write out a program that prints numbers from 1 to 10, formatted like this
Current value: 1
Current value: 2
Current value: 3
Use both the while loop and the for loop
'''
# Using the while loop
number = 1
while number <= 10:
    print('Current value:', number)
    number = number + 1

# Using for loop
for i in range(1,11):
    print('Current value:', i)

'''
Write a program to print first ten even numbers in reverse
Using a while loop and a for loop
'''
# Using a while loop
number = 20
while number >= 1:
    if number % 2 == 0:
        print('Backwards even', number)
    number = number - 1

# Using for loop
for e in range(20,1,-2):
    print(e)

'''
Write a program to display all the numbers which are divisible by 11
and not by 2 between 100 and 500
Using while loop and for loop
'''
# Using a while loop
number = 100
while number < 500:
    if number % 11 == 0 and number % 2 != 0:
        print('Result', number)
    number = number + 1

# Using a for  loop
for i in range(100,500):
    if i % 11 == 0 and i % 2 != 0:
        print(i)

'''
Create a loop that iterates over a range and produces the following output
5
6
7
8
9
'''
# Using a while loop
number = 5
while number <= 9:
    print(number)
    number = number + 1

# Using for loop
for n in range(5,10):
    print(n)

'''
Create a loop that iterates over a range and produces the following output
0
25
50
75
Using a for loop and a while loop
'''
# Using a for loop
for i in range(0,76,25):
    print(i)

# Using a while loop
number = 1
while number <= 75:
    if number % 25 == 0:
        print(number)
    number = number + 1

'''
Print out the squares of the numbers that fall between 10 and 30
Using a for loop and a while loop
'''
# Using a while loop
number = 10
while number < 30:
    square_num = number * number
    print(square_num)
    number = number + 1

# Using a for loop
for i in range(10,30):
    square_num = i * i
    print(square_num)

# Find the multiples of a number using while loop
n = int(input('Enter an integer: ' ))
i = 1
while i <= 12:
    multiple = i * n
    print(multiple)
    i = i + 1

'''
Write a program to print multiples of 3 or 5 that fall between 10 and 500
Using a while loop and for loop
'''
# Using while loop
digit = 10
while digit < 500:
    if digit % 3 == 0 or digit % 5 == 0:
        print(digit)
    digit = digit + 1

# Using a for loop
for d in range(10,500):
    if d % 3 == 0 or d % 5 == 0:
        print(d)










    



