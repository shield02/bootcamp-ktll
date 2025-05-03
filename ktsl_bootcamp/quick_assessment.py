"""
Write a program that allows a teacher to enter exam marks.
Valid marks a decimal numbers in the range of 0-100. The program 
    should terminate when the teacher emters '999' and display the 
    average mark for the class, rounded to one decimal place.

Additional Rules To Handle:
    If the entered mark is a numeric value but outside the range of 0-100, 
        display an error message 'Number outside the range 0-100 inclusive', 
        ignore the entry, and proceed to the next input.
    If the entered mark is not a numeric value, display a message 
        stating "Not a number", ignore the entry, and proceed to the next input.
    If '999' is entered as before the first valid input, display a 
        message saying 'No results entered'.
"""
input("Enter marks: ")
