import tkinter as tk
from random import randint


window = tk.Tk()

check_is_num_there_list = []

butt_list = []

tot = 0

def lol(n):
    global tot
    if butt_list[n]["state"] == "normal":
        tot += 1
    butt_list[n].config(state="disabled")
    print(tot)

def check():
    
    global time
    if tot != 25:
        time.set(time.get() + 1)
    window.after(1000,check)
    
def display_5_rows(col: int):
    for iterate in range(1, 6):
        while True:
            num = randint(0, 999)
            if num not in check_is_num_there_list:
                break
        check_is_num_there_list.append(num)

        button = tk.Button(window, text=str(num))
        button.grid(column=col, row=iterate)

        button.bind("<Button-1>", lambda event, num=len(butt_list): lol(num))

        butt_list.append(button)

for col in range(5):
    display_5_rows(col)

time = tk.IntVar(window,0)

time_count_label = tk.Label(window,textvariable=time)
time_count_label.grid(column=2,row=6)

window.after(1000,check)
window.mainloop()
