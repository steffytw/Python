from tkinter import *

window =Tk()
window.title("GUI tkinter")

label1 = Label(window, text="hello World")

label1.pack()
window.geometry("300x300")
window.mainloop()