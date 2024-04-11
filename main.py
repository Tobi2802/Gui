import custom_module
import tkinter as tk


fenster = tk.Tk()
fenster.geometry("100x100")

B1 = tk.Button(fenster, text ="Freundlich", command=lambda: custom_module.Freundliche_Nachricht("Tobi"))#Lambda wird benötigt für Funktionen mit Parameter
B1.pack()
 
B2 = tk.Button(fenster, text ="Unfreundlich", command=lambda: custom_module.Unfreundliche_Nachricht("Tobi"))#Lambda wird benötigt für Funktionen mit Parameter
B2.pack()
fenster.mainloop()
