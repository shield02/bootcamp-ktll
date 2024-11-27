#The previous assignment no. 1
def name_of_country():
    country = "Switzerland"
    return country  + " is a beautiful place"
print(name_of_country())

#Assignment II
#1
def bio_data(name, age, hobby):
    new_name = "Vlad"
    new_age = 70
    new_hobby = "Judo"
    all_data = f"My name is {new_name}, I'm {new_age} years old, I love to play {new_hobby}."
    return all_data
print(bio_data("Vlad", 70, "Judo"))

#2
def two_numbers(num1, num2):
    first_new = 1 * 6
    second_new = 2 % 2
    third_new = first_new + second_new
    return third_new
print(two_numbers(1 * 6, 2 % 2))
