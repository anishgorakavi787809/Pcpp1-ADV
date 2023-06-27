from __future__ import annotations
import tkinter as tk
from random import randint


window = tk.Tk()
window.title("Catch Me!")


#Set dimension of window to be 500x500
window.geometry("500x500")

#I want window to be unresizable
window.resizable(False, False)

button = tk.Button(window, text="Click Me!")


button.place(x=0,y=0)
button.bind("<Enter>",lambda x: button.place(x=randint(0,480),y=randint(0,480)))
window.mainloop()