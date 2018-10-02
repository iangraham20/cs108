'''
Model a single polygon
Created Fall 2016
homework12
@author Ian Christensen (igc2)
'''

from tkinter import *
from polygon import *
from help import *
from random import randint


class PolygonGUI:
    ''' This class represents a Polygon rendering GUI object. '''
    
    def __init__(self, window):
        ''' This is the constructor method for the Polygon GUI class. '''
        
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        
        self.width = 400
        self.height = self.width
        
        self.canvas = Canvas(self.window, bg = '#FFFFFF', width = self.width, height = self.height)
        self.canvas.pack()
        
        add_button = Button(window, text = 'Clear', command = self.clear_canvas)
        add_button.pack(side = LEFT)
        
        add_button = Button(window, text = 'Quit', command = self.safe_exit)
        add_button.pack(side = RIGHT)
        
        self.terminated = False
        self._rate = 100
        
        while not self.terminated:
            
            x = randint(-50, self.width)
            y = randint(0, self.height + 50)
            scale = randint(0, self.width / 2)
            
            new_polygon = Polygon(x, y,
                                  x + scale, y,
                                  x, y - scale,
                                  x + scale, y - scale,
                                  get_random_color())
            new_polygon.render(self.canvas)
            
            self.canvas.after(self._rate)
            self.canvas.update()
    
    def clear_canvas(self):
        ''' This method removes everything on the canvas. '''
        return self.canvas.delete(ALL)
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()
        
if __name__ == '__main__':
    root = Tk()
    root.title('Polygons')    
    app = PolygonGUI(root)
    root.mainloop()
        