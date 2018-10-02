'''
This is the GUI for the temperature class.
November 28, 2016
Homework 11 Exercise 2
@author: Ian Christensen (igc2)
'''

from tkinter import *
from temperature_cli import *

class Gui:
    
    def convert(self):
        ''' The conversion command method. '''
        try:
            self._temp = Temperature(self._input.get())
            result = self._temp.celsius_format()
            self._result.set(result)
        except Exception as e:
            self._message.set('Invalid Temperature: Please enter a numeric character greater than absolute zero.')

    def __init__(self, window):
        ''' The Constructor Method for the temperature GUI.  '''
        
        # Create variable
        self._temp = Temperature()
        
        # First row
        self._input = StringVar()
        input_label = Label(window, text="Temperature (in Fahrenheit):")
        input_label.grid(row=0, column=0, sticky=W)
        
        input_entry = Entry(window, width=6, textvariable=self._input)
        input_entry.grid(row=0, column=1, sticky=W)
        
        # Second row
        add_button = Button(window, text="Convert to Celsius", command=self.convert)
        add_button.grid(row=1, column=0, sticky=E)
        
        self._result = StringVar()
        self.result_label = Label(window, textvariable=self._result, width=6)
        self.result_label.grid(row=1, column=1, sticky=W)
        
        # Third row
        self._message = StringVar()
        self._message.set("Welcome!")
        
        self.message_label = Label(window, textvariable=self._message)
        self.message_label.grid(row=5, sticky=W)
        
if __name__ == '__main__':
    ''' test case '''
    root = Tk()
    root.title('Temperature Conversions')
    app = Gui(root)
    root.mainloop()