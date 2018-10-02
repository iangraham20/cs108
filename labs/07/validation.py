''' A program that uses a definition to validate user created strings.
October 20, 2016
Lab 7 Exercises 7.1, 7.2, 7.3
@author: kvlinden
@author Ian Christensen (igc2)
@author: Griffin Sparling (grs4) '''



def isValidSSN(ssn):
    ''' A function that determines whether a Social Security Number is valid. '''
    if ssn[0:3].isnumeric() and ssn[3] == '-' and ssn[4:6].isnumeric() and ssn[6] == '-' and ssn[7:12].isnumeric():
        return True
    else:
        return False

def isValidpassword(pswd):
    ''' A function that determines whether a password is valid. '''
    if len(pswd) <= 0:
        return False
    if len(pswd) >= 8:
        return True
    elif pswd.isalnum():
        return True
    elif pswd.digit() >= 2:
        return True
    else: 
        return False

def isValidPrefix(cc):
    ''' A function that determines whether the prefix of a Credit Card Number is valid. '''
    if 13 <= len(cc) <= 16:
        if cc.startswith('37'):
            return True
        elif cc.startswith('4'):
            return True
        elif cc.startswith('5'):
            return True
        elif cc.startswith('6'):
            return True
        else:
            return False

def sum_of_odds(cc):
    ''' Finds the sum of all the odds in a credit card number. '''
    sum_odds_cc = 0
    for odds in cc[-1::-2]:
        sum_odds_cc = sum_odds_cc + int(odds)
    return sum_odds_cc

def sum_of_double_evens(cc):
    ''' Finds the sum of all the doubled evens in a credit card number. '''
    double_evens_cc = 0
    for evens in cc[-2::-2]:
        evens = 2 * int(evens)
        if len(str(evens)) == 2:
            evens = int(str(evens)[0]) + int(str(evens)[1])
        double_evens_cc = double_evens_cc + int(evens)
    return double_evens_cc

def isValidCC(cc):
    ''' Validates credit card number.'''
    if len(cc) <= 0:
        return 'Invalid CC Number'
    for num in cc:
        if num.isdigit() == False:
            return 'Invalid character for CC number'
    if isValidPrefix(cc) == False:
        return 'Invalid CC number.'
    elif not ((sum_of_odds(cc) + sum_of_double_evens(cc)) % 10 == 0):
        return 'Invalid CC number'
    return True

def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Social Security Number')
    print('B. Password ')
    print('C. Credit Card Number')
    print('Q. Quit')


# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()
    
    if choice == 'A':
        print('Social Security Number', isValidSSN(input('Please Enter Social Security Number: ')))
        print('SSN')
    elif choice == 'B':
        print('P', isValidpassword(input('Please Enter Password: ')))
    elif choice == 'C':
        print('CCN', isValidCC(input('Please Enter Credit Card Number: ')))
    elif choice == 'Q':
        break
    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))
print('\nGood-bye!')