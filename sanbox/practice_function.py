'''
Write a function called return day. This function takes in one parameter
(a number from 1 to 7) and returns the day of the week(1 is Sunday,2 is Monday,
3 is Tuesday, etc). If the number is less than 1 or greater than 7, the 
function should return None. HINT: Store the days of the week in a list or 
dictionary using numbers as key 
'''


# Solution
def return_day(num):
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if num >= 0 and num < len(week_days):
        return week_days[num]
    else:
        return None


print(return_day(2))


# Using a dictionary
def retourn_day(nom):
    days_of_week = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    if nom > 0 and nom <= len(days_of_week):
        return days_of_week[nom]
    else:
        return None
    

print(retourn_day(3))
print(retourn_day(6))
print(retourn_day(9))





