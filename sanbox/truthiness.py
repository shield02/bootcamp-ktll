#TRUTHINESS AND LOGICAL OPERATORS

animal = input("enter your favourite animal")
if animal: #means if animal exist
    print(animal + " ","is my favourite too" )
else:
    print("you didn't say anything")

"""
In python all conditional checks resolve to True or False
values that resolve to True are called "truthy", values that
resolve to false are called "falsy".
Besides False conditional checks, other things that are naturally
falsy include: empty objects, empty strings, None, zero.
"""

city = input("where do you live?")

if city == "los angeles" or city == "san francisco":
    print("YOU LIVE IN CALIFORNIA")
else:
    print("YOU LIVE SOMEWHERE ELSE")

age = 21
# 2-8: 2 dollar ticket
# 65 : 5 dollar ticket
# 10 dollar ticket for everyone else

if not((age >= 2 and age <= 8) or age >=65):
    print("YOU PAY 10 DOLLARS and not a child or senior") 
else:
    print("YOU ARE A CHILD OR SENIOR")





