# WHILE LOOP
"""
A loop is a way of doing something repeatedly in your program.

You will need a WHILE loop when you want to do something till
a certain condition becomes false.

So that means, when you are in need of a WHILE loop, you will
need to start with setting a condition. 

Usually, the codition is set beside the WHILE.

The loop will keep
running only when the condition is true and until that condition
becomes false.

So that means you will need to have a way of modifying the condition
so that at some point it will no more be true but it will be
false so that the loop might stop.

If you do not have a way of modifying the condition, then the
loop will keep running and running without stopping.

Usually, you will be modifying the condition inside of the loop.
"""
# Example
num = 0 # start value for the condition
while num < 10: # (num < 10) is the condition
    print(num) # we are simply printing the value of num
    num = num + 1 # this is where we modify the condition

print("--------------------------------------------------")

# CLASSWORK
"""
Write a loop that starts with 5 and stops running
when the number is 10
"""
num = 5
while num <= 10:
    print(num)
    num = num + 1

number = 5
while number < 11:
    print(number)
    number = number + 1

# Example - A fun example
word = 'assignments'
while len(word) >= 3:
    print(word)
    word = word[:-1]

word = 'assignments'
while len(word) >= 3:
    print(word)
    word = word[1:]

# CLASSWORK
"""
Write a loop that will always trim the last 2
letters of a work till it remains 2 letters.
"""
# Option 1
word = "hippopotamus"
if len(word) % 2 == 0:
    while len(word) >= 2:
        print(word)
        word = word[:-2]
else:
    while len(word) >= 2:
        print(word)
        word = word[:-1]

# Option 2
word = "hippopotamus"
while len(word) >= 2:
    print(word)
    word = word[2:]

# ASSIGNMENT
"""
Write a while loop that adds 3 to a number while the number
is still less than 500, and print only the last number after
while loop is complete.
"""
print("---------------------------------------")
num = 0
while num < 500:
    # num += 3 # += does two things. both adding 3 to num and reassign it back to num
    num = num + 3 # same thing like this
print (num)

"""
Write a function that takes one variable that will be a number
and prints a number while the number is less than the number passed
as the variable. print "Done", once the while loop is complete.
"""
print("--------------------")
def uptil(num):
    n = 0
    while n < num:
        print(n)
        n = n + 1
    print("Done")

uptil(8)
