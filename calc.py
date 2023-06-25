import tkinter as tk
from tkinter import messagebox

wdow = tk.Tk()
wdow.title("My Calculator app")
operator_var = tk.StringVar(wdow,"+")

def do_math():
    try:
        match operator_var.get():
            case "+":
                messagebox.showinfo(message=str(first_number_variable.get() + second_number_variable.get()))
            case "-":
                messagebox.showinfo(message=str(first_number_variable.get() - second_number_variable.get()))
            case "*":
                messagebox.showinfo(message=str(first_number_variable.get() * second_number_variable.get()))
            case "/":
                try:
                    messagebox.showinfo(message=str(first_number_variable.get() / second_number_variable.get()))
                except ZeroDivisionError:
                    messagebox.showerror(message="Hey, you cannot put second box as 0")
            case _:
                messagebox.showinfo(message="Somehow, this bug came.")
    except tk.TclError:
        messagebox.showerror(message="You typed in a non number!")
#Operators 

add = tk.Radiobutton(wdow,text="+",variable=operator_var,value="+")
add.grid(row=1,column=1)

sub = tk.Radiobutton(wdow,text="-",variable=operator_var,value="-")
sub.grid(row=2,column=1)

mul = tk.Radiobutton(wdow,text="*",variable=operator_var,value="*")
mul.grid(row=3,column=1)

div = tk.Radiobutton(wdow,text="/",variable=operator_var,value="/")
div.grid(row=4,column=1)

submit_button = tk.Button(wdow,text="Submit!",command=do_math).grid(column=1,row=5)
#2 number entry

first_number_variable = tk.IntVar(wdow)
second_number_variable = tk.IntVar(wdow)

first_number_input = tk.Entry(wdow,textvariable=first_number_variable).grid(column=0,row=2)
second_number_input = tk.Entry(wdow,textvariable=second_number_variable).grid(column=2,row=2)
wdow.mainloop()