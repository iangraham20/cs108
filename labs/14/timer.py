'''
 This module implements a simple timer that runs every one second (1000 milliseconds).

 @author: kvlinden
 @version: Summer, 2016
 '''

from tkinter import *

class TimerDemo:
    def __init__(self, window):
        self.window = window
        self.counter = IntVar()
        self.counter.set(0)
        Label(self.window, textvariable=self.counter).pack()
        self.window.after(1000, self.update_clock)

    def update_clock(self):
        self.counter.set(self.counter.get() + 1)
        # Schedule the next event. Skip this step if you want the timed events to stop.
        self.window.after(1000, self.update_clock)

if __name__ == '__main__':
    root = Tk()
    root.title('Timer Demo')
    app = TimerDemo(root)
    root.mainloop()
