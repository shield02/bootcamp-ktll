# string slicing assignment

"""
# Question 1
-------------------------------------------------------
Create a variable for the string 'Python is Fun!' and
write the commands that will return the following
- 'ytho'
- 'Pytho'
- 'ython is Fun!'
- 'Python is Fun!'
- 'yhni u'
- 'yoiF'
- 'Pto sFn'
"""

"""
# Question 2
-------------------------------------------------------
Create 3 variables to store
- 'hello'
- ','
- 'world'
and a fourth variable that will be a concatenation of
the first and third variable.c
Write a command that will give the following output
- 'ello'
- 'elloworl'
- 'elwr'
- 'dlrowolleh'
"""


message = 'Python is Fun!'

print(message[-13:-9])
print(message[-14:-9])
print(message[-13:])
print(message[:])
print(message[1:13:2])
print(message[1:13:3])
print(message[0:13:2])

first_word = 'hello'
second_word = ','
third_word = 'world'
greeting = first_word + third_word
print(greeting)
print(greeting[1:5])
print(greeting[1:9])
print(greeting[1:9:2])
print(greeting[-1:-11:-1])
