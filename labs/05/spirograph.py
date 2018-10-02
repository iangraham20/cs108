''' spirograph.py allows a user to create multiple overlapping spirographs
Created October 3, 2016
Lab 05 Exercise 5.2 a, b, c
@author: Ian Christensen (igc2)
@author: Griffin Sparling (grs4)
'''

# import necessary libraries
import turtle
import math

# create window and name turtle
window = turtle.Screen()
barf = turtle.Turtle()

# create loop that allows user to overlap multiple spirographs
while True:
    choice = input('Would you like to draw a spirograph? (Y/n): ')
    if choice == 'n' or choice == 'N':
        break
    elif choice == 'y' or choice == 'Y' or choice == '':
    
        # assign variables
        mov_rad = float(input('Please enter the moving radius: '))
        fix_rad = float(input('Please enter the fixed radius: '))
        pen_offset = float(input('Please enter the pen offset: '))
        color = str(input('Please enter color: '))
        
        # use parametric equation
        time = 0.0
        x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
        y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)
        
        # setup turtle
        barf.penup()
        barf.goto(x, y)
        barf.pendown()
        barf.color(color)
        
        # draw spirograph
        while time < 100:
            x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
            y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)
            time += 0.1
            barf.goto(x, y)
    
    else:
        print('Enter n, N, y, or Y')
        continue

# keep the window open until it is closed by the user
window.exitonclick()