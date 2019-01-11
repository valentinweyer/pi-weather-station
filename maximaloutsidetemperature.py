import tkinter as tk
from guisettings import *


class MaximalOutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Max = str(6)

        
        self.maximalOutsideTemperature = tk.Label(self, text="Max: " + self.Max + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'))
        self.maximalOutsideTemperature.grid()    