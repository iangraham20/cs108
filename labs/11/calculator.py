''' Provide calculator functionality
Created Fall 2014
updated, Summer, 2015
Lab 11 Exercise 1
@author: Ian Christensen (igc2)
@author: smn4
@author: kvlinden '''

class Calculator:
    ''' A calculator that is capable of performing basic arithmetic. '''
    
    def __init__(self):
        ''' Initialize calculator memory to 0 '''
        memory = 0

    def calculate(self, operand1 = '0', operator = '+', operand2 = '0'):
        ''' Perform the specified calculation '''
        
        if operator == '+':
            return float(operand1) + float(operand2)
        if operator == '-':
            return float(operand1) - float(operand2)
        if operator == '*':
            return float(operand1) * float(operand2)
        if operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError('float division by zero')
            else:
                return float(operand1) / float(operand2)
        else:
            raise ValueError('Invalid operation: ' + operator)
        
if __name__ == '__main__':
    calc = Calculator()
    print(calc.calculate('1', '+', '1'))
    calc = Calculator()
    print(calc.calculate('0', '+', '1'))
