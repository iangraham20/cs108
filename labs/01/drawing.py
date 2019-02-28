'''
drawing.py implements two possible turtle drawings
Calvin College, Computer Science 108, Lab 01
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''


import turtle
import sys

LENGTH = 50
DEGREE = 90

window = turtle.Screen()
turtle = turtle.Turtle()

def acronym():
	turtle.pendown()
	turtle.left(DEGREE * 2)
	turtle.forward(LENGTH)
	turtle.left(DEGREE)
	turtle.forward(LENGTH * 2)
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

def star():
	turtle.pendown()
	for x in range(0, 5):
		turtle.forward(LENGTH * 2)
		turtle.right(DEGREE * 1.6)
	turtle.penup()
	window.exitonclick()

def stickFigure():
	turtle.circle(LENGTH)
	turtle.right(DEGREE)
	turtle.forward(LENGTH * 4)
	turtle.left(DEGREE / 2)
	turtle.forward(LENGTH * 2.5)
	turtle.penup()
	turtle.left(DEGREE * 2)
	turtle.forward(LENGTH * 2.5)
	turtle.left(DEGREE)
	turtle.pendown()
	turtle.forward(LENGTH * 2.5)
	turtle.penup()
	turtle.left(DEGREE * 2)
	turtle.forward(LENGTH * 2.5)
	turtle.left(DEGREE / 2)
	turtle.forward(LENGTH * 2)
	turtle.right(DEGREE)
	turtle.forward(LENGTH * 2)
	turtle.right(DEGREE * 2)
	turtle.pendown()
	turtle.forward(LENGTH * 4)
	turtle.penup()
	turtle.forward(LENGTH * 2)
	window.exitonclick()

if __name__ == '__main__':
	selection = input("Hello,\nPlease select an option:\n0. exit\n1. acronym\n2. star\n3. stick figure\n")
	if selection == 0:
		sys.exit()
	elif selection == 1:
		acronym()
	elif selection == 2:
		star()
	elif selection == 3:
		stickFigure()
	else:
		print "Invalid input"
