''' Model of a solar system.
Created Fall 2014
Lab 10 Exercise 4
@author: smn4
@author: Ian Christensen (igc2) '''

from sun import *
from planet import *

class Solar_System:
    
    def __init__(self):
        self._sun = None
        self._planets = []
        
    def add_sun(self, a_sun):
        if isinstance(a_sun, Sun):
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')
        
    def add_planet(self, a_planet):
        if isinstance(a_planet, Planet):
            self._planet = a_planet
        else:
            raise TypeError('add_planet(): cannot add ' + str(type(a_planet)) + ' to solar system')
        
    def show_planets(self):
        for a_planet in self._planets:
            print(a_planet)

if __name__ == '__main__':
    solar_sys = Solar_System()
    solar_sys.add_sun(Sun('Sun', 1000, 1000, 1000))
    try:
        solar_sys.add_sun(Planet('Earth', 1000, 1000, 1000))
        assert False
    except TypeError:
        pass
    solar_sys.add_planet(Planet('Earth', 1000, 1000, 1000))
    try:
        solar_sys.add_planet(Sun('Sun', 1000, 1000, 1000))
        assert False
    except TypeError:
        pass