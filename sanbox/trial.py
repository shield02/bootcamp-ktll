# QUESTION 1
"""
Using a loop print out the word "programming" like this
Pp
Rr
Oo
Gg
....till the end of the word.
"""
# Solution
phrase = 'programming'
for q in phrase:
    print(q.upper(),q)

"""
# Question 4
Write a while loop to display numbers from 10 to 1.
"""
# Using while loop
num = 10
while num >= 1:
    print(num)
    num -= 1

"""
# Question 5
Using a nested for loop, print the following output
111111111
222222222
...
888888888
999999999
"""
r = 9
for i in range(1,r+1):
    for j in range(1,r+1):
        print(i , end='')
    print()
