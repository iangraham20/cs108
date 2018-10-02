'''
This program draws the Japanese flag using turtle graphics.
Created September 20, 2016
Homework 02 Exercise 01
@author: Ian Christensen (igc2)
'''

# improt tutles and create window
import turtle
window = turtle.Screen()

# variables
flag_length = 150
flag_height = (flag_length * 2) / 3
flag_symbol = (flag_height * 3) / 10

# give the turtle a Japanese name.
haruto = turtle.Turtle()

# move haruto to the top right of the flag
haruto.penup()
haruto.right(180)
haruto.forward(flag_length / 2)
haruto.right(90)
haruto.forward(flag_height / 2)
haruto.right(90)
haruto.pendown()

# draw the flag border and fill
haruto.color('black', 'white')
haruto.begin_fill()
haruto.forward(flag_length)
haruto.right(90)
haruto.forward(flag_height)
haruto.right(90)
haruto.forward(flag_length)
haruto.right(90)
haruto.forward(flag_height)
haruto.end_fill()
haruto.penup()

# move haruto to the center of the flag's length and 1/5 from the top
haruto.right(90)
haruto.forward(flag_length / 2)
haruto.right(90)
haruto.forward(flag_height / 5)
haruto.right(90)

# draw the sun symbol in the center of the flag
haruto.color('#C70025', '#C70025')
haruto.pendown()
haruto.begin_fill()
haruto.circle(flag_symbol)
haruto.end_fill()
haruto.penup()

window.exitonclick()
