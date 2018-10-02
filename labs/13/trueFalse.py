'''
Models a True or False short answer problem.
Created on Dec 8, 2016
Lab13
@author: ian christensen (igc2)
'''

from problem import *

class TrueFalse(Problem):
    ''' Model a short-answer question '''
    
    def __init__(self, q, a):
        ''' Construct a short-answer question with question and answer texts '''
        Problem.__init__(self, q)
        self.text = q
        self.answer = a
        if not isinstance(a, bool):
            raise ValueError('Please enter a Boolean value (True or False)')
              
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text()+'.\nIs this statement true or false?'
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        if a.lower() == 'true' and self.answer == True:
            return True
        elif a.lower() == 'false' and self.answer == False:
            return True
        else:
            return False
    
    def get_answer(self):
        ''' Return the answer text '''
        return str(self.answer)