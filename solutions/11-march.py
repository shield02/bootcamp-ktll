
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


username = "tewogbade"
print(len(username))

if username <3:
    print("Invalid_username.")
if username >15:
    print("Invalid_username.")
else:
    print("Valid_username")



"""
# Question 2
------------------------------------------------------------------
Create a variable and assign any integer value to it.
Check whether is even and print "Even number".
In a case that the number is not even, print "Odd number".

TIP: to check whether a number is even use the modulo operator.
"""

tewogbade = 15
print(len(tewogbade))
num=int(input(15))
while(num%2 == 0):
    print("Even_number")
    break
    while (num%2 != 0):
        print("Odd-number")

"""
# Question 3
------------------------------------------------------------------
Create a variable called `happy` and assign an integer to it.
If the number in that variable is greater than 6, print "Hello World!!!"
but if the number is less than 6, print "Hi World!!!"
"""

happy = 15
if happy>6:
    print("Hello World!!!")
else:
    print("Hi World!!!")
