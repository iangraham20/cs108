''' Model of a planet.
Created Fall 2014
Lab 10 Exercise 2
@author: smn4
@author: Ian Christensen (igc2) '''

import turtle

class Planet:
    
    def __init__(self, name, rad, m, dist, color):
        if rad <= 0 or m <= 0 or dist <= 0:
            raise ValueError('Planet numeric properties must be positive')
        else:
            self._radius = rad
            self._mass = m
            self._distance = dist
            
        self._x = dist
        self._y = 0
        self._color = color
        self._name = name
        self._turtle = turtle.Turtle()
        
        # Draw turtle graphic.
        self._turtle.penup()
        self._turtle.color(self._color)
        self._turtle.shape('circle')
        self._turtle.shapesize(self._radius, self._radius)
        self._turtle.goto(self._x, self._y)
            
    def get_name(self):
        return self._name
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass
    
    def get_distance(self):
        return self._distance
    
    def set_name(self, newname):
        self._name = newname
    
    def __str__(self):
        return self._name

if __name__ == '__main__':
    window = turtle.Screen()

    Planet('Earth', .5, .5, .5, 'blue')
    Planet('Mars', .5, .5, .5, 'red')
    try:
        Planet('Jupiter', -1000, -1000, -1000, 'orange')
        assert False
    except ValueError:
        pass
    try:
        Planet('Mercury', -1000, 1000, 1000, 'brown')
        assert False
    except ValueError:
        pass
    try:
        Planet('Venus', 1000, -1000, 1000, 'grey')
        assert False
    except ValueError:
        pass
    try:
        Planet('Neptune', 1000, 1000, -1000, 'blue')
        assert False
    except ValueError:
        pass
    #Keep the window open until it is clicked
    window.exitonclick()      