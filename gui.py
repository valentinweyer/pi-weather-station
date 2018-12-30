import tkinter as tk
import temperature as Temp_in
import datetime
import Adafruit_DHT
from clock import *
 
#sensor=Adafruit_DHT.DHT11
#gpio=27
 

    #humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    #Temp_In = str(temperature)
    #now = datetime.datetime.now()
    #time_now = str(time)


root = tk.Tk() # Fenster erstellen
root.wm_title("Wetterstation") # Fenster Titel
#root.config(background = "#ffffff") # Hintergrundfarbe des Fensters
 

#Hier kommen die Elemente hin
#timeFrame.grid(row=0, column=0, padx=10, pady=3) # Relative Position und Seitenabstand (padding) angeben


    #leftLabel1 = Label(leftFrame, text="\n\nInnen: " + Temp_In + "°")
#    timeLabel.grid(row=1, column=0, padx=10, pady=3)
#    leftLabel2 = Label(leftFrame, text=time_now)
##   leftLabel3 = Label(leftFrame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                               ")
#    leftLabel3.grid(row=3, column=0, padx=10, pady=3)


#So geht ein Bild:
#imageEx = PhotoImage(file = '200x200')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
myClock = Clock(root)
 
root.mainloop() # GUI wird upgedated. Danach keine Elemenet setzen