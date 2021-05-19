#Om Ghanshyam Bhamare SE A 3
# Assignmenet 3 Q1
from tkinter import *
root = Tk()
root.geometry("455x233")
def col1():
    root['background']='pink'
    pass
def col2():
    root['background']='red'
    pass
def col3():
    root['background']='blue'
    pass

but1=Button(text="Pink",activebackground="pink",command=col1).place(x=30,y=100)
but2=Button(text="Red",activebackground="red",command=col2).place(x=130,y=100)
but3=Button(text="Blue",activebackground="blue",command=col3).place(x=230,y=100)



root.title("Assignmet 3 Q1")
root.mainloop()