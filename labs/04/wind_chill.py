''' This program is used to determine the wind chill using temperature, wind speed, and the National Weather Service formula
Created September 29, 2016
Lab 04 Exercise 4.1 (a, b, c)
@author: Ian Christensen (igc2)
@author: Griffin Sparling (grs4)
'''

# assign variables
temp_fah = float(input('Please enter a temperature in degrees Fahrenheit: '))
wind_mph = float(input('Please enter a wind speed in mph: '))

# solve for wind_chill
wind_chill = 35.74 + (0.6215 * temp_fah) - (35.75 * (wind_mph**0.16)) + (0.4275 * temp_fah * (wind_mph**0.16))

# determine number of layers necessary
if wind_mph < 2 or temp_fah < -58 or temp_fah > 41:
    print('Error: the user input was invalid')
else:
    print(wind_chill)

if wind_chill < -40:
    print('Stay home')
elif -40 <= wind_chill < -10:
    print('Wear 4 layers')
elif -10 <= wind_chill < 20:
    print('Wear 3 layers')
elif 20 <= wind_chill < 40:
    print('Wear 2 layers')
else:
    print('Wear 1 layer')