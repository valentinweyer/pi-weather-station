import tkinter as tk
from guisettings import *


class OutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Außen = str(4)
        
        self.OutsideTemperatureLabel = tk.Label(self, text="Außen: " + self.Außen + "°", font = ('arial', LABEL_FONT_SIZE, 'bold'))
        self.OutsideTemperatureLabel.grid()