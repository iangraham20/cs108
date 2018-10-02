'''
This program is the CLI for the temperature class.
November 28, 2016
Homework 11 Exercise 2
@author: Ian Christensen (igc2)
'''

class Temperature:
    '''
    This class represents a temperature object in Fahrenheit.
    Invariant: temperature > absolute zero   
    '''
    
    def __init__(self, degrees = 0.0):
        ''' The constructor method for the Temperature class. '''
        if float(degrees) < -459.67:
            raise ValueError('Invalid temperature (must be greater than or equal to absolute zero).')
        if float(degrees) >= -459.67:
            self._degrees = float(degrees)
    
    def get_fahrenheit(self):
        ''' This accessor method converts Celsius into Fahrenheit. '''
        return self._degrees
    
    def get_celsius(self):
        ''' This accessor method converts Fahrenheit into Celsius. '''
        return (self._degrees - 32) * (5 / 9)
    
    def __str__(self):
        ''' The default format method. '''
        return '{:.2f} F'.format(self._degrees)
    
    def farenheit_format(self):
        ''' The format method for get_farenheit. '''
        return '{:.2f} F'.format(self.get_farenheit())
    
    def celsius_format(self):
        ''' The format method for get_celsius. '''
        return '{:.2f} C'.format(self.get_celsius())
    
if __name__ == '__main__':
    ''' Basic test cases. '''

    try:
        temp = Temperature(212.00)
        assert(temp.get_celsius() == 100.00)
        assert(temp.get_fahrenheit() == 212.00)
        
    except:
        print('Tests failed.')
    try:
        temp2 = Temperature(-600)
        assert False
    except ValueError:
        pass
    try:
        temp2 = Temperature('word')
        assert False
    except Exception:
        pass