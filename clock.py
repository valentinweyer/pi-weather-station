import datetime
import tkinter as tk


class ClockWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
        
        self.timeLabel = tk.Label(self, text=self.time_now, font = ('arial', 48, 'bold'))
        self.timeLabel.grid()
        
        self.updateClock()
    
    
    def updateClock(self):
        self.now = datetime.datetime.now()
        self.time_now = self.now.strftime("%X")
    
        self.timeLabel.configure(text = self.time_now, font = ('arial', 48, 'bold'))
        
        self.after(200, self.updateClock)
