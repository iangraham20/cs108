'''
Models a fill in the blank short answer problem.
Created on Dec 8, 2016
Lab13
@author: ian christensen (igc2)
'''

from problem import *

class FillInTheBlank(Problem):
    ''' Model a short-answer question '''
    
    def __init__(self, q, a):
        ''' Construct a short-answer question with question and answer texts '''
        Problem.__init__(self, q)
        self.text = q
        self.answer = a
              
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text()+'.\nFill in the blank.'
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        return self.answer == a
    
    def get_answer(self):
        ''' Return the answer text '''
        return self.answer