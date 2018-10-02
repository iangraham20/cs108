'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *

class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.pack()
        add_button = Button(window, text='Add particle', command=self.add_particle)
        add_button.pack()
        self.terminated = False
        
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        
        self.p_list = []
        while not self.terminated:
            self.canvas.delete(ALL)
            for par in self.p_list:
                par.move(self.canvas)
                par.render(self.canvas)
                for element in self.p_list:
                    par.bounce(element)
            self.canvas.after(50)
            self.canvas.update()
    
    def add_particle(self):
        ''' '''
        var = Particle(randint(100 , 300), randint(100, 300),
                       randint(-25, 25), randint(-25, 25),
                       randint(10, 20), get_random_color())
        self.p_list.append(var)
    
    def check_remove_particle(self, event):
        ''' '''
        copy = self.p_list[:]
        for par in copy:
            if distance(event.x, event.y, par.get_x(), par.get_y()) < par.get_radius():
                self.p_list.remove(par)
        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()