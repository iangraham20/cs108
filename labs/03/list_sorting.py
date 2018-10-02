'''
This program prompts user for four numbers and orders them in a list from min to max
Created September 22, 2016
Lab 03 Exercise 3.2
@author: Ian Christensen (igc2)
@author: Kenneth Horjus (kjh48)
'''

#prompt user and assign integers to a variable

num_1 = int(input('Please enter number 1'))
num_2 = int(input('Please enter number 2'))
num_3 = int(input('PLease enter number 3'))
num_4 = int(input('Please enter number 4'))

#create list
list = [num_1, num_2, num_3, num_4]

#create second list and transfer values
list_2 = []
list_2.append(min(list))
list.remove(min(list))
list_2.append(min(list))
list.remove(min(list))
list_2.append(min(list))
list.remove(min(list))
list_2.append(min(list))
list.remove(min(list))

#print the ordered values
print('Your numbers from minimum to maximum are:', list_2)
