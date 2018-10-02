''' A program that writes hard coded content to the rectangles.text file.
November 7, 2016
Homework 9 Exercise 9.3
@author Ian Christensen (igc2) '''

with open('rectangles.txt', 'w') as txt_file:
    txt_file.write('0 0 100 50 black\n')
    txt_file.write('100 0 10 50 gold\n')
    txt_file.write('130 20 20 50 blue\n')
    txt_file.write('100 -50 20 15 orange\n')
    txt_file.write('-25 -50 75 85 purple')