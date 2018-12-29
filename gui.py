from tkinter import *
#from


uhrzeit=str(12:34)
Temp_In= str(5)


root = Tk() # Fenster erstellen
root.wm_title("Wetterstation") # Fenster Titel
root.config(background = "#FFFFFF") # Hintergrundfarbe des Fensters
 
# Hier kommen die Elemente hin
 
 
#Hier kommen die Elemente hin
leftFrame = Frame(root, width=200, height = 400) # Frame initialisieren
leftFrame.grid(row=0, column=0, padx=10, pady=3) # Relative Position und Seitenabstand (padding) angeben

 
#rightFrame = Frame(root, width=800, height = 400)
#rightFrame.grid(row=0, column=1, padx=10, pady=3)


leftLabel1 = Label(leftFrame, text=)
leftLabel1.grid(row=1, column=0, padx=10, pady=3)
leftLabel2 = Label(leftFrame, text="\n\nInnen: " + Temp_In + "°")
leftLabel2.grid(row=2, column=0, padx=10, pady=3)
leftLabel3 = Label(leftFrame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                               ")
leftLabel3.grid(row=3, column=0, padx=10, pady=3)


#So geht ein Bild:
#imageEx = PhotoImage(file = '200x200')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
 
 
root.mainloop() # GUI wird upgedated. Danach keine Elemenet setzen