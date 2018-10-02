''' A program that contains a class that represents a rectangle object.
November 7, 2016
Homework 9 Exercise 9.3
@author Ian Christensen (igc2) '''

# Import necessary libraries.
import turtle

# Create rectangle class that includes a constructor method, printing method, accessor methods, mutator methods, overlap method, and render method.
class Rectangle:
    ''' A class that represents a rectangle object.
    Invariants: width >= 0 and height >= 0 '''

    def __init__(self, coordinates = (0,0), width = 50, height = 50, color = 'black'):
        ''' The Constructor Method names the variables appropriately if the rectangle is valid. '''
        
        if str(coordinates[0]).isalpha():
            raise TypeError('Please enter a numeric character for the x coordinate.')
        
        if str(coordinates[1]).isalpha():
            raise TypeError('Please enter a numeric character for the y coordinate.')
        
        if str(width).isdigit() == False:
            raise ValueError('Please enter a numeric character for the width.')
        
        if str(height).isdigit() == False:
            raise ValueError('Please enter a numeric character for the height.')
        
        if str(color).isdigit():
            raise TypeError('Please enter an alpha character for the color.')
        
        if not self._invariant(width, height):
            raise ValueError('Please enter a numeric value greater than zero.')
        
        else:
            self._coordinates = coordinates
            self._height = height
            self._width = width
            self._color = color
    
    def __str__(self):
        ''' The Format Method allows for readable printing of the variables in the class. '''
        return 'Coordinates: {0}\nWidth: {1}\nHeight: {2}\nColor: {3}'.format(self._coordinates, self._width, self._height, self._color)

    def get_coordinates(self):
        ''' The Accessor Method that finds the coordinates of the rectangle. '''
        return self._coordinates

    def get_height(self):
        ''' The Accessor Method that finds the height of the rectangle. '''
        return self._height
    
    def get_width(self):
        ''' The Accessor Method that finds the width of the rectangle. '''
        return self._width

    def get_color(self):
        ''' The Accessor Method that finds the color of the rectangle. '''
        return self._color

    def get_area(self):
        ''' The Accessor Method that finds the area of the rectangle. '''
        return self._width * self._height
    
    def get_perimeter(self):
        ''' The Accessor Method that finds the perimeter of the rectangle. '''
        return (self._width + self._height) * 2
    
    def modify_width(self, delta = 0.0):
        ''' The Mutator Method that changes the width of the rectangle. '''
        new_width = self._width + delta
        if self._invariant(new_width, self._height):
            self._width = new_width
        else:
            raise ValueError('Please enter a value greater than zero.')
            
    
    def modify_height(self, delta = 0.0):
        ''' The Mutator Method that changes the height of the rectangle. '''
        new_height = self._height + delta
        if self._invariant(self._width, new_height):
            self._height = new_height
        else:
            raise ValueError('Please enter a value greater than zero.')
    
    def overlaps(self, rectangle2):
        ''' The Comparator Method that checks if two rectangles overlap. '''
        c1 = self.get_coordinates()
        x1 = c1[0]
        y1 = c1[1]
        c2 = rectangle2.get_coordinates()
        x2 = c2[0]
        y2 = c2[1]
        h1 = self.get_height()
        h2 = rectangle2.get_height()
        w1 = self.get_width()
        w2 = rectangle2.get_width()
        
        if y1 >= y2 and (y2 + h1) >= y1 and x1 >= x2 and x1 <= (x2 + w2):
            return True
        elif y1 >= y2 and (y2 + h1) >= y1 and x2 >= x1 and x2 <= (x1 + w1):
            return True
        elif y2 >= y1 and (y1 + h2) >= y2 and x1 >= x2 and x1 <= (x2 + w2):
            return True
        elif y2 >= y1 and (y1 + h2) >= y2 and x2 >= x1 and x2 <= (x1 + w1):
            return True
        else:
            return False

    def render(self, turtle_name):
        ''' The Render Method uses turtle graphics to draw the rectangle. '''
        turtle_name.pencolor(self._color)
        
        # Draw rectangle.
        turtle_name.showturtle()
        turtle_name.penup()
        turtle_name.goto(self._coordinates)
        turtle_name.setheading(0)
        turtle_name.pendown()
        turtle_name.forward(self._width)
        turtle_name.right(90)
        turtle_name.forward(self._height)
        turtle_name.right(90)
        turtle_name.forward(self._width)
        turtle_name.right(90)
        turtle_name.forward(self._height)
        turtle_name.penup()
        turtle_name.hideturtle()

    
    
    def _invariant(self, width, height):
        ''' The Validation Method tests for violation of invariants and returns a boolean expression. '''
        return width >= 0 and height >= 0

if __name__ == '__main__':
    ''' Perform tests if run in the program itself. '''
    
    try:
        Rectangle(('x', 0), 5, 5, 'black')
        assert False
    except TypeError as te:
        print(te)
        pass
    
    try:
        Rectangle((0, 'y'), 5, 5, 'black')
        assert False
    except TypeError as te:
        print(te)
        pass
    
    try:
        Rectangle((0, 0), 'five', 5, 'black')
        assert False
    except ValueError as ve:
        print(ve)
        pass
    
    try:
        Rectangle((0, 0), 5, 'five', 'black')
        assert False
    except ValueError as ve:
        print(ve)
        pass
    
    try:
        Rectangle((0, 0), 5, 5, 0)
        assert False
    except TypeError as te:
        print(te)
        pass
    
    try:
        Rectangle((-1, -1), -5, -5, 'black')
        assert False
    except ValueError as ve:
        print(ve)
        pass