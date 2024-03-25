number = 1
while number <= 20:
    if number % 2 == 0:
        print('Even no', number)
    number = number + 1

# Write a loop that prints out multiples of 3 from 0 to 60
number = 0
while number <= 60:
    if number % 3 == 0:
        print('Multiple of 3', number)
    number = number + 1

# Doing a for loop that prints out multiples of 3 from 0 to 60
for number in range(0,61):
    if number % 3 == 0:
        print(number)

'''
# Create a while loop and a for loop that prints out the odd numbers between 0 and 40
'''
# WHILE LOOP
number = 0
while number <= 40:
    if number % 2 != 0:
        print('odd number', number)
    number = number + 1

# FOR LOOP
for o in range(40):
    if o % 2 != 0:
        print(o)
