"""
# Question 1
------------------------------------------------------------------
Create a variable called `username`.
Using a python function check the length of the string in the variable
and use the result as follows:
- a case that the length is smaller than 3, print "Invalid username. Must be at least 3 characters long"
- a case that the lenght is greater than 15, print "Invalid username. Must be at most 15 characters long"
- a case where the two conditons are not meet, print "Valid username"
"""

"""
# Question 2
------------------------------------------------------------------
Create a variable and assign any integer value to it.
Check whether is even and print "Even number".
In a case that the number is not even, print "Odd number".

TIP: to check whether a number is even use the modulo operator.
"""

"""
# Question 3
------------------------------------------------------------------
Create a variable called `happy` and assign an integer to it.
If the number in that variable is greater than 6, print "Hello World!!!"
but if the number is less than 6, print "Hi World!!!"
"""


identity = 'username'
length_of_identity = len(identity)
print(length_of_identity)
if 8 < 3:
    print("Invalid username. Must be at least 3 characters long")
elif 8 > 15:
    print("Invalid username. Must be at most 15 characters long")
else:
    print("Valid username")

number = 8
if (8%2) == 0:
    print("Even number")
else:
    print("Odd number")

mood = 'happy'
mood = 9
if 9 > 6:
    print("Hello World!!!")
else:
    print("Hi World!!!")
    