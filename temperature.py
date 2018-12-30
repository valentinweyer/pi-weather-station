import Adafruit_DHT
import time
import tkinter as tk


sensor=Adafruit_DHT.DHT11
gpio=27
 

class TemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.temperatureLabel = tk.Label(self, text=str(self.getCurrent()))
        self.temperatureLabel.grid()
        
        self.updateTemperature()
    
    
    def updateTemperature(self):    
        self.temperatureLabel.configure(text = str(self.getCurrent()))

        self.after(30000, self.updateTemperature)
 
 
    def getCurrent(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        return temperature
