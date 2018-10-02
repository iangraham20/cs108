'''
This program determines the minimum number of bills in change required for a transaction.
Created September 20, 2016
Homework 02 Exercise 01
@author: Ian Christensen (igc2)
'''

# According to the instructions all transactions must be whole numbers thus the use of integer.
cost = int(input('Please enter the charged amount for the transaction:'))
paid = int(input('Please enter the amount paid:'))

total_change = paid - cost
bill_20 = int(total_change / 20)
bill_10 = int((total_change % 20) / 10)
bill_05 = int(((total_change % 20) % 10) / 5)
bill_01 = int((((total_change % 20) % 10) % 5) / 1)

print('Change is $'+str(total_change)+':', bill_20, '20(s)', bill_10, '10(s)', bill_05, '5(s) and', bill_01, '1(s)')
