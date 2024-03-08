# Accessing the elements of a string
'''
# String Indexing
....................................
String Indexing has to do with accessing the individual letters that make up
 a string using  their corresponding indexes.

In python, index starts fron zero. That measn that the first 
letter of a string has index number zero(0)
The index must be an integer. You cannot use a float as an index
Pythin will throw an error called TypeError
You can also use negative integers as index.
'''

sentence = "a quick brown fox"
word = "python"

# we can retrieve the first letter from the variables
print(sentence[0]) #this will give us the first letter in sentence
print(word[1]) #this will give us the second letter in word
print(sentence[-1]) #this will give us the last letter

'''
#classwork
''''''''''''''''''''''''''''''''''''
Create a variable called fruit and assign your best fruit to it,
then retrieve the third letter of the fruit
'''
fruits = "Banana"
print(fruits[2])

'''
#String s;icing
String slicing has to do with using indexes to retrieve 
part of the lettes of a string.
In string slicing, you will need 3 values
  - start : index where you want to start extracting from
  - stop: index where you wan to stop plus 1
  - step: how many letters should be counted in succession
When you are doing string slicing, the last number should be one 
higher than the index of where you want to stop.
'''
statement = "python is a very interesting programming language"

# we want to extract only the word "python" from statement
print(statement[0:6]) #this has a step of 1
print(statement[0:6:2]) #this has step of 2
print(statement[-8:]) #this prints Language.
#when you leave out a stop value, python takes it to mean till the end
print(statement[:6])#this prints python
#when you leave out a start value, python takes it to mean from the beginning
print(statement[:]) # when you leave out both start and stop, it will give you a copy of the original string
print(statement[-8:-4])
#In using negatives, your stop value must be 1 value lesser than where you want to stop
print (statement[:8]) #this prints python i.
