import tkinter as tk

window = tk.Tk()
window["bg"] = "black"
window.geometry("200x400")
show_num = tk.StringVar(window, "0")
first_num = ""
second_num = ""
is_negative = False
operator = tk.StringVar(window,"")
def negy():
    global is_negative
    print(is_negative)
    if not is_negative:
        is_negative = True
        return show_num.set(f"-{show_num.get()}")
    is_negative = False
    return  show_num.set(show_num.get().strip("-"))

lol = tk.Label(
    window,
    textvariable=show_num,
    font=("Seven Segment", 45),
  
    width=8,
    border=0,
    borderwidth=0,
    anchor="e"
    )

lol.grid(column=0,row=0)
nums = []
frame = tk.Frame(window, height=30, width=100,background="black")
frame.grid(column=0,row=1)

def do_math():
    global nums
   
    print(operator.get())
    match operator.get():
        case "+":
           
            show_num.set(str(nums[0] + nums[1]))
        case "-":
             show_num.set(str(nums[0] - nums[1]))
        case "x":
             show_num.set(str(nums[0] * nums[1]))
        case "/":
             show_num.set(str(nums[0] / nums[1]))

def operator_var(sign:str):
    global nums
  
    operator.set(sign)
    if len(nums) > 2:
        del nums[::]
    
    nums.append(int(show_num.get()))
    print(nums)
    show_num.set("0")
    print(nums)

C = tk.Button(window, text="C",command= lambda: show_num.set("0"))
C.grid(column=0,row=2,sticky="w")
nine = tk.Button(window, text="9",command= lambda: show_num.set(f"{show_num.get()}9"))
nine.grid(column=0,row=2,)

eight = tk.Button(window, text="8",command= lambda: show_num.set(f"{show_num.get()}8"))
eight.grid(column=0,row=2,sticky="e")

seven = tk.Button(window, text="7",command= lambda: show_num.set(f"{show_num.get()}7"))
seven.grid(column=0,row=3,sticky="w")

six = tk.Button(window,background="black", text="6",command= lambda: show_num.set(f"{show_num.get()}6"))
six.grid(column=0,row=3,)

five = tk.Button(window,background="black", text="5",command= lambda: show_num.set(f"{show_num.get()}5"))
five.grid(column=0,row=3,sticky="e",)

neg = tk.Button(window,background="black", text="+/-",command=negy, width=1)
neg.grid(column=0,row=4,sticky="w")

four = tk.Button(window,background="black", text="4",command= lambda: show_num.set(f"{show_num.get()}4"))
four.grid(column=0,row=4,)

three = tk.Button(window,background="black", text="3",command= lambda: show_num.set(f"{show_num.get()}3"))
three.grid(column=0,row=4,sticky="e",)

two = tk.Button(window,background="black", text="2",command= lambda: show_num.set(f"{show_num.get()}2"))
two.grid(column=0,row=5,sticky="w")

one = tk.Button(window,background="black", text="1",command= lambda: show_num.set(f"{show_num.get()}1"))
one.grid(column=0,row=5,)

zero = tk.Button(window,background="black", text="0",command= lambda: show_num.set(f"{show_num.get()}0"))
zero.grid(column=0,row=5,sticky="e")

plus = tk.Button(window,background="black", text="+",command= lambda: operator_var("+"))
plus.grid(column=0,row=6,sticky="w")

minus = tk.Button(window,background="black", text="-",command= lambda: operator_var("-"))
minus.grid(column=0,row=6,)

mul = tk.Button(window,background="black", text="x",command= lambda: operator_var("x"))
mul.grid(column=0,row=6,sticky="e")

div = tk.Button(window,background="black", text="÷",command= lambda: operator_var("/"))
div.grid(column=0,row=7,sticky="w")

eq = tk.Button(window,background="black", text="=",command= do_math)
eq.grid(column=0,row=7,)
window.call()
window.mainloop()
