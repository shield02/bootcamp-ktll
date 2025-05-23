"""
Write a program that allows a teacher to enter exam marks.
Valid marks are decimal numbers in the range of 0-100. The program 
    should terminate when the teacher enters '999' and display the 
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
# input("Enter marks: ")
total_score = 0
counter = 1
while True:
    try:
        score = int(input("Enter mark(0-100) 999 to quit: "))
    except ValueError:
        print("Not a number")
        continue

    if score >= 0 and score <= 100:
        total_score += score
        counter += 1
    else:
        counter -= 1
        print (f"Number outside the range 0-100 inclusive")
        break

average_score = total_score/counter
print(f"Average marks: {average_score}")
