print ("how many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles,2)
print ("ok, you said" + ' ', miles)
print (f"that is equal to {miles} miles")

#round is a function that helps you round off numbers
#when using the rounf function, you will input 2 things
#the thing to round and to how many decimal points
#round(thing to round, how many decimal points)

print("ok, you said" + ' ', {round(miles,2)})
print("your {kms}km ride was {miles}miles") # deosnt really print out the input you want
#so you have to use the f string method

print(f"your {kms}km ride was {miles}miles")
#this round offs off the miles to 2 decimal points


"""

------- USER INPUT ---------
Input is a built in function in python that will prompt the user
and store the result to a variable
"""
#Example

data = input("What's your favourite color")
print("You said" + data) # this will print out my favourite colour

data = input("What's your favourite color")
data = input() #this takes it to another line
print("You said" + data) # this will print out my favourite colour




