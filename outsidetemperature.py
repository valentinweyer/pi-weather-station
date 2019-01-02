import tkinter as tk


class OutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Außen = str(4)
        
        self.OutsideTemperatureLabel = tk.Label(self, text="Außen: " + self.Außen + "°", font = ('arial', 48, 'bold'))
        self.OutsideTemperatureLabel.grid()
        
#        self.updateClock()
    

#    def updateOutTemperature(self):
#        self.now = datetime.datetime.now()
#        self.time_now = self.now.strftime("%X")
#    
#        self.timeLabel.configure(text = self.time_now)
#        
#        self.after(200, self.updateClock)


