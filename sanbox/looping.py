"""
LOOPING IN PYTHON
--------------------------
# In python, a loop is simply what repeats itself

There are 2 types of looping in python
- while loop
- for loop

WHILE LOOP
.....................................
The while loop is used when you do no know the exact number
of times you want the loop to run
So it means that the while loop is suitable when you want to keep
running the loop till a certain condition is met.
The while loop only needs a conditiion that will be tested each
time the loop runs

FOR LOOP
The for loop is used when you know the exact number of times 
you want the loop to run.
So it means the for loop is suitable when you have an exact
number of times before hand you wnat the loop to run.

Usually the for loop is used with the range() function.
The range() function generates a list of numbers within a start
value and an end +1 value

range function takes 1 argument
-start value
-end value
-step value
range(start,end,step). This will give you values from start to end -1
with step
range(end). This will give you from 0 to end -1
range(start,end). This will give you values from start to end, and assume the step to be 1.

"""
#Example While loop
# when you are doing while loop you MUST set a value outside the loop
counter =1
while counter < 7: #the condition that must always be True
    print("i are hungry", counter)
    counter = counter + 1 #you must increase or decrease this inside the loop, or else your loop will run infinitely

age = 30
while age > 23:
    print("you can work for us",age)
    age = age -1 #decreases the value of age

    cups = 0
    while cups <= 5:
        print("Add more cups", cups)
        cups = cups + 1
        
