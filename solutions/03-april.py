"""
# QUESTION 1
Using a loop print out the word "programming" like this
Pp
Rr
Oo
Gg
....till the end of the word.
"""
# Solution
word = 'programming'
for u in word:
    print(u.upper(),u)

"""
# Question 2
Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and 
ending with x=10.
"""
# Using for loop
for i in range(1,11):
    cube = i**3
    print(cube)

# Using while loop
num = 1
while num <= 10:
    cube = num**3
    print(cube)
    num += 1

"""
# Question 3
Write a script that prints the multiples of 7 between 0 and 100. Print one multiple 
per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 
is also a multiple of 7.
"""
# Using for loop
for m in range(0,101):
    if m % 7 == 0:
        print(m)

# Using while loop
digit = 0
while digit <= 100:
    if digit % 7 == 0:
        print(digit)
    digit += 1

"""
# Question 4
Write a while loop to display numbers from 10 to 1.
"""
# Using for loop
for y in range(10,0,-1):
    print(y)

# Using while loop
number = 10
while number > 0:
    print(number)
    number = number - 1


"""
# Question 5
Using a nested for loop, print the following output
111111111
222222222
...
888888888
999999999
"""
# Solution
r = 9
for i in range(1,r+1):
    for j in range(1,r+1):
        print(i , end='')
    print()

"""
# Guide
First, you will need a string variable where you will add the characters 
to be printed on the current line.
If your outer loop uses a variable named i, then your inner loop should 
use range(0, 9). In the inner loop, all you have to do is add the value 
of i to the string variable. You have to cast the integer i to a string 
first with str(i).

After the inner loop finishes, the outer loop prints the string variable 
and then sets it to the empty string '', clear for reuse in the next iteration.
"""