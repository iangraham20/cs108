''' A class that represents an employee object.
November 3, 2016
Lab 9 Exercise 9.1, 9.2, 9.3
@author Ian Christensen (igc2) '''

import sys

class Employee:
    ''' A class that represents an employee object. 
        Invariant: Salary >= 20000 '''
    
    def __init__(self, line = ''):
        ''' The Constructor Method... '''
        if line == '':
            self._first = 'John'
            self._last = 'Smith'
            self._rank = 'Staff'
            self._salary = 100000
        if line != '':
            strings = line.split()
            self._first = strings[0]
            self._last = strings[1]
            self._rank = strings[2]
            if int(strings[3]) >= 20000:
                self._salary = strings[3]
            else:
                print('Invalid Salary')
                sys.exit(-1)
            
        
    def __str__(self):
        ''' The Format Method allows for readable printing of the variables in the class. '''
        return '{0}, {1}.:{2} (${3})'.format(self._last, self._first[0], self._rank, self._salary)
    
    def get_rank(self):
        ''' The Accessor Method that finds the rank of an employee. '''
        return self._rank
    
    def get_salary(self):
        ''' The Accessor Method that finds the salary of an employee. '''
        return self._salary

if __name__ == '__main__':
    ''' test cases '''
    print(Employee())
    print(Employee('Tom Brown Staff 50000'))
    print(Employee('Jane Doe Staff 100'))
    