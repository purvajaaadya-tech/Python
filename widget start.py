from tkinter import *
from datetime import date

r = Tk()
r.title('Getting started with widgets')
r.geometry('400x300')

l = Label(text = "Hey there!", fg = "white", bg = "#072F5F", height = 1, width = 300)

nl = Label(text = "Full name", bg = "#3895D3")
ne = Entry()

def d():
    n = ne.get()
    global m
    m = "Welcome to the application! \nToday's date is: "
    g = "Hello "+n+"\n"
    tb.insert(END, g)
    tb.insert(END, m)
    tb.insert(END, date.today())

tb = Text(height = 3)

b = Button(text = "Begin", command = d, height = 1, bg = "#1261A0", fg = "black")

l.pack()
nl.pack()
ne.pack()
b.pack()
tb.pack()

r.mainloop()