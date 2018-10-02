''' bounce.py uses turtle graphics to create a screen saver
Created October 12, 2016
Homework 05 Exercise 5.6
@author: Ian Christensen (igc2)
'''

# import libraries
import turtle
import random

# create window and modify turtle
window = turtle.Screen()
window.setup(500, 500)
ball = turtle.Turtle()
ball.shape('circle')
ball.setheading(random.randint(0,360))

# create a loop that allows the ball to bounce off the walls 
while True:
    xcor = ball.xcor()
    ycor = ball.ycor()
    heading = ball.heading()
    if xcor < -225  or xcor > 225:
        ball.setheading(180 - heading)
    if ycor < -225  or ycor > 225:
        ball.setheading(-ball.heading())
    ball.forward(10)  
  
# keep the window open until it is closed by the user
window.exitonclick()