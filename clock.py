import datetime
from tkinter import *


class ClockComponent:
    def __init__(self, root):
        self.root = root
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
        
        self.timeFrame = Frame(self.root, width=200, height = 400) # Frame initialisieren
        self.timeFrame.grid(row=0, column=0, padx=10, pady=3)
        self.timeLabel = Label(self.timeFrame, text=self.time_now)
        self.timeLabel.grid()
        
        self.updateClock()
    
    
    def updateClock(self):
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
    
        self.timeLabel.configure(text = self.time_now)
        self.timeFrame.after(200, self.updateClock)



    def Date():
       print(now.strftime("%d ""%B ""%Y"))