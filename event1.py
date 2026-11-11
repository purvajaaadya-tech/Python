from tkinter import *

w = Tk()
w.title("Event Handler")
w.geometry("100x100")

def hk(e):
    """Print the character associated to the key pressed"""
    print(e.char)

w.bind("<Key>", hk)

def hc(e):
    print("\nThe button was clicked!")

b = Button(text="Click me!")
b.pack()

b.bind("<Button-1>", hc)

w.mainloop()