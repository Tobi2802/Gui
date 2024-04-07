import custom_module
import tkinter as tk

def say_hi (name):
    print(f"Hallo herzlich Willkommen {name}")

fenster = tk.Tk()
fenster.geometry("100x100")
  
B = tk.Button(fenster, text ="Drücken", command=lambda: custom_module.say_hi("Tobi"))#Lambda wir dbenötigt für Funktionen mit Parameter
B.pack()
fenster.mainloop()