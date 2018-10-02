'''
This program is a computer generated game of rock, paper, scissors
Created September 29, 2016
Lab 04 Exercise 4.3
@author: Ian Christensen (igc2)
'''

# import randomizer
from random import randint

# assign variables
rock = 0
paper = 1
scissors = 2
user_choice = int(input('Please enter 0 for rock, 1 for paper, 2 for scissors: '))
computer_choice = randint(0, 2)

# print computer_choice
print('The computer chose:', computer_choice)

# determine outcome given a user input of 0
if user_choice == 0:
    if computer_choice == 1:
        print('Computer wins!')
    elif computer_choice == 2:
        print('You win!')
    else:
        print('It is a draw!')

# determine outcome given a user input of 1
if user_choice == 1:
    if computer_choice == 2:
        print('Computer wins!')
    elif computer_choice == 0:
        print('You win!')
    else:
        print('It is a draw!')

# determine outcome given a user input of 2
if user_choice == 2:
    if computer_choice == 0:
        print('Computer wins!')
    elif computer_choice == 1:
        print('You win!')
    else:
        print('It is a draw!')
