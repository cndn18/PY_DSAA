from tkinter import*
import tkinter.messagebox as tkMessageBox

root=Tk()
root.geometry("1350x750+0+0")
root.title("system to manage")
root.configure(bg="pink")

#--------------- frames ------------------

Tops=Frame(root,bd=15,height=100,width=1300,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,bd=8,height=650,width=900,relief="raise")
f1.pack(side=LEFT)

f2=Frame(root,bd=8,height=650,width=440,relief="raise")
f2.pack(side=RIGHT)

f11=Frame(f1,bd=8,height=350,width=900,relief="raise")
f11.pack(side=TOP)

f12=Frame(f1,bd=8,height=300,width=900,relief="raise")
f12.pack(side=BOTTOM)

f11a=Frame(f11,bd=8,height=350,width=440,relief="raise")
f11a.pack(side=LEFT)

f11b=Frame(f11,bd=8,height=350,width=455,relief="raise")
f11b.pack(side=RIGHT)

f12a=Frame(f12,bd=8,height=300,width=440,relief="raise")
f12a.pack(side=LEFT)

f12b=Frame(f12,bd=8,height=300,width=455,relief="raise")
f12b.pack(side=RIGHT)

f2a=Frame(f2,bd=8,height=450,width=440,relief="raise")
f2a.pack(side=TOP)

f2b=Frame(f2,bd=8,height=200,width=440,relief="raise")
f2b.pack(side=BOTTOM)

f1.configure(bg="green")
f2.configure(bg="green")

heading=Label(Tops,text="YOUR FAVOURITE SPOT",font=('arial',60,'bold'),bd=10)
heading.grid(row=0,column=0)


#----------------------------------------------functions------------------------------------------------------

def exitpls():
    tkMessageBox.askquestion("wanna exit,are you sure you wanna exit",icon='warning')


#---------------------------------------------------checkbuttons------------------------------------------------------
Var1 = IntVar()
Var1.set("0")

Var2 = IntVar()
Var2.set("0")

Var3 = IntVar()
Var3.set("0")

Var3 = IntVar()
Var3.set("0")

Var4 = IntVar()
Var4.set("0")

Var5 = IntVar()
Var5.set("0")

Var6 = IntVar()
Var6.set("0")

Var7 = IntVar()
Var7.set("0")

Var8 = IntVar()
Var8.set("0")

Var9 = IntVar()
Var9.set("0")

Var10 = IntVar()
Var10.set("0")

Var11 = IntVar()
Var11.set("0")

Var12 = IntVar()
Var12.set("0")

Var13 = IntVar()
Var13.set("0")

Var14 = IntVar()
Var14.set("0")




cocacola=Checkbutton(f11a,text="Cocacola",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var1).grid(row=0,sticky=W)
spirit=Checkbutton(f11a,text="Spirit",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var2).grid(row=1,sticky=W)
fanta=Checkbutton(f11a,text="Fanta",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var3).grid(row=2,sticky=W)
maaza=Checkbutton(f11a,text="Maaza",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var4).grid(row=3,sticky=W)
thumpsup=Checkbutton(f11a,text="ThumpsUP",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var5).grid(row=4,sticky=W)
limew=Checkbutton(f11a,text="LimeSoda",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var6).grid(row=5,sticky=W)
sexOTB=Checkbutton(f11a,text="SOTB",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var7).grid(row=6,sticky=W)
vanilla=Checkbutton(f11b,text="Vanilla cup",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var8).grid(row=0,sticky=W)
rasberry=Checkbutton(f11b,text="Rasberry Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var9).grid(row=1,sticky=W)
strawberry=Checkbutton(f11b,text="Strawberry Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var10).grid(row=2,sticky=W)
chocalate=Checkbutton(f11b,text="Chocolate Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var11).grid(row=3,sticky=W)
mango_flavour=Checkbutton(f11b,text="Mango Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var12).grid(row=4,sticky=W)
butterscotch=Checkbutton(f11b,text="Butter Scotch",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var13).grid(row=5,sticky=W)
mutka_kulfi=Checkbutton(f11b,text="Mutka Kulfi",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var14).grid(row=6,sticky=W)




#---------------------------------------------------------buttons----------------------------------------------------------------------------

exit=Button(f2b,text="EXIT",command=exitpls,font=('arial',16,'bold'))
exit.pack()


root.mainloop()
