"""
# QUESTION 1
Using a loop print out the word "programming" like this
Pp
Rr
Oo
Gg
till the end of the word.

"""

word = "programming"

for letter in word:
    print((letter * 2).title())

"""
# Question 2
Write a script that prints the first 10 cube numbers (x**3),
starting with x= 1 and ending with x= 10.

"""
for i in range(1, 11):
    print(i ** 3)

"""
 # Question 3
Write a script that prints the multiples of 7 between 0 and 100.
Print one multiple per line; avoid printing numbers that aren't multiples of 7.
Remember that 0 is also a multiple of 7.
"""

for num in range(0, 101):
    if num % 7 == 0:
        print(num)

"""
# Question 4
Write a while loop to display numbers from 10 to 1.
"""

x = 10
while (x >= 1):
    print(x)
    x -= 1

"""
# Question 5
Using a nested for loop, print the following output
111111111
222222222
...
888888888
999999999
"""

# No of rows
rows = 9

# outer loop
for i in range(1, rows + 1):
    # inner loop
    for x in range(1, rows + 1):
        print(i, end='')
    # new line after each row
    print()
