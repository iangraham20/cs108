'''
This program uses turtle graphics to create triangles with user input coordinates
Created September 27, 2016
Homework 03 Exercise 3.2
@author: Ian Christensen (igc2)
'''

# import necessary libraries
import turtle
import math

# assign variables
x1 = int(input('Please enter first x-coordinate'))
x2 = int(input('Please Enter second x-coordinate'))
x3 = int(input('Please Enter third x-coordinate'))
y1 = int(0)
y2 = int(0)
y3 = int(input('Please Enter third y-coordinate'))

# create data structures
tup1 = (x1, y1)
tup2 = (x2, y2)
tup3 = (x3, y3)
tup4 = (x3, y1)
list1 = [tup1, tup2, tup3]

# find the lengths of each side
side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
side3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
side4 = math.sqrt((x3 - x3)**2 + (y1 - y3)**2)

# assign perimeter and area to variables
perimeter = (side1 + side2 + side3)
area = (side1 * side4) / 2

# create window and name turtle
window = turtle.Screen()
joe = turtle.Turtle()

# draw triangle and perpendicular line
joe.penup()
joe.goto(tup3)
joe.pendown()
joe.goto(tup1)
joe.goto(tup2)
joe.goto(tup3)
joe.goto(tup4)
joe.penup()

# move to top left of window and write points, perimeter, and area
joe.goto(-250, 250)
joe.write('Points: '+str(list1), font=('Arial', 12, 'normal'))
joe.goto(-250, 230)
joe.write('Perimeter: '+str(perimeter)+' pixels', font=('Arial', 12, 'normal'))
joe.goto(-250, 210)
joe.write('Area: '+str(area)+' pixels squared', font=('Arial', 12, 'normal'))

# close window when clicked on
window.exitonclick()
