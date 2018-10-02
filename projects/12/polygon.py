'''
Model a single polygon
Created Fall 2016
homework12
@author Ian Christensen (igc2)
'''

from help import *

class Polygon:
    ''' This class represents a polygon object. '''
    
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 50, x3 = 40, y3 = 30, x4 = 10, y4 = 30, color = '#0000FF'):
        ''' This is the Constructor method for the Polygon class. '''
        
        self._x1 = x1
        self._y1 = y1
        
        self._x2 = x2
        self._y2 = y2
        
        self._x3 = x3
        self._y3 = y3
        
        self._x4 = x4
        self._y4 = y4
        
        self._color = color
        
    def render(self, canvas):
        ''' This render method allows the polygon object to be displayed on a screen. '''
        canvas.create_polygon(self._x1, self._y1, self._x2, self._y2, self._x3, self._y3, self._x4, self._y4, fill = self._color, outline='black')