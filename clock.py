import datetime
import tkinter as tk
from guisettings import *


class ClockWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
        
        self.timeLabel = tk.Label(self, text=self.time_now, font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)
        self.timeLabel.grid()
        
        self.updateClock()
    
    
    def updateClock(self):
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
    
        self.timeLabel.configure(text = self.time_now, font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)
        
        self.after(200, self.updateClock)
