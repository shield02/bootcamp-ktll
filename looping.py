"""
# LOOPING IN PYTHON
--------------------------------------------------------
# in python a loop is simply what repeats itself

There are two types of looping in Python
- while loop
- for loop

WHILE LOOP
---------------------------------------------------------
The while loop is used when you do not know the exact number
of times you want the loop to run.
So it means that a while loop is sutibale when you want to keep
running the loop till a certian condition is met.
The while loop only needs a condition that will be tested each
time the loop runs


FOR LOOP
----------------------------------------------------------
The for loop is used when you know the exact number of times
you want the loop to run.
So it means the for loop is suitable when you have an exact
number of times before hand you want the loop to run.

Usually, the for loop is used with the range() function. The
range() function generates a list of numbers within a start
value and an end-1 value

range function takes 3 argument
- start value
- end value
- step value
range(start, end, step) - this will give you values from start to end-1 with step
range(end) - this will give you from 0 to end-1, and assume the step to be 1
range(start, end) - this will give you values from start to end, and assume the step to be 1

"""
# Example - while loop
# when you are doing while loop you MUST set a value outside the loop
counter = 1
while counter < 7:  # the condition that must always be True
    print("I are hungry.", counter)
    counter = counter + 1  # you must increase or decrease this inside the loop, or else your loop will run infinitly


age = 30
while age > 23:
    print("You can work for us", age)
    age = age - 1  # decrease the value of age
    
cups = 0
while cups <= 5:
    print('Add more cups', cups)
    cups = cups + 1

# 25 March 2024 - continuation of loops
# Revision
current_age = 25
employement_age = 25
retirement_age = 70
promote_after = 4
while current_age < retirement_age:  # looping is used because it will be a repeated thing
    # check if current is the same with employment age we will continue
    if current_age <= employement_age:
        current_age = current_age + promote_after
        continue # means do not proceed with the other lines in the loop, instead go and start from the begining again
    # continue to promote the person after every 4 years
    print("You have been promoted.", current_age)
    current_age = current_age + promote_after
print("You are a retireeeee now")

# Classwork
"""
Write a while loop that prints only even numbers between 1 and 20. Tip: use the modulo operator
"""

# For loop
""""
The for loop works with only things that are iterable.
Iterable means it can pick one item at a time.

So data types/strutures that are iterable in python include
- strings
- list
- dictionary
"""
for letter in "python":
    print(letter)
print("---------------------------------------------")
for number in range(1,10):  # range(1,10) will give you a sequence of numbers 1,2,3,4,5,6,7,8,9
    print(number)
print("---------------------------------------------")
for number in range(10):    # range(10) will give a sequence of numbers 0,1,2,3,4,5,6,7,8,9
    print(number)
for i in range(21):
    if i % 2 == 0:
        print(i)