'''
This program will use turtle graphics to create the Calvin Computing Club Abstraction.
Created September 14, 2016
Homework 01, Exercise 1.3
@author: Ian Christensen (igc2)
'''

# Access code named "turtle".
import turtle

# Name the turtle screen "window"
window = turtle.Screen()

# Create a turtle and name it larry.
larry = turtle.Turtle()

# Change color and size of pen.
larry.pencolor('red')
larry.pensize(15)

# Set variables.
length = 150
length_two = int(length / 3)
length_three = int(length / 6)

# Begin drawing the red triangle.
larry.pendown()
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.penup()
# The red triangle is complete.

# Move to the start point of the green triangle and change color of pen to green.
larry.right(90)
larry.forward(length_two)
larry.left(90)
larry.pencolor('#39FF14')

# Begin drawing the green triangle.
larry.pendown()
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.penup()
# The green triangle is complete.

# Move to the start point of the blue triangle and change color of pen to blue.
larry.forward(length_two)
larry.left(90)
larry.forward(length_three)
larry.right(90)
larry.pencolor('blue')

# Begin drawing the blue triangle.
larry.pendown()
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.forward(length)
larry.left(120)
larry.penup()
# The blue triangle is complete.

# Keep the window open until user exits manually.
window.exitonclick()
