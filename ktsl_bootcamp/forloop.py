# FOR LOOP
"""
A for loop allows you to repeatedly do something in
your code.

You will use a for loop when you know the exact number of times
you want to loop.

So to use a for loop you will need to specify a sequnce you will
use to perform the loop.

A sequence here can be anything that can be deal with one item
after another.

Example of such sequence include, string, list, tuple

Sometimes you will use a special function called range() to
generate this sequence.

The range function is used like this
range(start,stop,step) - here start is the number you want the
sequence to start from, stop is the number where you want to the
sequnce to stop, and step is how many numbers should be counted
before the next number in the sequence.
"""
# Example using a string as a sequence
for letter in "python":
    print(letter)

print("--------------------------------------")
# Example where the string is in a variable
word = 'programming'
for l in word:
    print(l)

print("--------------------------------------")
# Example using a list that is stored in a variable
fruits = ['mango', 'banana', 'orange', 'apple']
for fruit in fruits:
    print(fruit)

print("--------------------------------------")
for f in fruits:
    print(f)

print("--------------------------------------")
# Example using the range function
# The range function will generate a sequence of numbers
for number in range(0, 8, 1):
    print(number)

print("--------------------------------------")
for number in range(0, 8, 2):
    print(number)

print("--------------------------------------")
for number in range(0, 8):
    print(number)

print("--------------------------------------")
# Example with using string
for letter in "LANGUAGE":
    print(letter.lower())

print("--------------------------------------")
for letter in "language":
    print(letter.upper())

# CLASSWORK
"""
Using string in a variable, write a for loop that
will print each of the letter on seprate lines.
"""
print("--------------------------------------")
word = "Dogacademy"
for l in word:
    print(l)

"""
Using the range function, write a for loop that
will print only even numbers between 0 and 20
both numbers should be included in the printing
"""
print("--------------------------------------")
for number in range(0, 22, 2):
    print (number)

"""
Using a list of colors stored in a variable, write a
for loop that prints each color and makes them capital
letters.
"""
print("--------------------------------------")
colors = ["white", "grey", "black"]
for color in colors:
    print(color.upper())

"""
Using a range function, write a for loop that with print
7 numbers starting from 3.
"""
print("--------------------------------------")
for number in range (3, 10, 1):
    print(number)

print("--------------------------------------")
# Example with range function and if statement
"""This example will only print even numbers from the sequence."""
for num in range(3, 10):
    if num % 2 == 0: # The % checks that when num is divided by 2 there is 0 remainder
        print(num)

print("--------------------------------------")
# CLASSWORK
"""
Using the range function, write a for loop that will print odd
numbers, between 0 and 11. Both numbers may not be included.
"""
for num in range(1,11):
    if num % 2 != 0:
        print(num)

print("--------------------------------------")
for num in range(1, 11):
    if num % 2 == 1:
        print(num)


# ASSIGNMENT
"""
Write a function called greet_names that takes one argument that will be
a list of names, loops over the list and print "Hi name" for each of the
name in the list.
"""

"""
Write a for loop that prints the multiples of 7 between 0 and 100. Print 
one multiple per line and avoid printing any numbers that aren't 
multiples of 7. Remember that 0 is also a multiple of 7.

A mutiple of 7 is a number that be divided by 7, for example 7, 14, 21, ...
"""