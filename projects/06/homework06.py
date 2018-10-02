''' A program that uses a definition to create a composite turtle graphic.
October 18, 2016
Homework 6 Exercise 6.3
@author Ian Christensen (igc2) '''

def smiley_face(coordinates, size):
    ''' Draws a smiley face using turtle graphics. '''
    
    # Import necessary library, create window, and name turtle.
    import turtle
    window = turtle.Screen()
    joe = turtle.Turtle()
    joe.width(size / 30)

    # Move to user coordinates and draw circle
    joe.penup()
    joe.goto(coordinates)
    joe.forward(-size)
    joe.pendown()
    joe.right(90)
    joe.color('black', 'yellow')
    joe.begin_fill()
    joe.circle(size, 360)
    joe.end_fill()
    
    # Move to and draw the mouth.
    joe.penup()
    joe.left(90)
    joe.forward(size / 2)
    joe.right(90)
    joe.forward(size / 4)
    joe.pendown()
    joe.circle(size / 2, 180)
    joe.penup()
    
    # Move to and draw the eyes.
    joe.left(90)
    joe.forward(size / 4)
    joe.right(90)
    joe.forward(size / 5)
    joe.pendown()
    joe.forward(size / 2)
    joe.penup()
    joe.left(90)
    joe.forward(size / 2)
    joe.left(90)
    joe.pendown()
    joe.forward(size / 2)
    joe.hideturtle()
    
    return
    # Keep the window open until it is closed by the user.
    window.exitonclick()

# Create variables for the test cases.
coordinates1 = (0, 0)
coordinates2 = (-200, 200)
coordinates3 = (200, -200)
coordinates4 = (-250, -250)
coordinates5 = (250, 250)
size1 = 50
size2 = 100
size3 = 150
size4 = 200
size5 = 250

# Create test case definition and call.
def smiley_test():
    smiley_face(coordinates1, size1)
    smiley_face(coordinates2, size2)
    smiley_face(coordinates3, size3)
    smiley_face(coordinates4, size4)
    smiley_face(coordinates5, size5)
smiley_test()