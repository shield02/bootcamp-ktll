"""
continuation of while loop"""

current_age = 25
employment_age = 25
retirement_age = 70
while employment_age < retirement_age:
    #continue to promote the person after every 4 years
    print("you have been promoted", employment_age)
    employment_age +=4
print("you are retired!")

print("----------------")

current_age = 25
employment_age = 25
retirement_age = 70
while current_age > employment_age and current_age < retirement_age:
    #false and true = false. the loop won't run
    print("you have been promoted")

print("************************")

current_age =25
employment_age = 25
retirement_age = 70
while current_age < retirement_age: #looping is used cos it's going to be a repeated thing.
    #check if current age is the same as employment age we will continue
    if current_age <= employment_age:
        current_age +=4
        continue #means do not proceed with the other lines in the loop, instead start afresh
    print("you have been promoted", current_age)
    current_age +=4
print("you are retired!")


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# you can also do this
"""
adding the promote after variable helps in case you want to change 
how many years the person will  be promoted after. so that 
it will be easier to just change it at 1 place and its effectes
in all the places you have to put it in
"""
current_age =25
employment_age = 25
retirement_age = 70
promote_after = 3
while current_age < retirement_age:
    if current_age <= employment_age:
        current_age += promote_after
        continue
    print("you have been promoted",current_age)
    current_age += promote_after


#write a while loop that prints only even numbers between 1 and 20
    
num = 1
while num <= 20:
    if num % 2 == 0:
        print("even number", num)
    num += 1


