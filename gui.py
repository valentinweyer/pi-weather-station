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
from weatherday1 import *
from weatherday2 import *
from weatherday3 import *
from weatherday4 import *
from weatherpicture import *
from placeholder import *
from guisettings import *


root = tk.Tk()
root.config(background = "#" + BACKGROUND)


clock = ClockWidget(root)
clock.grid(row=1, column=1, padx=10, pady=10)

date = DateWidget(root)
date.grid(row=1, column=4, padx=10, pady=10)

temperature = TemperatureWidget(root)
temperature.grid(row=2, column=1, padx=10, pady=10)

humidity = HumidityWidget(root)
humidity.grid(row=3, column=1, padx=10, pady=10)

outsideTemperature = OutsideTemperatureWidget(root)
outsideTemperature.grid(row=2, column=4, padx=10, pady=10)

minimalOutsideTemperature = MinimalOutsideTemperatureWidget(root)
minimalOutsideTemperature.grid(row=3, column=4, padx=10, pady=10)

maximalOutsideTemperature = MaximalOutsideTemperatureWidget(root)
maximalOutsideTemperature.grid(row=4, column=4, padx=10, pady=10)

weathertomorrow = WeatherTowmorrowWidget(root)
weathertomorrow.grid(row=5, column=1, padx=10, pady=10)

weatherday2widget = WeatherDay2Widget(root)
weatherday2widget.grid(row=5, column=2, padx=10, pady=10)

weatherday3widget = WeatherDay3Widget(root)
weatherday3widget.grid(row=5, column=3, padx=10, pady=10)

weatherday4widget = WeatherDay4Widget(root)
weatherday4widget.grid(row=5, column=4, padx=10, pady=10)

weatherpicturewidget = WeatherPictureWidget(root)
weatherpicturewidget.place(x=575, y=100)

placeholder = PlaceHolderWidget(root)
placeholder.grid(row=2, column=7)


root.grid_columnconfigure(0, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(1, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(2, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(3, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(4, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(5, minsize=COLUMN_MIN_SIZE)
root.grid_columnconfigure(8, minsize=COLUMN_MIN_SIZE)
root.grid_rowconfigure(1, minsize=ROW_MIN_SIZE)
root.grid_rowconfigure(5, minsize=ROW_MIN_SIZE)


#interesting fullscreen hack: https://stackoverflow.com/a/42173885
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)


root.mainloop()