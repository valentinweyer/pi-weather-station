from tkinter import *
import temperature as Temp_in
import datetime
import Adafruit_DHT
import time
 
sensor=Adafruit_DHT.DHT11
 

gpio=27
 


#def Temp():
#    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
while True:
    #Temp()
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    Temp_In = str(temperature)
    now = datetime.datetime.now()


    root = Tk() # Fenster erstellen
    root.wm_title("Wetterstation") # Fenster Titel
    root.config(background = "#FFFFFF") # Hintergrundfarbe des Fensters
 
# Hier kommen die Elemente hin
 
 
#Hier kommen die Elemente hin
    leftFrame = Frame(root, width=200, height = 400) # Frame initialisieren
    leftFrame.grid(row=0, column=0, padx=10, pady=3) # Relative Position und Seitenabstand (padding) angeben

 
#rightFrame = Frame(root, width=800, height = 400)
#rightFrame.grid(row=0, column=1, padx=10, pady=3)




    leftLabel1 = Label(leftFrame, text="\n\nInnen: " + Temp_In + "°")
    leftLabel1.grid(row=1, column=0, padx=10, pady=3)
    leftLabel2 = Label(leftFrame, text=now.strftime("%X"))
    leftLabel2.grid(row=2, column=0, padx=10, pady=3)
    leftLabel3 = Label(leftFrame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                               ")
    leftLabel3.grid(row=3, column=0, padx=10, pady=3)


#So geht ein Bild:
#imageEx = PhotoImage(file = '200x200')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
    print("test")
 
    root.mainloop() # GUI wird upgedated. Danach keine Elemenet setzen