import tkinter as tk
from tkinter import*
mainscreen=tk.Tk()
mainscreen.geometry("500x300")
def slider():
    print(w1.get(),w2.get())

w1=tk.Scale(mainscreen, from_=0,to=40,tickinterval=8)
w1.set(39)
w1.pack()
w2=tk.Scale(mainscreen, from_=20,to=440,tickinterval=42,length=7000,orient=HORIZONTAL)
w2.set(390)
w2.pack()
bi=tk.Button(mainscreen,text="show",command=slider).pack()
mainscreen.mainloop()
