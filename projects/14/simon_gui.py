'''
This program is the graphical user interface for the classic hasbro game Simon.
Created Fall 2016
Final Project
@author Ian Christensen (igc2)
'''

from tkinter import *
from simon import *
from random import randint
import time

class GUI:
    ''' This is the graphical user interface for Simon. '''
    
    def __init__(self, window):
        ''' The Constructor Method for the GUI. '''
        
        self._list = []
        self._best_sequence = 0
        self._last_sequence = 0
        self._current_score = 0
        self._attempt = 0
        self._user_list = []
        
        self._window = window
        self._window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        
        Win_Size = 500
        Arc_Size = Win_Size - (Win_Size / 35)
        Menu_Size = Win_Size - (Win_Size * 1.25)
        
        Arc_Trim = Win_Size / 25
        
        Win_Radius = Win_Size / 2
        Arc_Radius = (Arc_Size - Arc_Trim) / 2
        Menu_Radius = Menu_Size / 2
        
        self.width = Win_Size
        self.height = Win_Size
        self.canvas = Canvas(self._window, bg='white', width=self.width, height=self.height)
        self.canvas.pack()
        
        self.canvas.create_oval(0, 0, Win_Size, Win_Size, fill='black', outline='black')
        self.canvas.create_arc(Win_Size - Arc_Size, Win_Size - Arc_Size, Arc_Size, Arc_Size, fill='green', outline='black', width=Arc_Trim, start=90, extent=90)
        self.canvas.create_arc(Win_Size - Arc_Size, Win_Size - Arc_Size, Arc_Size, Arc_Size, fill='#FF0000', outline='black', width=Arc_Trim, start=0, extent=90)
        self.canvas.create_arc(Win_Size - Arc_Size, Win_Size - Arc_Size, Arc_Size, Arc_Size, fill='#FFFF00', outline='black', width=Arc_Trim, start=270, extent=90)
        self.canvas.create_arc(Win_Size - Arc_Size, Win_Size - Arc_Size, Arc_Size, Arc_Size, fill='#0000FF', outline='black', width=Arc_Trim, start=180, extent=90)
        self.canvas.create_oval(Win_Radius - Menu_Size, Win_Radius - Menu_Size, Win_Radius + Menu_Size, Win_Radius + Menu_Size, fill = 'black')
#         self.canvas.create_oval(125, 125, 375, 375, outline='#FFFFFF')
#         self.canvas.create_oval(25, 25, 475, 475, outline='#FFFFFF')
#         self.canvas.create_oval(0, 0, 500, 500, outline='#FFFFFF')
        
        add_button = Button(window, text='Last', command=self.get_last)
        add_button.pack(side=LEFT)
        add_button = Button(window, text='Play', command=self.play_game)
        add_button.pack(side=LEFT)
        add_button = Button(window, text='Check', command=self.check_game)
        add_button.pack(side=LEFT)
        add_button = Button(window, text='Best', command=self.get_best)
        add_button.pack(side=LEFT)
        
        self._message = StringVar()
        self._message.set('Let\'s play')
        self.message_label = Label(window, textvariable=self._message)
        self.message_label.pack(side=RIGHT)
        
        self.canvas.bind('<Button-1>', self.process_click)
                
    def check_game(self):
        ''' This method checks the user's list against the ai's list. '''
        if self._user_list == self.simon.get_sequence():
            self._message.set('Correct!')
        else:
            self._message.set('You lost! Your score was: '+str(self.simon.get_seqlen()))
            self.simon.reset_sequence()
            if self.simon.get_seqlen() > self._best_sequence:
                self._best_sequence = self.simon.get_seqlen()
            else:
                pass
        self._last_sequence = self.simon.get_seqlen()
        self.reset_userlist()

    def process_click(self, event):
        ''' This method allows the user to select a color. '''
        if 250 < event.x < 500 and 0 < event.y < 250:
            self._user_list.append('Red')
            
        if 250 < event.x < 500 and 250 < event.y < 500:
            self._user_list.append('Yellow')
            
        if 0 < event.x < 250 and 250 < event.y < 500:
            self._user_list.append('Blue')
            
        if 0 < event.x < 250 and 0 < event.y < 250:
            self._user_list.append('Green')
        
    def get_last(self):
        ''' This accessor method allows the user to see the previous score. '''
        return self._message.set('Your score last game was: '+str(self._last_sequence))
    
    def get_best(self):
        ''' This accessor method allows the user to see the high score. '''
        return self._message.set('Your high score is: '+str(self._best_sequence))
    
    def get_score(self):
        ''' This accessor method allows the user to get the current score. '''
        self._current_score = self.simon.get_sequence()
    
    def play_game(self):
        ''' This method adds an additional color to the ai sequence. '''
        self.simon = Simon()
        self.simon.new_color(randint(1, 4))
        for c in self.simon.get_sequence():
            self._message.set('New Color: '+c)
    
    def reset_userlist(self):
        ''' This method resets the user's list. '''
        self._user_list = []
  
    def safe_exit(self):
        ''' Terminate the animation before shutting down the GUI window. '''
        self._terminated = True
        self._window.destroy()
        
if __name__ == '__main__':
    root = Tk()
    root.title('Hasbro Simon')
    app = GUI(root)
    root.mainloop()