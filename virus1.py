from tkinter import *
from tkinter import messagebox

r = Tk()
r.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

b = Button(r, text="Scan for Virus", command=msg)
b.place(x=40, y=80)

r.mainloop()