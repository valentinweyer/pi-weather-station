import Adafruit_DHT
import time
import tkinter as tk
from guisettings import *
 

class PlaceHolderWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.imageEx = tk.PhotoImage(file = '200x200')
        self.image = tk.Label(image = self.imageEx)
        self.image.grid(row=2, column=7)     