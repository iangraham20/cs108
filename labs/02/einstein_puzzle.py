'''
einstein_puzzle.py simulates the albert einstein puzzle
Calvin College, Computer Science 108
Author: Ian Christensen
Email: igc2@students.calvin.edu
Date: Fall, 2016
'''

def einsteinPuzzle():
	# Give the initial message and prompt
	print "The person administering this test should write a number down on a piece of paper and then have you follow the instructions.\n"
	abc = int(input("Type a three digit number where the first and last digits differ by at least two:\n"))

	# Find each seperate digit of the original number
	a = (abc // 100)
	b = (abc // 10) % 10
	c = (abc // 1) % 10

	# Reassemble the number in reverse
	cba = (100 * c) + (10 * b) + (1 * a)

	# Calculate the difference of the original number and it's reverse value
	difference = abs(abc - cba)

	# Find each seperate digit of the solution
	a = difference // 100
	b = difference // 10 % 10
	c = difference // 1 % 10

	# Reassemble the number in reverse
	reversedDifference = c * 100 + b * 10 + a

	# Calculate the sum of the solution and it's reverse value
	solution = difference + reversedDifference

	# Output the solution
	print "\nThe original number is equal to: " + str(abc)
	print "\nThe reversed number is equal to: " + str(cba)
	print "\nThe difference of " + str(abc) + " and " + str(cba) + " is equal to: " + str(difference)
	print "\nThe reversed difference is equal to " + str(reversedDifference)
	print "\nThe sum of " + str(difference) + " and " + str(reversedDifference) + " is equal to: " + str(solution)

if __name__ == '__main__':
	einsteinPuzzle()
