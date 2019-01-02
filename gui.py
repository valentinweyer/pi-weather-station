import tkinter as tk
import datetime

import Adafruit_DHT

from clock import *
from temperature import *
from date import *
from humidity import *
from outsidetemperature import *
from minimaloutsidetemperature import *
from maximaloutsidetemperature import *



root = tk.Tk()
root.wm_title("Wetterstation")

clock = ClockWidget(root)
clock.grid(row=0, column=1, padx=10, pady=10)

date = DateWidget(root)
date.grid(row=0, column=6, padx=10, pady=10)

temperature = TemperatureWidget(root)
temperature.grid(row=2, column=1, padx=10, pady=10)

humidity = HumidityWidget(root)
humidity.grid(row=4, column=1, padx=10, pady=10)

outsideTemperature = OutsideTemperatureWidget(root)
outsideTemperature.grid(row=2, column=6, padx=10, pady=10)

minimalOutsideTemperature = MinimalOutsideTemperatureWidget(root)
minimalOutsideTemperature.grid(row=3, column=6, padx=10, pady=10)

maximalOutsideTemperature = MaximalOutsideTemperatureWidget(root)
maximalOutsideTemperature.grid(row=4, column=6, padx=10, pady=10)

root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(2, minsize=200)
root.grid_columnconfigure(3, minsize=200)
root.grid_columnconfigure(4, minsize=200)
root.grid_columnconfigure(5, minsize=200)
root.grid_columnconfigure(8, minsize=200)
root.grid_rowconfigure(1, minsize=50)

      
root.mainloop()