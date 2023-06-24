
import tkinter as tk

rome = tk.Tk()

for i in range(1,4):
    print(12 * i)
    label = tk.Label(rome,text="Testing Testing!",font=("Ariel",str(12 * i),"underline"))
    label.pack()

button_2 = tk.Button(rome, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
rome.mainloop()