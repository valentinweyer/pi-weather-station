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
from weathertomorrow import *
from guisettings import *


root = tk.Tk()
root.wm_title("Wetterstation")
root.geometry("1280x720") #Hack for fixing the size when developing...
root.resizable(0, 0)

clock = ClockWidget(root)
clock.grid(row=0, column=1, padx=10, pady=10)

date = DateWidget(root)
date.grid(row=0, column=5, padx=10, pady=10)

temperature = TemperatureWidget(root)
temperature.grid(row=2, column=1, padx=10, pady=10)

humidity = HumidityWidget(root)
humidity.grid(row=4, column=1, padx=10, pady=10)

outsideTemperature = OutsideTemperatureWidget(root)
outsideTemperature.grid(row=2, column=5, padx=10, pady=10)

minimalOutsideTemperature = MinimalOutsideTemperatureWidget(root)
minimalOutsideTemperature.grid(row=3, column=5, padx=10, pady=10)

maximalOutsideTemperature = MaximalOutsideTemperatureWidget(root)
maximalOutsideTemperature.grid(row=4, column=5, padx=10, pady=10)

weathertomorrow = WeatherTowmorrowWidget(root)
weathertomorrow.grid(row=6, column=1, padx=10, pady=10)

root.grid_columnconfigure(0, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(2, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(3, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(4, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(5, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(8, minsize=COLUMN_MIN_SIZE)
root.grid_rowconfigure(1, minsize=ROW_MIN_SIZE)
root.grid_rowconfigure(5, minsize=ROW_MIN_SIZE)
      
root.mainloop()