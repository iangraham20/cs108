''' This program tests varying try blocks.
Created on Nov 10, 2016
Lab 10 Exercise 1
@author: Ian Christensen (igc2) '''

try:
    import happiness
except ImportError as ie:
    print('ImportError occurred:', ie)

try:
    'hi' + 4
except TypeError as te:
    print('TypeError occurred:', te)

try:
    10 / 0
except ZeroDivisionError as zde:
    print('ZeroDivisionError occurred:', zde)

try:
    'person'.find_first('e')
except AttributeError as ae:
    print('AttributeError occurred:', ae)

try:
    [0,1,2]['summer']
except TypeError as te:
    print('TypeError occurred:', te)

try:
    ['hi','there','student'][5]
except IndexError as xe:
    print('IndexError occurred:', xe)

try:
    print(name)
except NameError as ne:
    print('NameError occurred:', ne)

try:
    9 <= (3, 4)
except TypeError as te:
    print('TypeError occurred:', te)

try:
    f = open('missingFile.txt')
except FileNotFoundError as fnfe:
    print('FileNotFoundError:', fnfe)