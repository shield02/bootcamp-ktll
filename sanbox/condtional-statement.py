gname = "Emem Jolie"
if name == "Uduak Edikan":
    print("you you")
elif name == "Emem Jolie":
    print("There you have it")
else:
    print("forget about it")

name = "Jolie"
if name == "jolie":
    print('welcome')
else:
    print("let's move on")

#you can have multiple elif's but only 1 else

colour = input("what's your favourite colour?")
if colour == "Blue":
    print("good choice!")
elif colour == "yellow":
    print("wow, you don't say")
elif colour == "green":
    print("not bad")
else:
    print("silly you!")

"""
-----------------------------------
TRUTHINESS OR FALSINESS
"""

animal = input("enter your favourite animal")
if animal: #this means that if animal exist at all or is mentioned then print next line
    print(animal = "is my favourite animal too")
else:
    print("you said nothing")

