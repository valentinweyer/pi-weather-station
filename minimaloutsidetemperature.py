import tkinter as tk
from guisettings import *


class MinimalOutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Min = str(2)

        self.minimalOutsideTemperature = tk.Label(self, text="Min: " + self.Min + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'))
        self.minimalOutsideTemperature.grid()