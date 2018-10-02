''' A driver program that creates a solar system turtle graphic.
Created on Nov 10, 2016
Lab 10 Exercise 5
@author: Ian Christensen (igc2) '''

import turtle
from solar_system import *

window = turtle.Screen()
window.setworldcoordinates(-1, -1, 1, 1)
ian = turtle.Turtle()

ss = Solar_System() 
ss.add_sun(Sun("SUN", 8.5, 1000, 5800))
ss.add_planet(Planet("EARTH", .475, 5000, 0.6, 'blue'))
try:
    ss.add_planet(
        Planet(input('Please enter the name of the planet: '),
        float(input('Please enter the radius of the planet: ')),
        float(input('Please enter the mass of the planet: ')),
        float(input('Please enter the distance of the planet from the origin: ')),
        input('Please enter the color of the planet: ')))
except ValueError as ve:
    print('ValueError occurred:', ve)
except TypeError as te:
    print('TypeError occurred:', te)
except:
    print('Unknown Error')
#Keep the window open until it is clicked
window.exitonclick()                