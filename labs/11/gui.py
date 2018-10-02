'''
Created on Nov 17, 2016
Lab 11 Exercise 2
@author: Ian Christensen (igc2)
'''

from tkinter import *
from calculator import *

class Gui:
    
    def do_calculation(self):
        ''' Calculates the answer using the input values and the Calculator class. '''
        try:
            result = self._calc.calculate(self._input1.get(), self._operator.get(), self._input2.get())
            self._result.set(result)
        except Exception as e:
            self._message.set(e)
    
    def __init__(self, window):
        ''' Constructor Method for a calculator interface. '''
        
        # Call calculator class.
        self._calc = Calculator()
        
        # First input.
        self._input1 = StringVar()
        input1_label = Label(window, text="Input 1:")
        input1_label.grid(row=0, column=0, sticky=E)
        input1_entry = Entry(window, width=6, textvariable=self._input1)
        input1_entry.grid(row=0, column=1, sticky=W)
        
        # Second input.
        self._input2 = StringVar()
        input2_label = Label(window, text="Input 2:")
        input2_label.grid(row=2, column=0, sticky=E)
        input2_entry = Entry(window, width=6, textvariable=self._input2)
        input2_entry.grid(row=2, column=1, sticky=W)
        
        # Radiobuttons' location and default.
        operator_frame = Frame(window)
        operator_frame.grid(row=3, column=0, columnspan=2)
        self._operator = StringVar()
        self._operator.set("+")
        
        # Radiobuttons for all possible operators.
        add_button = Radiobutton(operator_frame, text="+", variable=self._operator, value='+')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="-", variable=self._operator, value='-')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="*", variable=self._operator, value='*')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="/", variable=self._operator, value='/')
        add_button.pack(side=LEFT)
        
        # Calculate button.
        add_button = Button(window, text="Calculate", command=self.do_calculation)
        add_button.grid(row=4, column=1, sticky=W)
        
        # Find and give result.
        result_label = Label(window, text="Result: ")
        result_label.grid(row=3,  column=2, sticky=W)
        self._result = StringVar()
        self.result_label = Label(window, textvariable=self._result, width=6)
        self.result_label.grid(row=4, column=2, sticky=W)
        
        # Initial message and any errors during calculation.
        self._message = StringVar()
        self._message.set("Please enter a calculation.")
        self.message_label = Label(window, textvariable=self._message)
        self.message_label.grid(row=5, sticky=W)
        
if __name__ == '__main__':
    ''' test case '''
    root = Tk()
    root.title('Calculator')
    app = Gui(root)
    root.mainloop()