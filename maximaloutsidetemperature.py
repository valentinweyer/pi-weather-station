import tkinter as tk


class MaximalOutsideTemperatureWidget(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.root = root
        self.Max = str(6)

        
        self.maximalOutsideTemperature = tk.Label(self, text="Max: " + self.Max + "°", font = ('arial', 48, 'bold'))
        self.maximalOutsideTemperature.grid()
        
#        self.updateClock()
    

#    def updateOutTemperature(self):
#        self.now = datetime.datetime.now()
#        self.time_now = self.now.strftime("%X")
#    
#        self.timeLabel.configure(text = self.time_now)
#        
#        self.after(200, self.updateClock)




       