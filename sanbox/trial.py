'''
Print out the prime numbers between 100 and 200
Using while loop
Using for loop
'''
# Using for loop
for n in range(100,201):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n)

# Using for loop
number = 100
while number <= 200:
    if number % 2 == 0:
