''' A program that models a fraction using classesc
October 27, 2016
Homework 7 Exercise 7.3
@author Ian Christensen (igc2)
@author: Griffin Sparling (grs4) '''

# Import libraries.
import sys

def computeGCD(alpha, beta):
    ''' (int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid's algorithm '''
    
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

class Fraction:
    ''' A class that models a fraction.
        Invariant: Cannot have a denominator of zero. '''

    def __init__(self, numerator = 0, denominator = 1):
        ''' A method that initializes a fraction object '''
        
        # Create if statement to determine whether invariant is valid.
        if denominator != 0:
            self._numerator = numerator
            self._denominator = denominator
            self.simplify()
        else:
            print('Unable to create invalid fraction', file=sys.stderr)
            sys.exit(-1)
            
    def __str__(self):
        ''' A method that returns the numerator and denominator as a string. '''
        return (str(self._numerator) + '/' + str(self._denominator))
    
    def get_numerator(self):
        ''' An accessor method for numerator. '''
        return self._numerator
    
    def get_denominator(self):
        ''' An accessor method for denominator. '''
        return self._denominator
    
    def simplify(self):
        ''' A method that simplifies fractions using the Euclid's algorithm. '''
        gcd = computeGCD(self._numerator, self._denominator)
        
        if gcd != 0:
            self._numerator = self._numerator // gcd
            self._denominator = self._denominator // gcd
        if self._denominator < 0:
            self._numerator = self._numerator * -1
            self._denominator = self._denominator * -1
    
    def __mul__(self, other):
        ''' A mutator method that multiplies two fractions. '''
        numerator = self._numerator * other.get_numerator()
        denominator = self._denominator * other.get_denominator()
        return Fraction(numerator, denominator)

''' Test cases '''

# Exercise 8.4: Print tests

# zero = Fraction(0, 0)
# print(zero)
f1 = Fraction()
print(f1)
f2 = Fraction(1, 2)
print(f2)
f3 = Fraction(2, 4)
print(f3)
print(f2 * f3)

assert(f1.get_numerator() == 0)
assert(f1.get_denominator() == 1)
assert(f2.get_numerator() == 1)
assert(f2.get_denominator() == 2)
assert(f3.get_numerator() == 1)
assert(f3.get_denominator() == 2)