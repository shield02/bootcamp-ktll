# Boolean conditional logic

#Boolean: a bool is a data type in Python that is 
#either True or False

"""
#Conditional logic
.....................................................
In Python we can logically test the condition of something
and then make some certain decisions based on the result of 
the test we did

How can we write a logical test statement?
we can use mathematical operators or logical operators to write a test 
statement. The result of a test statement is always a bool

Which mathematical operators can we use to write a test statement?
# mathematical operators
..................
< less than
> greater than
<= less than or equal to
>= greater than or equal to
= equal to

what are the logical operators
#logical operators
...............................
and: gives a true only when both sides are true
or: gives a False only when both sides are false

False and False ==  False
False and True ==  False
True and False == False
True and True == True

True or false == True
False or True == True
True or True == True
False or Fasle == False
............................................
A logical statement is going to be an expression with something on 
the left and something on the right with the operator in between them
"""

print (4 < 7) #this is a logical statement. 
print (6 == 1)
print (7 <= 7)

print(4 > 4 and 3 == 1) #bool and bool : false and false == false
print(3 < 2 or 2 < 2) #bool or bool : false or False == False

"""
#Branching statements using "If statement
....................................................
 The branching statement is done in  python using the If function
 
 It allows you perform certain operations or task based on the result
 of a logical statement

 You can have a single or multiple if statement.

 The if statement must evaluate to True
"""
if 4 == 1: # the logical statement here is evaluated based on Truth value
    print("we are winners") #this will only run on the condition that the logical statement was true

if 3 < 7:
    print('this is now going to be printed')

#In a case where we still want to do something when it evaluated to false
if 4 == 1: #this evaluation is false
    print("this will not print in this situation") #this will not print
else: #you need to have this else statement to cover for the situation where the logical statement was False
    print("this is what will be printed") #this is what will be printed

#Example of a multiple if statement
if 4 > 5:
    print("Yes we are going higher")
elif 4 < 5:
    print("it was actually the other way round oh!")
elif 5 == 5:
    print("we are even")
else:
    print("Omo we have lost our way oh!!!")
