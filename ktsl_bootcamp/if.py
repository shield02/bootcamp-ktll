# IF LOGICAL FUNCTION
"""
A logical function is used to write a logical statement
A logical statement allows you to write code that can
make decisions.
A logical statement will have a logical test that test
a condition for truth value and then executes block of
code else it will execute another block of code if the
logical test is false.

So to write a logical statement, we use the IF function.
If you have more than one logical test you will use ELIF
in addition to the the IF.
The IF statement may have an ELSE block that will execute
in an instance where the IF logical test is false
"""
# EXAMPLE
# Write a function that will take a word, start and stop value
# and will only slice the string if the
# length of the string is greater than the stop value
# by 3
def the_word(word, start, stop):
    """Slice the string if it is longer than stop value."""
    string_len = len(word)
    if (string_len + 3) > stop:
        return word[start:stop]

result = the_word("statement", 2, 5)
print(result)

def the_word(word, start, stop):
    """Slice the string if it is longer than stop value."""
    string_len = len(word)
    if (string_len + 3) > stop:
        return word[start:stop]
    else:
        return f"Your stop value {stop}, is larger than the length of the string."

result = the_word("statement", 2, 15)
print(result)

# EXAMPLE
# Write a function that takes a number 
# if the number is less than 3, it should return "level 1"
# if the number is 3 and less than 7, return "level 2"
# if it is equal to and above 7, return "high level"
def my_number(num):
    """Return different levels based on number."""
    if num < 3:
        return "level 1"
    elif num >= 3 and num < 7: 
        return "level 2"
    else:
        return "high level"

"""
 true and true == true
 true and false == false
 false and true == false
 flase and false == false
"""

result = my_number(9)
print(result)

result = my_number(4)
print(result)

result = my_number(3)
print(result)

# CLASSWORK
# Create a variable that will hold a number
# Using the IF, ELIF and ELSE check for the following conditions
# when the number is less than 5, print "good"
# when the number is equal to 5 but less than 10, print "better"
# for any other number print, "too high"
shoe_size = 39
if (shoe_size < 5):
    print("good")
elif (shoe_size >= 5) and (shoe_size < 10):
    print("better")
else:
    print("too high")

animal = 'elephant'
word = len(animal)
if word < 5:
    print("good")
elif word >= 5 and word < 10:
    print("better")
else:
    print("word is too long")
