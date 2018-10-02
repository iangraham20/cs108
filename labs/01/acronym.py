'''
acronym.py draws the acronym for computer science
Calvin College, Computer Science 108, Lab 01, Exercise 03
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''

import turtle

window = turtle.Screen()
turtle = turtle.Turtle()

LENGTH = 50
DEGREE = 90

turtle.pendown()
turtle.left(DEGREE*2)
turtle.forward(LENGTH)
turtle.left(DEGREE)
turtle.forward(LENGTH*2)
turtle.left(DEGREE)
turtle.forward(LENGTH)
turtle.penup()
turtle.forward(LENGTH)
turtle.pendown()
turtle.forward(LENGTH)
turtle.left(DEGREE)
turtle.forward(LENGTH)
turtle.left(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.right(DEGREE)
turtle.forward(LENGTH)
turtle.penup()

window.exitonclick()
