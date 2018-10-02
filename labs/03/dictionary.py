'''
This program is use to manage scores of students using dictionaries
Created September 22, 2016
Lab 03 Exercise 3.3
@author: Ian Christensen (igc2)
'''

# create dictionary
scoreDict = dict()
scoreDict.update({'Joe': 10, 'Tom': 23, 'Barb': 13, 'Sue': 19, 'Sally': 12})

# change sally's score
scoreDict['Sally'] = 13

# remove tom from the class
del scoreDict['Tom']

# print results
print(scoreDict)
