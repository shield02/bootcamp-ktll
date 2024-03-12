"""
#STRINGS#
'''''''''''''''''''''''''''''''''''''''''''''
A string is simply a sequence of characters enclosed
either in single quotes or double quotes

A string could be just about any alpha numeric character
"""
#Examples
'i am learning python' #string with a single quote
"I am learning python" #string with double quote

#when creating strings you have to be consistent with the opening and closing quote
#what is the difference between single and double quotes
#there is no difference except for a special case of the example below

'i'm hungry' '
#doesn't really work. 
#you can escape the inner single quote by typing / before it
'i/m hungry'
"i/m hungry" # this works perfectly

# We can concatenate (join) two string
first_name = "Itoro"
last_name = "Uduak"
full_name = first_name + " " + last_name
"Itoro" + "Uduak"
print(full_name)

#you can also multiply a string with an integer
hail_Emem_2x = "Emem" * 4
print(hail_Emem_2x)

#we can find the length of a string
print(len("Itoro"))
print(len("Itoro "))


#STRING FORMATTING
print("Itoro",uppercase()) 
print("Itoro",lower())

print("My name is " + first_name)
print("My name is " + first_name + ' ' + last_name)
print('My name is', first_name, last_name)
print('My name is {} {}'.format(first_name, last_name)) # {} is called a placeholder. This is using format function
# The first placeholder will be replaced by the first value of format() 
# and the second placeholder will be replaced by the second value of format()
print(f'My name is {first_name} {last_name}') # this is called the f-string method of formatting strings
