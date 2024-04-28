colours = ["yellow", "read", "orange", "purple", "green"]
print(colours)

colours[1] = "red"
print(colours)




def unique_list(my_list):
    unique = []
    for x in my_list:
        if x not in unique:
            unique.append(x)

my_list = [1, 2, 3, 3, 4, 5, 5, 6]
print(my_list)


def say_hi():
    print("HI")


say_hi()
          

def say_hello():
    return 'Hello'


greeting = say_hello
print(greeting)


def square_of_7():
    return 7 ** 2
    

result = square_of_7()
print(result)


def generate_evens():
    result = []
    for i in range(1, 50):
        if i % 2 == 0:
            result.append(i)
    return result


def speak(animal):
    if animal == ("") or animal == "dog":
        return "woof"
    elif animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    else:
        return "?"
    

print(speak(""))


def product(num1, num2):
    return (num1 * num2)


print(product(2, 2))
print(product(2, -2))


# write a function called last_element. this function takes in one parameter 
# (a list) and returns the last value in the list. 
# it should return None if list is empty


numbers = [1, 2, 3]


def last_element(numbers):
    if numbers:
        return numbers[-1]
    return None


last = last_element(numbers)

print(last)


num1 = 3
num2 = 8


def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"
    else:
        return "Numbers are equal"


print(number_compare(num1, num2))


word = "bananas"
letter = "a"


def single_letter_count(word, letter):
    return word.upper().count(letter.upper())


print(single_letter_count(word, letter))


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = float(0)

for donation in donations.values():
    total_donations += donation
    

print(total_donations)



from random import choice 
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) 


bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"We have {bakery_stock[food]} left")
else:
    print("We don't make that")





