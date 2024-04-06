# for loop
"""
The for loop works with only things that are iterable
Iterable means it can pick one item at a time.

So data types/ structures that are iterable in python
include:
- strings
- list
- dictionary
"""
for letter in "python":
    print(letter)
print("""""""")

for i in range(1,10): #range will give you a sequence of numbers 1,2,3,4,5,6,7,8,9
    print(i)

print("@@@@@@@@@@@@@@@@@@@@")

for n in range(10): #will give you a sequence of numbers from 0 to 10 minus 1
    print(n)

print("!!!!!!!!!!!!!!!")

#Exercise: Print all even numbers between 1 and 20
for a in range(1,21):
    if a % 2 == 0:
        print(a)

"""
A for loop is used when we know beforehand how long we want
the loop to run
"""
print("another example")
#example if i want to loop fot 10 times
for number in range(10): #generates numbers from 0 to 9
    print("time",number)
print("-------------------")
for number in range(1,11):
    print("time",number)

#print only even numbers
for i in range (1,21):
    if i % 2  == 0:
        print('even number', i)

print("ok oh")
#you can also do it this way
for i in range(0,20,2):
    if i == 0:
        continue
    print("even number", i)
#another method is to use break
print("lets skip")

for i in range(0,20,2):
    if i == 16:
        break #means stop the loop. go no further.
    print("even numbers up to 16",i)

#something interesting
word = "programming"
vowels = ['a','e','i','o','u'] #this is a list of letters. list is written in square bracket

for letter in word:
    if letter in vowels:
        print("i am a vowel",letter)

value = 2
for x in range(1,25):
    print("value raise to the power of x is",value**x)
    print(f"value raised to the power of x is {value**x}") #f-string method
    print("{} raised to the power of {} is {}".format(value,x,value**x)) #format method



"""
Ask a user for a value and the user's favourite word
then cheer the word by the number of times
"""
favourite_number = int(input("whats your fav number?")) #input function always collect string values
#we can type cast it to integer by adding int
fav_word = input ("whats your fav word?")
counter = 0
while counter < favourite_number:
    print(fav_word)
    counter += 1
