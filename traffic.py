import tkinter as tk


window = tk.Tk()

can = tk.Canvas(window,width=200,height=600,bg="gray")
can.create_oval(200,10,10,200)

can.pack()
window.mainloop()