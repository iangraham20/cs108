''' This program implements zeller's congruence as an algorithm to calculate the day of the week
Created September 29, 2016
Lab 04 Exercise 4.2
@author: Ian Christensen (igc2)
@author: Griffin Sparling (grs4)
'''

# assign variables
q = int(input('Please enter a day of the month: '))
m = int(input('Please enter the month: '))
year = int(input('Please enter the year'))
if m == 1:
    m = 13
    year = year - 1
if m == 2:
    m = 14
    year = year - 1
J = (year // 100)
K = (year % 100)
 
# solve for h
h = (q + ((( m + 1 ) * 26) // 10) + K + (K // 4) + (J // 4) + 5 * J) % 7

# create list for the days of the week
days_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# print results
print(days_week[h])