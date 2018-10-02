''' find_perfects.py finds and prints all perfect numbers between 2 and 10,000
Created October 3, 2016
Lab 05 Exercise 5.1 a, b, c
@author: Ian Christensen (igc2)
@author: Griffin Sparling (grs4)
'''

perfect_num = 0

# begin while loop and if statments
for value in range(2, 10000):
    # assign variables
    # value = int(input('Please enter a positive integer: '))
    low = 1
    high = value
    divisors = []
    
    # begin while loop
    while low < high:
        if value % low == 0:
            high = value / low
            divisors.append(low)
            if high != low:
                divisors.append(high)
        low = low + 1
    divisors.remove(value)
    if sum(divisors) == value:
        # print results
        print(value)
        perfect_num += 1
    if perfect_num == 4:
        break