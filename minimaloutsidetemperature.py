import tkinter as tk


class MinimalOutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Min = str(2)

        
        self.minimalOutsideTemperature = tk.Label(self, text="Min: " + self.Min + "°", font = ('arial', 48, 'bold'))
        self.minimalOutsideTemperature.grid()
        
#        self.updateClock()
    

#    def updateOutTemperature(self):
#        self.now = datetime.datetime.now()
#        self.time_now = self.now.strftime("%X")
#    
#        self.timeLabel.configure(text = self.time_now)
#        
#        self.after(200, self.updateClock)




#        self.Max = str(6)