import Adafruit_DHT
import time
import tkinter as tk
from guisettings import *


sensor=Adafruit_DHT.DHT11
gpio=27
 

class HumidityWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.humidityLabel = tk.Label(self, text=str(self.getCurrent()) + "%", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)
        self.humidityLabel.grid()
        
        self.updateHumidity()
    
    
    def updateHumidity(self):    
        self.humidityLabel.configure(text =str(self.getCurrent()) + "%", font = ('arial', LABEL_FONT_SIZE, 'bold'), background = "#" + BACKGROUND)

        self.after(30000, self.updateHumidity)
 
 
    def getCurrent(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        return humidity
