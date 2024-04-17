"""
# CLASSWORK
--------------------------------------------------------------------
Write a function that takes two arguments, your first name and last name then prints your full name.
Write another function that takes two arguments, your first name and last name then returns your full name.
"""


# Solution
def ful_name(fname, lname):
    print(fname, lname)


ful_name('Uduak', 'Eti-mfon')


def full_name(fname, lname):
    return fname, lname


print(full_name('Uduak','Eti-mfon'))

# Create a function that prints out the names of all the children in your family


def children_names(child_name):
    print(child_name + ' ' + 'Eti-mfon')


# Write out a function that prints out the name of the fourth child in your family
children_names('Emem')
children_names('Ime')
children_names('Mfon')
children_names('Uduak')
children_names('Itoro')


def position(*siblings):
    print('The fourth child is ' + siblings[3])


position('Emem', 'Ime', 'Mfon', 'Uduak', 'Itoro')


# Write out a function that prints out my favourite meal
def food(*fav_food):  # Add a * before the parameter if you do not know how many arguments will be passed into your function.
    print('My favourite food is ' + fav_food[0])


food('ekpang_nkukwo', 'white_soup', 'banga_soup', 'fried_rice', 'potato_chips')


# Write out a function that prints out my favourite subject
def subjects(*fav_course):
    print(f'I love {fav_course[5]} so much')


subjects('biology', 'english', 'mathematics', 'agric', 'physics', 'french', 'phe')


# Write out a function that prints out the name of the fourth child in your family using keyword arguments
def children(child3, child5, child1, child2, child4):
    print(child4 + ' ' + 'is the fourth child')


children(child1='Emem', child2='Ime', child3='Mfon', child4='Uduak', child5='Itoro')


# Write out a function that prints out my favourite subject using keyword arguments
def sub(**fav_sub):  # Use ** before the parameter name in the function if you do not know how many kwargs will be passed into the function
    fav_sub = dict(sub5='mathematics', sub2='physics', sub1='french', sub3='phe', sub4='economics')
    print(fav_sub['sub1'] + ' ' + 'is my favourite subject')


sub()


# Write a python function to find the maximum of two numbers
def max(x,y):
    if x > y:
        print(str(x) + '' + 'is the greater number')
    else:
        print(str(y) + ' ' + 'is the greater number')
    

max(12, 20)


# Write a python function to find the maximum of three numbers
def maxi(x, y, z):
    if x > y and x > z:
        print(str(x) + ' ' + 'is the greatest number')
    elif y > z and y > x:
        print(str(y) + ' is the greatest number')
    else:
        print(f'So, it is {str(z)} that is the greatest')
    

maxi(32, 42, 50)


# Alternatively, use the max_of_two functions to find the greatest number among three numbers
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
    

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(54, 20, 60))


# Write a python function to sum up all the numbers in a list. Sample list: (12,36,47,23)
def add_nums(a, b, c, d):
    print(a + b + c + d)


add_nums(12, 36, 47, 23)


# Alternatively, you can use a for loop to solve the question above
def summation(*numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total
    

print(summation(12, 36, 47, 23))


# Write a function list to multiply all the numbers in the list[4,5,6,8,10]
def multiply(*digits):
    product = 1
    for digit in digits:
        product = product * digit
    return product


print(multiply(4, 5, 6, 8, 10))

# Write a python program to reverse a string
word = 'hippopotamus'
print(word[::-1])


# Alternatively, use the function and loop method 
def rev_word(word):
    rev = ''
    index = len(word)
    while index > 0:
        rev += word[index - 1]
        index = index - 1
    return rev


print(rev_word('hippopotamus'))

'''
Print the given strings in reverse using first, functions and loops and subsequently, string slicing.
a. Concentration
b. Mediteranean
c. Endometriosis
d. Insubordination
'''

# USING STRING SLICING
word = 'Concatenation'
print(word[::-1])
phrase = 'Mediterranean'
print(phrase[::-1])
fact = 'Endometriosis'
print(fact[::-1])
attitude = 'Insurbordination'
print(attitude[::-1])


# USING FUNCTIONS AND LOOPS
def from_last(phrase):
    phr = ''
    length = len(phrase)
    while length > 0:
        phr += phrase[length - 1]
        length -= 1
    return phr


print(from_last('Concatenation'))


# Second word
def from_back(word):
    wor = ''
    length = len(word)
    while length > 0:
        wor += word[length - 1]
        length -= 1
    return wor


print(from_back('Mediterranean'))


# Third word
def rever(word):
    w = ''
    l = len(word)
    while l > 0:
        w += word[l-1]
        l -= 1
    return w


print(rever('Endometriosis'))


'''
Write a python function to calculate the factorial of a number(a non-negative integer)
The function accepts the number as an argument.
'''


# Solution
def factorial(num):
    if num == 0:
        return 1  # Factorial of 0 is defined as 1 by convention
    else:
        return num * factorial(num - 1)
    

num = int(input('Enter a number: '))
print(factorial(num))


# Write a program to find the sum of natural numbers using recursive function
def recur_sum(num):
    if num <= 1:
        return num
    else:
        return num + recur_sum(num - 1)
    

print(recur_sum(20))
















