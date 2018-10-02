'''
This program draws a scalable stick figure
Calvin College, Computer Science 108, Lab 02, Exercise 03
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''

import turtle
import math

window = turtle.Screen()
turtle = turtle.Turtle()

LENGTH1 = 25
LENGTH2 = LENGTH1 * 2
LENGTH3 = LENGTH1 * 4
LENGTH4 = LENGTH1 * 2.5
DEGREE1 = 45
DEGREE2 = DEGREE1 * 2
DEGREE3 = DEGREE1 * 4

turtle.circle(LENGTH1)
turtle.right(DEGREE2)
turtle.forward(LENGTH3)
turtle.left(DEGREE1)
turtle.forward(LENGTH4)
turtle.penup()
turtle.right(DEGREE3)
turtle.forward(LENGTH4)
turtle.left(DEGREE2)
turtle.pendown()
turtle.forward(LENGTH4)
turtle.penup()
turtle.right(DEGREE3)
turtle.forward(LENGTH4)
turtle.left(DEGREE1)
turtle.forward(LENGTH2)
turtle.right(DEGREE2)
turtle.forward(LENGTH2)
turtle.right(DEGREE3)
turtle.pendown()
turtle.forward(LENGTH3)
turtle.penup()
turtle.forward(LENGTH2)

window.exitonclick()
