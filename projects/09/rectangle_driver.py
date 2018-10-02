''' A program that converts content from a text file into rectangle objects.
November 7, 2016
Homework 9 Exercise 9.3
@author Ian Christensen (igc2) '''

# Import necessary libraries.
import turtle
from rectangle import Rectangle

# Create window and name turtle.
window = turtle.Screen()
ian = turtle.Turtle()

rectangles = []

# Open the text file, and save each line to a list as rectangle objects.
with open('rectangles.txt', 'r') as file:
    for line in file:
        temp = line.split()
        rectangles.append(Rectangle((int(temp[0]), int(temp[1])), int(temp[2]), int(temp[3]), temp[4]))
    
for rect in rectangles:
    rect.render(ian)

# Keep the window open until it is closed by the user.
window.exitonclick()