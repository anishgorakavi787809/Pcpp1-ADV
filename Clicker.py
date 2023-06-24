import tkinter as tk
from tkinter import messagebox 
from tkmacosx import Button

first_app = tk.Tk()
def onClick():
    if messagebox.askyesno(message="Do you want to close me?"):
        first_app.destroy()
    
first_app.title("Anish COm")
button_1 = Button(first_app, text="Button #1",bg="red")
button_2 = Button(first_app, text="Button #2")
button_3 = Button(first_app, text="Button #3")


button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()
first_app.mainloop()