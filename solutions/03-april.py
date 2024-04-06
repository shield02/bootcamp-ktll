"""
# QUESTION 1
Using a loop print out the word "programming" like this
Pp
Rr
Oo
Gg
....till the end of the word.
"""
#SOLUTION 1
word = "programming"
for letter in word:
    print(letter.upper(),letter.lower())

        
        
"""
# Question 2
Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and 
ending with x=10.
"""
#SOLUTION 2


x = 1
cube = 3
while x <= 10:
    print("cube of {} = {}".format(x,x**cube))
    x +=1
#or
#value = 3
#for x in range(1,11):#i had a problem here cos when i put range to 10 it only printed till 9 
#    if x <= 10:
#        print("cube of {} equals {}".format(x,x**value))
    
#N.B. I had a problem with the for loop for this one thats why i commented it out

"""
# Question 3
Write a script that prints the multiples of 7 between 0 and 100. Print one multiple 
per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 
is also a multiple of 7.
"""
#SOLUTION 3
for i in range(100):
    if i % 7 == 0:
        print("this is a multiple of 7:",i)

"""
# Question 4
Write a while loop to display numbers from 10 to 1.
"""
#ANSWER 4
counter = 10
while counter <=10:
    if counter == 0:
        break
    print(counter)
    counter -= 1


"""
# Question 5
Using a nested for loop, print the following output
111111111
222222222
...
888888888
999999999

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

#ANSWER 5
for x in range(10): 
    for y in range(1,10):
        if x == 0:
            continue
        print(x, end= '')
    print()
    
