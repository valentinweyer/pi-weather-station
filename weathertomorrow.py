import tkinter as tk
from guisettings import *


class WeatherTowmorrowWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.temperature = str(0)
        self.Min = str(2)
        self.Max = str(4)
          
        self.imageEx = tk.PhotoImage(file = '200x200')
        tk.Label(self, image=self.imageEx).grid(row=2, column=0, padx=10, pady=3)
          
        self.mintemptomorrow = tk.Label(self, text = "Min: " + self.Min + "°", font = ('arial', LABEL_FONT_SIZE, 'bold')) 
        self.mintemptomorrow.grid()
        
        self.maxtemptomorrow = tk.Label(self, text = "Max:" + self.Max + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'))
        self.maxtemptomorrow.grid()