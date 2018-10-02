''' A program that contains a class that represents a rectangle object.
October 31, 2016
Homework 8 Exercise 4
@author Ian Christensen (igc2) '''

# Import necessary libraries.
import sys
import turtle

# Create rectangle class that includes a constructor method, printing method, accessor methods, mutator methods, overlap method, and render method.
class rectangle:
    ''' A class that represents a rectangle object.
    Invariants: width > 0 and height > 0 '''

    def __init__(self, coordinates = (0,0), width = 50.0, height = 50.0, color = 'black'):
        ''' The Constructor Method names the variables appropriately if the rectangle is valid. '''
        if self._is_valid_rectangle(width, height):
            self._coordinates = coordinates
            self._height = height
            self._width = width
            self._color = color
        else:
            print('Invalid rectangle.')
            sys.exit(-1)
    
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
        if self._is_valid_rectangle(new_width, self._height):
            self._width = new_width
        else:
            print('Invalid rectangle.')
            sys.exit(-1)
            
    
    def modify_height(self, delta = 0.0):
        ''' The Mutator Method that changes the height of the rectangle. '''
        new_height = self._height + delta
        if self._is_valid_rectangle(self._width, new_height):
            self._height = new_height
        else:
            print('Invalid rectangle.')
            sys.exit(-1)
    
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

    def render(self, ian):
        ''' The Render Method uses turtle graphics to draw the rectangle. '''
        ian.pencolor(self._color)
        
        # Draw rectangle.
        ian.penup()
        ian.goto(self._coordinates)
        ian.setheading(0)
        ian.pendown()
        ian.forward(self._width)
        ian.right(90)
        ian.forward(self._height)
        ian.right(90)
        ian.forward(self._width)
        ian.right(90)
        ian.forward(self._height)
        ian.penup()
        ian.hideturtle()

    
    
    def _is_valid_rectangle(self, width, height):
        ''' The Validation Method tests for violation of invariants and returns a boolean expression. '''
        return width > 0 and height > 0

# Create window and name turtle.
window = turtle.Screen()
ian = turtle.Turtle()
default = rectangle()

# assert(default == 'Coordinates: (0, 0)\nWidth: 50\nHeight: 50\nColor: black')
assert(default.get_height() == 50)
assert(default.get_width() == 50)
assert(default.get_area() == 2500)
assert(default.get_perimeter() == 200)
default.modify_height(50)
default.modify_width(50)
assert(default.get_height() == 100)
assert(default.get_width() == 100)
assert(default.get_area() == 10000)
assert(default.get_perimeter() == 400)
# control
r1 = rectangle()
# overlaps left and top
r2 = rectangle((-10, 10), 50, 50, 'black')
# overlaps left and bottom
r3 = rectangle((-10, -10), 50, 50, 'black')
# overlaps right and bottom
r4 = rectangle((10, -10), 50, 50, 'black')
# overlaps right and top
r5 = rectangle((10, 10), 50, 50, 'black')
# overlaps top
r6 =  rectangle((25, 10), 10, 50, 'black')
# overlaps bottom
r7 =  rectangle((25, -10), 10, 50, 'black')
# overlaps left
r8 =  rectangle((25, -25), 50, 10, 'black')
# overlaps right
r9 =  rectangle((-25, -25), 50, 10, 'black')
# does not overlap
r10 = rectangle((100, 0), 50, 50, 'black')
assert(r1.overlaps(r2))
assert(r1.overlaps(r3))
assert(r1.overlaps(r4))
assert(r1.overlaps(r5))
assert(r1.overlaps(r6))
assert(r1.overlaps(r7))
assert(r1.overlaps(r8))
assert(r1.overlaps(r9))
assert(r1.overlaps(r10) == False)

# Renders default rectangle
r1.render(ian)

# Keep the window open until it is closed by the user.
window.exitonclick()