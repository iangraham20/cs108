'''
This program prompts a user for four coordinates and draws a line between the two points
Created September 22, 2016
Lab 03 Exercise 3.4
@author: Ian Christensen (igc2)
'''

import turtle
import math

window = turtle.Screen()
Hope = turtle.Turtle()
Hope.hideturtle()

#prompt the user for the coordinates
x1 = int(input('Please enter 1st x-coordinate'))
x2 = int(input('Please enter 2nd x-coordinate'))
y1 = int(input('Please enter 1st y-coordinate'))
y2 = int(input('Please enter 2nd y-coordinate'))

#assign the coordinates to points
point1 = (x1, y1)
point2 = (x2, y2)

#draw the line between the points
Hope.goto(point1)
Hope.write('p1'+str(point1), font=('Arial', 20, 'italic'))
Hope.pendown()
Hope.goto(point2)
Hope.penup()
Hope.write('p2'+str(point2), font=('Arial', 20, 'italic'))

window.exitonclick()
