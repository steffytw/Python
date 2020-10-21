import tkinter as tk
import tkinter.ttk as ttk


window = tk.Tk()

window.title("Calculator")

exp=""
text = tk.StringVar()

def press(num):
    global exp
    exp +=str(num)
    text.set(exp)

def equal():
    global exp
    data =str(eval(exp))
    text.set(data)

def clear():
    global exp
    exp=""
    text.set(exp)



entry1= ttk.Entry(window,justify="right",textvariable=text)
entry1.grid(row=0, columnspan=4,sticky="nsew")

button_7 = ttk.Button(window,text="7",command = lambda : press(7))
button_7.grid(row=1,column=0)

button_8 = ttk.Button(window,text="8",command = lambda : press(8))
button_8.grid(row=1,column=1)

button_9 = ttk.Button(window,text="9",command = lambda : press(9))
button_9.grid(row=1,column=2)

button_div = ttk.Button(window,text="/",command = lambda : press("/"))
button_div.grid(row=1,column=3)

button_4 = ttk.Button(window,text="4",command = lambda : press(4))
button_4.grid(row=2,column=0)

button_5 = ttk.Button(window,text="5",command = lambda : press(5))
button_5.grid(row=2,column=1)

button_6 = ttk.Button(window,text="6",command = lambda : press(6))
button_6.grid(row=2,column=2)

button_mul = ttk.Button(window,text="*",command = lambda : press("*"))
button_mul.grid(row=2,column=3)

button_1 = ttk.Button(window,text="1",command = lambda : press(1))
button_1.grid(row=3,column=0)

button_2 = ttk.Button(window,text="2",command = lambda : press(2))
button_2.grid(row=3,column=1)

button_3 = ttk.Button(window,text="3",command = lambda : press(3))
button_3.grid(row=3,column=2)

button_sub = ttk.Button(window,text="-",command = lambda : press("-"))
button_sub.grid(row=3,column=3)

button_0 = ttk.Button(window,text="0",command = lambda : press(0))
button_0.grid(row=4,column=0)

button_dec = ttk.Button(window,text=".",command = lambda : press("."))
button_dec.grid(row=4,column=1)

button_clr = ttk.Button(window,text="c",command = clear)
button_clr.grid(row=4,column=2)

button_add = ttk.Button(window,text="+",command = lambda : press("+"))
button_add.grid(row=4,column=3)



button_equal = ttk.Button(window,text="=",command = equal)
button_equal.grid(row=5,columnspan=4,sticky="nsew")


window.mainloop()

