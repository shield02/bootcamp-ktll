# Create a for loop to print numbers from 1 to 10
for n in range(1,11):
    print(n)

# Solution 2
a = 0
while a < 7:
    print('number', a)
    a = a + 1

# Print numbers from 1 to 10 using a for loop
for d in range(1,11):
    print(d)

'''
Write a program to print all even numbers that fall between two numbers
(exclusive both numbers) entered from the user using while loop.
'''
number = 1
while number < 40:
    if number % 2 == 0:
        print('even', number)
    number = number + 1

'''
Write out a program to print out the first natural number in reverse order
Using a while loop
Using a for loop
'''

# Using a while loop
number = 10
while number >= 1:
    print('backwards', number)
    number = number - 1

# Using a for loop
for i in range(10,0,-1):
    print(i)

'''
Write a for loop statement to print the following series
10,20,30,40,50,60,70,80,....300
'''
for i in range(10,301,10):
    print(i)

'''
Write a while loop statement to print the following series
105,98,91,....7
'''
number = 105
while number >= 7:
    print('hey', number)
    number = number - 7

'''
Write a program to print the following using while loop
First 10 even numbers
First 10 odd numbers
First 10 natural numbers
First 10 whole numbers
'''
# First 10 even numbers
number = 1
while number <= 20:
    if number % 2 == 0:
        print('even', number)
    number = number + 1

# First 10 odd numbers
digit = 1
while digit <= 20:
    if digit % 2 != 0:
        print('odd', digit)
    digit = digit + 1

# First 10 natural numbers
number = 1
while number <= 10:
    print('natural', number)
    number = number + 1

# First 10 whole numbers
number = 0
while number <= 9:
    print('whole', number)
    number = number + 1

