import tkinter as tk
from tkinter import simpledialog,messagebox
import sqlite3
window = tk.Tk()

def des(id=0):
    arr[id][0].destroy()
    arr[id][1].destroy()

def saveit(filename):
    global lol
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("create table if not exists todo (task text);")
    conn.commit()
    cur.executemany("insert into todo values(?)",lol)
    conn.commit()

def openit(filename):
    global lol
    global butt
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("select * from todo")
    for i in cur.fetchall():
        print(i)
        factory(i[0])
    butt.grid(row=tot + 1)
def takecare(lol=None):
    global butt

    butt.grid(row=tot + 1)
    factory(simpledialog.askstring(title="Duh",prompt="What should task be")) # type: ignore
arr = []

lol = []
tot = 0
def factory(text:str):
    global tot
    arr.append([tk.Label(window,text=text),tk.Button(window,text="🗑️",command=lambda g=tot: des(g))])
    arr[tot][0].grid(column=0,row=tot)
    arr[tot][1].grid(column=1,row=tot)
    tot += 1
    lol.append([text])

window.title("Hi")
butt = tk.Button(window,text="Add more in to do",command= takecare)
butt.grid(row=tot + 1)
window.bind("<Command-s>",lambda event: saveit(simpledialog.askstring("Save","Enter file name?")))
window.bind("<Command-o>",lambda event: openit(simpledialog.askstring("Open","Enter file name?")))
window.mainloop()