from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

r = Tk()
r.title("Denomination Counter")
r.configure(bg="light blue")
r.geometry("650x400")

u = Image.open("app_img.jpg")
u = u.resize((300, 300))
i = ImageTk.PhotoImage(u)

l = Label(r, i=i, bg="light blue")
l.place(x=180, y=20)

l1 = Label(r, text="Hey User! Welcome to Denomination Counter Application.", bg="light blue")
l1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    mb = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if mb == "ok":
        tw()

b1 = Button(r, text="Let's get started!", command=msg, bg="brown", fg="white")
b1.place(x=260, y=360)

def tw():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    l = Label(top, text="Enter total amount", bg="light grey")
    e = Entry(top)

    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )

    lbl1 = Label(top, text="2000", bg="light grey")
    lbl2 = Label(top, text="500", bg="light grey")
    lbl3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calc():
        try:
            a = int(e.get())

            n2000 = a // 2000
            a %= 2000

            n500 = a // 500
            a %= 500

            n100 = a // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(n2000))
            t2.insert(END, str(n500))
            t3.insert(END, str(n100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
        top,
        text="Calculate",
        command=calc,
        bg="brown",
        fg="white"
    )

    l.place(x=230, y=50)
    e.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    lbl1.place(x=180, y=200)
    lbl2.place(x=180, y=230)
    lbl3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

r.mainloop()