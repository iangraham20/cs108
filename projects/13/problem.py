'''
This is the parent class of the quiz application.
Created on Dec 8, 2016
Lab13
@author: ian christensen (igc2)
'''

class Problem:
    ''' This is the parent class that represents a quiz object. '''
    
    def __init__(self, text):
        ''' This is the Constructor for the Problem Parent class. '''
        self._text = text
        
    def get_text(self):
        ''' This is the Accessor Method for the instance variable self._text. '''
        return self._text