#Om Ghansyam Bhamare SE A 3
#Experiment 3
from tkinter import *
from tkinter import *
import tkinter.messagebox as tmsg

top = Tk()

top.geometry("600x400")

c = Canvas(top, bg="pink", width="600", height="400")

reg = Label(top, text="Register Here...").place(x=10, y=10)
uname = Label(top, text="Username").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password" ).place(x=30, y=130)
e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)
e3 = Entry(top, width=20,show="*").place(x=100, y=130)


def conform():
    tmsg.showinfo("Register Successful!")


var = StringVar()
var.set("Radio")
Gender= Label(top, text="Gender").place(x=30, y=170)

radio = Radiobutton(text="Male", padx=14, variable=var, value="Male").place(x=90, y=170)
radio = Radiobutton(text="Female", padx=14, variable=var, value="Female").place(x=180, y=170)
radio = Radiobutton(text="Other", padx=14, variable=var,value="Other").place(x=280, y=170)

termAndCondition = Checkbutton(text="I Read All term and condition?").place(x=30, y=220)

sbmitbtn = Button(top, text="Submit", activebackground="pink",
                  activeforeground="blue",command=conform).place(x=30, y=260)
c.pack()
top.mainloop()
