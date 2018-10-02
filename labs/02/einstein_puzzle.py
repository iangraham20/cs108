'''
einstein_puzzle.py simulates the albert einstein puzzle
Calvin College, Computer Science 108, Lab 02, Exercise 02
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''

number = int(input("Type a three digit number where the first and last digits differ by at least two"))

digit1 = (number//100)
digit2 = (number//10)%10
digit3 = (number//1)%10
rev_number = (digit3*100+digit2*10+digit1)
difference = abs(number-rev_number)
digit1 = (difference//100)
digit2 = (difference//10)%10
digit3 = (difference//1)%10
rev_diff = (digit3*100+digit2*10+digit1)
print(difference+rev_diff)
