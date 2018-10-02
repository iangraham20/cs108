'''
A program that creates user names for users
Created September 22, 2016
Lab 03 Exercise 3.1
@author: Ian Christensen (igc2)
'''

first_name = input('Insert fist name')
last_name = input('Insert last name')
student_num = input('Insert student number')
print(first_name[0:2]+last_name[0:5]+student_num[-2:])
