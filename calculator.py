from tkinter import*

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnclear():
    global operator
    operator=""
    text_input.set("")

def equalsum():
    global operator
    sums=str(eval(operator))
    text_input.set(sums)
    operator=sums


cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()

txtdisplay=Entry(cal,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

bttn7=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda:btnclick(7)).grid(row=1,column=0)
bttn8=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda:btnclick(8)).grid(row=1,column=1)
bttn9=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda:btnclick(9)).grid(row=1,column=2)
bttn6=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda:btnclick(6)).grid(row=2,column=2)
bttn5=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda:btnclick(5)).grid(row=2,column=1)
bttn4=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda:btnclick(4)).grid(row=2,column=0)
bttn3=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda:btnclick(3)).grid(row=3,column=2)
bttn2=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda:btnclick(2)).grid(row=3,column=1)
bttn1=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda:btnclick(1)).grid(row=3,column=0)
bttn0=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda:btnclick(0)).grid(row=4,column=1)


add=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda:btnclick('+')).grid(row=1,column=3)
sub=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda:btnclick('-')).grid(row=2,column=3)
mul=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",command=lambda:btnclick('*')).grid(row=3,column=3)
div=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda:btnclick('/')).grid(row=4,column=3)
equal=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=equalsum).grid(row=4,column=2)
clear=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",command=btnclear).grid(row=4,column=0)
cal.mainloop()
