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