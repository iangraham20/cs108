''' A program that converts content from a text file into rectangle objects.
November 7, 2016
Homework 9 Exercise 9.3
@author Ian Christensen (igc2) '''

# Import necessary libraries.
from rectangle import Rectangle

rectangles = []

# Open the text file, and save each line to a list as rectangle objects.
try:
    with open('rectangles.txt', 'r') as file:
        for line in file:
            try:
                temp = line.split()
                rectangles.append(Rectangle((int(temp[0]), int(temp[1])), int(temp[2]), int(temp[3]), temp[4]))
            except Exception as e:
                print(e)
except FileNotFoundError:
    print('Please enter a valid filename.')