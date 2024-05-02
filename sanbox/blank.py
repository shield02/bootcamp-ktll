file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts['csv'] = 13
print(file_counts)

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(key)

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(file_counts[key])

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for key in file_counts:
    print(key, ':', file_counts[key])

"""
Question #6
-------------------------------------------------------------------
Create a dictionary of at least 5 grocery items and their respective
prices as float data type.
Write a function that returns the total price of all the grocery
items in a dictionary. The function will take a dictionary as argument.
Use the dictionary you created above to run the function.
"""

# Solution
grocery = {'bread': 1000.55, 'chicken': 3566.95, 'eggs': 799.50, 'cereal': 433.42, 'pasta': 233.66}


def total_price(groceri):
    total = 0
    for k in groceri:
        total += groceri[k]
    return total


groceri = grocery 
print(total_price(groceri))

"""
Question #7
--------------------------------------------------------------------
Write a function that receives a dictionary which contains email domain
names as keys and a list of users as values and returns a list that contains
complete email address of all the users.
You can use this dictionary:
domain_users = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
                "yahoo.com": ["barbara.gordon", "jean.grey"], 
                "hotmail.com": ["bruce.wayne"]}
Example: your function should return a list with `clark.kent@gmail.com` as one
of the elements.
"""


# Solution
def complete_email_addresses(domain_users):
    email_addresses = []
    for domain, users in domain_users.items():
        for user in users:
            email_addresses.append(f'{user}@{domain}')
    return email_addresses
    
             
domain_users = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
                "yahoo.com": ["barbara.gordon", "jean.grey"], 
                "hotmail.com": ["bruce.wayne"]}        

print(complete_email_addresses(domain_users))

"""
Question #8
---------------------------------------------------------------------
Write a function that takes any string and returns a dictionary where
the keys are each letter present in a string and the values are how many
times each letter is present in the string.

Example: if the string `pyyyytthoonnn` is given to the function it will return
{'p': 1, 'y': 4, 't': 2, 'h': 1, 'o': 2, 'n': 3}
"""


# Solution
def count_letters(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


print(count_letters('pyyyytthoonnn'))


    
