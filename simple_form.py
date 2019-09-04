from tkinter import*

def command1(event):
    if entry1.get()=='admin' and entry2.get()=='password' or entry1.get()=='test' and entry2.get()=='pass':
        root.deiconify()
        root.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

#def command3():




root=Tk()
top=Toplevel()

top.geometry("900x760")
top.title('Dogs Pet')
top.configure(background='white')
photo1=PhotoImage(file='CLARUSBU.GIF')
photo=Label(top,image=photo1,bg='white')
lbl1=Label(top,text='Username',font=('Helevtica',10))
entry1=Entry(top)
lbl2=Label(top,text='Password',font=('Helevtica',10))
entry2=Entry(top,show="*")

button2=Button(top,text='Cancel',command=lambda:command2())

entry2.bind('<Return>',command1)

lbl3=Label(top,text='Copyright Login Screen',font=('Arial',9))
photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

root.title('Main Screen')
root.configure(background='white')
root.geometry("855x690")

root.withdraw()
root.mainloop()








