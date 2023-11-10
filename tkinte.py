from tkinter import*
from tkinter import messagebox
def f1():
    messagebox.showinfo("Demo","You have clicked RED button")
def f2():
    messagebox.showinfo("Demo","You have clicked BLUE button")
def f3():
    messagebox.showinfo("Demo","You have clicked ORANGE button")
def f4():
    messagebox.showinfo("Demo","You have clicked YELLOW button")
top=Tk()
top.geometry("500x500")
b1=Button(top,text="Red",command=f1,activeforeground="Pink",activebackground="Red",pady=10)
b1.pack(side=TOP)
b2=Button(top,text="blue",command=f2,activeforeground="Pink",activebackground="blue",pady=10)
b2.pack(side=BOTTOM)
b3=Button(top,text="Orange",command=f3,activeforeground="Pink",activebackground="Orange",pady=10)
b3.pack(side=RIGHT)
b4=Button(top,text="Yellow",command=f4,activeforeground="Pink",activebackground="Yellow",pady=10)
b4.pack(side=LEFT)
top.mainloop()
i am going to request main branch
