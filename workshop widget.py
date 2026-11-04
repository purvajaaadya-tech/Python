from tkinter import *
from datetime import date

r = Tk()
r.title('Widget Workshop')
r.geometry('400x300')

l = Label(text = "Hi!", fg = "white", bg = "#075F17", height = 1, width = 300)

nl = Label(text = "Full name", bg = "#38D359")
ne = Entry()

def d():
    n = ne.get()
    global m
    m = "Welcome to the widget workshop! \nToday's workshop date is: "
    g = "Hello "+n+"\n"
    tb.insert(END, g)
    tb.insert(END, m)
    tb.insert(END, date.today())

tb = Text(height = 3)

b = Button(text = "CHECK", command = d, height = 1, bg = "#12A031", fg = "black")

l.pack()
nl.pack()
ne.pack()
b.pack()
tb.pack()

r.mainloop()