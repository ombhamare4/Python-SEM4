from tkinter import *  
top = Tk()  

top.geometry("600x400")  

c = Canvas(top,bg = "pink",width = "600",height="400")  

reg = Label(top,text="Register Here...").place(x=10,y=10)
uname = Label(top, text = "Username").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30,y = 90)
password = Label(top, text = "Password").place(x = 30,y = 130)  
e1 = Entry(top,width = 20).place(x = 100, y = 50)  
e2 = Entry(top, width = 20).place(x = 100, y = 90) 
e3 = Entry(top, width = 20).place(x = 100, y = 130)  


sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 200)  
c.pack()  
top.mainloop()  