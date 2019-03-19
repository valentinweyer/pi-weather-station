import tkinter as tk
from guisettings import *


class WeatherDay2Widget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.temperature = str(0)
        self.Min = str(3)
        self.Max = str(6)
        
        self.imageEx = tk.PhotoImage(file = '200x200')
        self.image = tk.Label(image = self.imageEx)
        self.image.grid(row=4, column=2)
        
        self.mintempday2 = tk.Label(self, text = "Min: " + self.Min + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND) 
        self.mintempday2.grid()
        
        self.maxtempday2 = tk.Label(self, text = "Max: " + self.Max + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)
        self.maxtempday2.grid()