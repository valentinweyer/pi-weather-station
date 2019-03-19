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
        self.image = tk.Label(image = self.imageEx)
        self.image.grid(row=4, column=1)
          
        self.mintemptomorrow = tk.Label(self, text = "Min: " + self.Min + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND) 
        self.mintemptomorrow.grid()
        
        self.maxtemptomorrow = tk.Label(self, text = "Max: " + self.Max + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)
        self.maxtemptomorrow.grid()