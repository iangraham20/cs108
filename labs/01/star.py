'''
star.py draws a star
Calvin College, Computer Science 108, Lab 01, Exercise 02
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''

import turtle

window = turtle.Screen()
turtle = turtle.Turtle()

DEGREE = 144
LENGTH = 100

turtle.pendown()
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.penup()

window.exitonclick()
