''' Model of a sun.
Created Fall 2014
Lab 10 Exercise 3
@author: smn4
@author: Ian Christensen (igc2) '''

import turtle

class Sun:
    
    def __init__(self, name, rad, m, temp):
        self._name = name
        if rad <= 0 or m <= 0:
            raise ValueError('Sun numeric demension properties must be positive')
        else:
            self._radius = rad
            self._mass = m
        if temp <= -273.15:
            raise ValueError('Temperature numeric properties must be above absolute zero.')
        else:
            self._temp = temp
        
        self._x = 0
        self._y = 0
        self._turtle = turtle.Turtle()
        
        # Draw turtle graphic.
        self._turtle.penup()
        self._turtle.color('orange')
        self._turtle.shape('circle')
        self._turtle.shapesize(self._radius, self._radius)
        self._turtle.goto(self._x, self._y)
        
    def get_mass(self):
        return self._mass
    
    def __str__(self):
        return self._name

if __name__ == '__main__':
    window = turtle.Screen()
    
    Sun('Sun', .75, .75, -270)
    Sun('Sun', .25, .25, 1000)
    try:
        Sun('Sun', -1000, 1000, 1000)
        assert False
    except ValueError:
        pass
    try:
        Sun('Sun', 1000, -1000, 1000)
        assert False
    except ValueError:
        pass
    try:
        Sun('Sun', 1000, 1000, -1000)
        assert False
    except ValueError:
        pass
    
    #Keep the window open until it is clicked
    window.exitonclick() 