import tkinter as tk
import datetime

import Adafruit_DHT

from clock import *
from temperature import *

root = tk.Tk()
root.wm_title("Wetterstation")

clock = ClockWidget(root)
clock.grid(row=0, column=0, padx=10, pady=10)

temperature = TemperatureWidget(root)
temperature.grid(row=1, column=0, padx=10, pady=10)
      
root.mainloop()