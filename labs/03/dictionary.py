'''
This program is use to manage scores of students using dictionaries
Created September 22, 2016
Lab 03 Exercise 3.3
@author: Ian Christensen (igc2)
'''

import sys

dictionary = dict()

if __name__ == '__main__':
	while True:
		selection = input("Please select an option:\n0. exit\n1. Add an element\n2. Remove an element\n3. Update an element\n4. View the value of a specific element\n")
		if selection == 0:
			break
			sys.exit()
		elif selection == 1:
			key = input("\nEnter a key value: ")
			element = raw_input("\nEnter a element value: ")
			dictionary[key] = element
		elif selection == 2:
			key = input("\nEnter the key value corresponding to the element you would like to delete: ")
			del dictionary[key]
		elif selection == 3:
			key = input("\nEnter the key value corresponding to the element you would like to update: ")
			element = raw_input("\nEnter the new element value: ")
			dictionary.update({ key: element })
		elif selection == 4:
			key = input("\nEnter the key value corresponding to the element you would like to view: ")
			print dictionary.get(key)
		else:
			print "Invalid input"
		print dictionary
