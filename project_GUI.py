import tkinter
from tkinter import *
wd = tkinter.Tk()

wd.title("Dashboard")
wd.geometry("500x500")
#wd.configure(background="grey")
wd.config(bg="skyblue")
#l1=Label(text="Rita Dhoble",font=("Cursive",30,"italic"),bg="orange")
f=("Conic Sans MS",17,"italic")
l1=Label(text="Orange",font=f,bg="orange",fg="white")
l1.pack()

l2=Label(text="White", font=("calabric",20,"bold"),bg="white",fg="blue")
l2.pack()

l3=Label(text="Green", font=("Times of roman",20,"italic"),bg="green", fg="white")
l3.pack()

wd.mainloop()