'''
This is the unit test for the temperature class.
November 28, 2016
Homework 11 Exercise 2
@author: Ian Christensen (igc2)
'''

# Import libraries
import unittest
from temperature_cli import Temperature

class Test(unittest.TestCase):
    ''' All test cases for the temperature class. '''
    
    def setUp(self):
        ''' Initialize the temperature class for each of the unit tests. '''
        self.temp = Temperature(-500)
    
    def ABS_ZERO(self):
        ''' Test invariant exception. '''
        try:
            self.temp.get_celsius()
            self.fail('This should raise an exception.')
        except Exception as e:
            assert(isinstance(e, ValueError))
            assert e.__str__() == 'Invalid Temperature'
            
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()