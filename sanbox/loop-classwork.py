#classwork

"""
write a while loop that prints only even numbers between 1 and 20
"""

counter = 1
while counter <= 20:
    if counter % 2 == 0:
        print("even number", counter)
    counter += 1

"""
Write a while loop that prints all odd numbers between 
1 and 50"""

print("---------------")
a = 1
while a <= 50:
    if a % 2 == 1:
        print("odd number", a)
    a += 1