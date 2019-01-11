import datetime
import tkinter as tk
from guisettings import *


class DateWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.now = datetime.datetime.now()
        self.date_now = self.now.strftime("%d.%m.%y")
        
        self.dateLabel = tk.Label(self, text=self.date_now, font = ('arial', LABEL_FONT_SIZE, 'bold'))
        self.dateLabel.grid()
        
        self.updateDate()
    
    
    def updateDate(self):
        self.now = datetime.datetime.now()
        self.date_now = self.now.strftime("%d.%m.%y")
    
        self.dateLabel.configure(text = self.date_now, font = ('arial', LABEL_FONT_SIZE, 'bold'))
        
        self.after(200, self.updateDate)
