'''
This program is the command line interface for the classic hasbro game Simon.
Created Fall 2016
Final Project
@author Ian Christensen (igc2)
'''
from random import randint

class Simon:
    
    def __init__(self, sequence = [], attempt = 1, turn = 0, color = ''):
        ''' The constructor method creates and initializes the necessary parameters for the class.  '''
        self._sequence = sequence
        self._attempt = attempt
        self._turn = turn
        self._color = color
       
    def new_color(self, num=0):
        ''' This mutator method adds a random color to the sequence. '''
        self._num = num
        if self._num == 1:
            self._sequence.append('Green')
        if self._num == 2:
            self._sequence.append('Red')
        if self._num == 3:
            self._sequence.append('Blue')
        if self._num == 4:
            self._sequence.append('Yellow')
    
    def get_color(self):
        ''' This accessor method returns the current color. '''
        return self._color
    
    def get_sequence(self):
        ''' This accessor method returns the current sequence. '''
        return self._sequence
    
    def get_seqlen(self):
        ''' This accessor method returns the current sequence. '''
        return len(self._sequence)
    
    def get_turn(self):
        ''' This accessor method returns the current turn value. '''
        return self._turn
    
    def get_attempts(self):
        ''' This accessor method returns the current number of attempts. '''
        return self._attempts
    
    def set_color(self, other):
        ''' This mutator sets the color value. '''
        self._color = other
    
    def reset_attempts(self, other=1):
        ''' This mutator resets the attempts'''
        self._attempts = other
        
    def reset_turns(self, other=0):
        ''' This mutator resets the turn value. '''
        self._turns = other
        
    def reset_sequence(self):
        ''' This mutator resets the sequence. '''
        for c in self._sequence:
            self._sequence.remove(c)