def multiply_firstname_by_3(firstname):
    result = firstname * 3
    return result

result = multiply_firstname_by_3("ima")
print(result)

def greet_specific_me(name, age, state):
    return f"Hello {name} you are {age} years old, You come from {state}. Welcome here"

print(greet_specific_me("Purple", 98, "Mecury"))
print(greet_specific_me("White", 128, "Pluto"))
print(greet_specific_me("Green", 10, "Jupiter"))
