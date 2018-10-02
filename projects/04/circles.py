''' circles.py takes user input to create two circles and determine the relation between them
Created October 3, 2016
Homework 04 Exercise 4.1
@author: Ian Christensen (igc2)
'''

# import necessary libraries
import turtle

# create window and name turtle
window = turtle.Screen()
tom = turtle.Turtle()

# assign variables for the first circle
x1_coordinate = int(input('Please enter the x-coordinate for the center of the first circle: '))
y1_coordinate = int(input('Please enter the y-coordinate for the center of the first circle: '))
radius_1 = int(input('Please enter the radius of the first circle: '))

# assign variables for the second circle
x2_coordinate = int(input('Please enter the x-coordinate for the center of the second circle: '))
y2_coordinate = int(input('Please enter the y-coordinate for the center of the second circle: '))
radius_2 = int(input('Please enter the radius of the second circle: '))

# create data structures
center_1 = (x1_coordinate, y1_coordinate)
center_2 = (x2_coordinate, y2_coordinate)

# draw first circle
tom.penup()
tom.goto(center_1)
tom.right(90)
tom.forward(radius_1)
tom.left(90)
tom.pendown()
tom.circle(radius_1)
tom.penup()

# draw second circle
tom.penup()
tom.goto(center_2)
tom.right(90)
tom.forward(radius_2)
tom.left(90)
tom.pendown()
tom.circle(radius_2)
tom.penup()

# assign variables necessary for the if statements
tom.goto(center_2)
dist_center = tom.distance(center_1)
radii = radius_1 + radius_2

# use if statements to determine the relation between the two circles
if dist_center + radius_2 < radius_1 or dist_center + radius_1 < radius_2:
    tom.write('Circle 1 contains circle 2', font=('Arial', 12, 'normal'))
elif dist_center <= radii:
    tom.write('Circle 1 and circle 2 overlap', font=('Arial', 12, 'normal'))
else:
    tom.write('Circles are disjoint', font=('Arial', 12, 'normal'))

# keep the window open until it is closed by the user
window.exitonclick()