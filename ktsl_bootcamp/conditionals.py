"""
BRANCHING PROGRAM - CONDITIONAL STATEMENTS

IF STATEMENT
"""
colors_list = ["purle", "blue", "yellow", "red", "pink"] # list

x = 0
if x > 10:
    print("It is less than 10 for now, keep going.")
else:
    print("It is greater than 10, truly.")

y = 12
if y % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

salary = 2_000_000
if salary < 2_000_000:
    print("We no dey do am o")
else:
    print("We go work am")

colors_tuple = ("purle", "blue", "yellow", "red", "pink") # tuple
if len(colors_tuple) == 5:
    print("We are on track")
else:
    print("We don enter express")

shoe_size = 20000.87
if shoe_size == 300:
    print("Meet Mayen for your shoe")
elif shoe_size >= 400:
    print("Meet Goodnews for your shoe")
elif shoe_size <= 200:
    print("Meet Ima-Abasi for your shoe")
else:
    print("We don't have your shoes, sorry")

shoes = ["flat", "stilletoes", "pumps"]
if "flat" in shoes:
    print("We have that shoe")
else:
    print("Check back after next week")

if len(shoes) == 3:
    print("Your shopping bag is full.")
    print("You can only pick 3 shoes at a time")
else:
    print("Select another shoes")
    print("You can still add to your shopping bag")



