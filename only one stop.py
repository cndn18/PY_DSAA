from tkinter import*
import tkinter.messagebox as tkMessageBox
import time;
import datetime
import random

root=Tk()
root.geometry("1250x750+0+0")
root.title("BILLING INTERFACE")
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

f2a=Frame(f2,bd=8,height=480,width=440,relief="raise")
f2a.pack(side=TOP)

f2b=Frame(f2,bd=8,height=170,width=440,relief="raise")
f2b.pack(side=BOTTOM)

f1.configure(bg="green")
f2.configure(bg="green")

heading=Label(Tops,text="YOUR FAVOURITE SPOT",font=('arial',60,'bold'),bd=10,anchor='w')
heading.grid(row=0,column=0)


#----------------------------------------------functions------------------------------------------------------

def exit_pls():
    exit=tkMessageBox.askyesno("wanna exit?","are you sure you wanna exit",icon='warning')
    if exit>0:
        root.destroy()
        return

def start_again():
    codTV.set(" ")
    coiTV.set(" ")
    stTV.set(" ")
    ptTV.set(" ")
    subtTV.set(" ")
    TotalcTV.set(" ")
    labeltext.delete("1.0",END)
    
    cocacolaTV.set("0")
    spritTV.set('0')
    fantaTV.set('0')
    maazaTV.set('0')
    thumpsupTV.set('0')
    limewTV.set('0')
    sexotbTV.set('0')

    vanillaTV.set('0')
    rasberryTV.set('0')
    strawberryTV.set('0')
    chocolateTV.set('0')
    mangoTV.set('0')
    butterscotchTV.set('0')
    mutkaTV.set('0')

    Var1.set("0")
    Var2.set("0")
    Var3.set("0")
    Var3.set("0")
    Var4.set("0")
    Var5.set("0")
    Var6.set("0")
    Var7.set("0")
    Var8.set("0")
    Var9.set("0")
    Var10.set("0")
    Var11.set("0")
    Var12.set("0")
    Var13.set("0")
    Var14.set("0")

    cocacolaE.configure(state=DISABLED)
    spiritE.configure(state=DISABLED)
    fantaE.configure(state=DISABLED)
    maazaE.configure(state=DISABLED)
    thumpsupE.configure(state=DISABLED)
    limewE.configure(state=DISABLED)
    sexOTBE.configure(state=DISABLED)

    vanillaE.configure(state=DISABLED)
    rasberryE.configure(state=DISABLED)
    strawberryE.configure(state=DISABLED)
    chocolateE.configure(state=DISABLED)
    mangoE.configure(state=DISABLED)
    butterscotchE.configure(state=DISABLED)
    mutkaE.configure(state=DISABLED)

def amount_to_be_paid():
    a1=float(cocacolaTV.get())
    a2=float(spritTV.get())
    a3=float(fantaTV.get())
    a4=float(maazaTV.get())
    a5=float(thumpsupTV.get())
    a6=float(limewTV.get())
    a7=float(sexotbTV.get())

    b1=float(vanillaTV.get())
    b2=float(rasberryTV.get())
    b3=float(strawberryTV.get())
    b4=float(chocolateTV.get())
    b5=float(mangoTV.get())
    b6=float(butterscotchTV.get())
    b7=float(mutkaTV.get())


    pod=(a1*19.20)+(a2*20.50)+(a3*18)+(a4*21.60)+(a5*23.20)+(a6*12.30)+(a7*200.10)
    poi=(b1*25.20)+(b2*35.50)+(b3*47)+(b4*61.60)+(a5*27.20)+(a6*70.30)+(a7*150.10)

    drinksprice="$",str('%.2f'%(pod))
    icecreamprice="$",str('%.2f'%(poi))
    codTV.set(drinksprice)
    coiTV.set(icecreamprice)
    SC="$",str('%.2f'%(1.59))
    stTV.set(SC)

    subtotal="$",str('%.2f'%(pod+poi+1.59))
    subtTV.set(subtotal)
    tax="$",str('%.2f'%((pod+poi+1.59)*0.15))
    ptTV.set(tax)

    tt=(pod+poi+1.59)*0.15
    tc="$",str('%.2f'%(pod+poi+1.59+tt))
    TotalcTV.set(tc)
    
    
def bill_please():
    labeltext.delete("1.0",END)
    x=random.randint(10456,500067)
    randomRef=str(x)
    Receipt_ref.set("BILL"+randomRef)

    labeltext.insert(END,'Receipt_Ref:\t'+Receipt_ref.get()+'\t\t\t\t\t'+DateOfOrder.get()+"\n")
    labeltext.insert(END,'Items:\t\t\t\t\t\t'+"NO. Of Items\n\n")
    labeltext.insert(END,'Cocacola:\t\t\t\t\t\t'+cocacolaTV.get()+"\n")
    labeltext.insert(END,'Spirit:\t\t\t\t\t\t'+spritTV.get()+"\n")
    labeltext.insert(END,'Fanta:\t\t\t\t\t\t'+fantaTV.get()+"\n")
    labeltext.insert(END,'Maaza:\t\t\t\t\t\t'+maazaTV.get()+"\n")
    labeltext.insert(END,'ThumpsUp:\t\t\t\t\t\t'+thumpsupTV.get()+"\n")
    labeltext.insert(END,'LimeSoda:\t\t\t\t\t\t'+limewTV.get()+"\n")
    labeltext.insert(END,'SOTB:\t\t\t\t\t\t'+sexotbTV.get()+"\n")
    labeltext.insert(END,'Vanilla Cup:\t\t\t\t\t\t'+vanillaTV.get()+"\n")
    labeltext.insert(END,'Rasberry Flavour:\t\t\t\t\t\t'+rasberryTV.get()+"\n")
    labeltext.insert(END,'Strawberry Flavour:\t\t\t\t\t\t'+strawberryTV.get()+"\n")
    labeltext.insert(END,'Chocolate Flavour:\t\t\t\t\t\t'+chocolateTV.get()+"\n")
    labeltext.insert(END,'Mango Flavour:\t\t\t\t\t\t'+mangoTV.get()+"\n")
    labeltext.insert(END,'Butter Scotch:\t\t\t\t\t\t'+butterscotchTV.get()+"\n")
    labeltext.insert(END,'Mutka Kulfi:\t\t\t\t\t\t'+mutkaTV.get()+"\n")
    labeltext.insert(END,'Cost of Drinks:\t\t'+codTV.get()+'\tTax Paid\t\t'+ptTV.get()+"\n")
    labeltext.insert(END,'Cost of Ice-Cream:\t\t'+coiTV.get()+'\tSubTotal\t\t'+subtTV.get()+"\n")
    labeltext.insert(END,'Service Charge:\t\t'+stTV.get()+'\tTotal Cost\t\t'+TotalcTV.get()+"\n")
    
     
    
    

def checkbuton_value():
    if Var1.get()==1:
        cocacolaE.configure(state=NORMAL)
    elif Var1.get()==0:
        cocacolaE.configure(state=DISABLED)
        cocacolaTV.set("0")
    if Var2.get()==1:
        spiritE.configure(state=NORMAL)
    elif Var2.get()==0:
        spiritE.configure(state=DISABLED)
        spritTV.set('0')
    if Var3.get()==1:
        fantaE.configure(state=NORMAL)
    elif Var3.get()==0:
        fantaE.configure(state=DISABLED)
        fantaTV.set('0')
    if Var4.get()==1:
        maazaE.configure(state=NORMAL)
    elif Var4.get()==0:
        maazaE.configure(state=DISABLED)
        maazaTV.set('0')
    if Var5.get()==1:
        thumpsupE.configure(state=NORMAL)
    elif Var5.get()==0:
        thumpsupE.configure(state=DISABLED)
        thumpsupTV.set('0')
    if Var6.get()==1:
        limewE.configure(state=NORMAL)
    elif Var6.get()==0:
        limewE.configure(state=DISABLED)
        limewTV.set('0')
    if Var7.get()==1:
        sexOTBE.configure(state=NORMAL)
    elif Var7.get()==0:
        sexOTBE.configure(state=DISABLED)
        sexotbTV.set('0')
        
    if Var8.get()==1:
        vanillaE.configure(state=NORMAL)
    elif Var8.get()==0:
        vanillaE.configure(state=DISABLED)
        vanillaTV.set('0')
    if Var9.get()==1:
        rasberryE.configure(state=NORMAL)
    elif Var9.get()==0:
        rasberryE.configure(state=DISABLED)
        rasberryTV.set('0')
    if Var10.get()==1:
        strawberryE.configure(state=NORMAL)
    elif Var10.get()==0:
        strawberryE.configure(state=DISABLED)
        strawberryTV.set('0')
    if Var11.get()==1:
         chocolateE.configure(state=NORMAL)
    elif Var11.get()==0:
         chocolateE.configure(state=DISABLED)
         chocolateTV.set('0')
    if Var12.get()==1:
        mangoE.configure(state=NORMAL)
    elif Var12.get()==0:
        mangoE.configure(state=DISABLED)
        mangoTV.set('0')
    if Var13.get()==1:
        butterscotchE.configure(state=NORMAL)
    elif Var13.get()==0:
        butterscotchE.configure(state=DISABLED)
        butterscotchTV.set('0')
    if Var14.get()==1:
        mutkaE.configure(state=NORMAL)
    elif Var14.get()==0:
        mutkaE.configure(state=DISABLED)
        mutkaTV.set('0')


#-------------------------------------------------------variable_entry-------------------------------------------------------------


cocacolaTV=StringVar()
spritTV=StringVar()
fantaTV=StringVar()
maazaTV=StringVar()
thumpsupTV=StringVar()
limewTV=StringVar()
sexotbTV=StringVar()

vanillaTV=StringVar()
rasberryTV=StringVar()
strawberryTV=StringVar()
chocolateTV=StringVar()
mangoTV=StringVar()
butterscotchTV=StringVar()
mutkaTV=StringVar()

cocacolaTV.set("0")
spritTV.set('0')
fantaTV.set('0')
maazaTV.set('0')
thumpsupTV.set('0')
limewTV.set('0')
sexotbTV.set('0')

vanillaTV.set('0')
rasberryTV.set('0')
strawberryTV.set('0')
chocolateTV.set('0')
mangoTV.set('0')
butterscotchTV.set('0')
mutkaTV.set('0')

codTV=StringVar()
coiTV=StringVar()
stTV=StringVar()
ptTV=StringVar()
subtTV=StringVar()
TotalcTV=StringVar()
DateOfOrder=StringVar()
Receipt_ref=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()
Var7 = IntVar()
Var8 = IntVar()
Var9 = IntVar()
Var10 = IntVar()
Var11 = IntVar()
Var12 = IntVar()
Var13 = IntVar()
Var14 = IntVar()

#--------------------------------------------------checkbuttons-----------------------------------------------------------------------



cocacola=Checkbutton(f11a,text="Cocacola",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var1,command=checkbuton_value).grid(row=0,sticky=W)
spirit=Checkbutton(f11a,text="Spirit",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var2,command=checkbuton_value).grid(row=1,sticky=W)
fanta=Checkbutton(f11a,text="Fanta",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var3,command=checkbuton_value).grid(row=2,sticky=W)
maaza=Checkbutton(f11a,text="Maaza",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var4,command=checkbuton_value).grid(row=3,sticky=W)
thumpsup=Checkbutton(f11a,text="ThumpsUP",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var5,command=checkbuton_value).grid(row=4,sticky=W)
limew=Checkbutton(f11a,text="LimeSoda",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var6,command=checkbuton_value).grid(row=5,sticky=W)
sexOTB=Checkbutton(f11a,text="SOTB",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var7,command=checkbuton_value).grid(row=6,sticky=W)

vanilla=Checkbutton(f11b,text="Vanilla cup",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var8,command=checkbuton_value).grid(row=0,sticky=W)
rasberry=Checkbutton(f11b,text="Rasberry Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var9,command=checkbuton_value).grid(row=1,sticky=W)
strawberry=Checkbutton(f11b,text="Strawberry Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var10,command=checkbuton_value).grid(row=2,sticky=W)
chocalate=Checkbutton(f11b,text="Chocolate Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var11,command=checkbuton_value).grid(row=3,sticky=W)
mango_flavour=Checkbutton(f11b,text="Mango Flavour",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var12,command=checkbuton_value).grid(row=4,sticky=W)
butterscotch=Checkbutton(f11b,text="Butter Scotch",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var13,command=checkbuton_value).grid(row=5,sticky=W)
mutka_kulfi=Checkbutton(f11b,text="Mutka Kulfi",font=('arial',16,'bold'),bd=10,onvalue=1,offvalue=0,variable = Var14,command=checkbuton_value).grid(row=6,sticky=W)


#------------------------------------------------------------entry------------------------------------------------------------------------

cocacolaE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=cocacolaTV)
cocacolaE.grid(row=0,column=3)
spiritE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=spritTV)
spiritE.grid(row=1,column=3)
fantaE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=fantaTV)
fantaE.grid(row=2,column=3)
maazaE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=maazaTV)
maazaE.grid(row=3,column=3)
thumpsupE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=thumpsupTV)
thumpsupE.grid(row=4,column=3)
limewE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=limewTV)
limewE.grid(row=5,column=3)
sexOTBE=Entry(f11a,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=sexotbTV)
sexOTBE.grid(row=6,column=3)

vanillaE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=vanillaTV)
vanillaE.grid(row=0,column=3)
rasberryE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=rasberryTV)
rasberryE.grid(row=1,column=3)
strawberryE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=strawberryTV)
strawberryE.grid(row=2,column=3)
chocolateE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=chocolateTV)
chocolateE.grid(row=3,column=3)
mangoE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=mangoTV)
mangoE.grid(row=4,column=3)
butterscotchE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=butterscotchTV)
butterscotchE.grid(row=5,column=3)
mutkaE=Entry(f11b,state=DISABLED,font=('arial',16,'bold'),bd=8,justify="left",width=7,textvariable=mutkaTV)
mutkaE.grid(row=6,column=3)



#-------------------------------------------------Total----------------------------------------------------------

cod=Label(f12a,text='Cost of drinks   ',font=('arial',16,'bold'))
cod.grid(row=0,sticky=W)
codE=Entry(f12a,font=('arial',16,'bold'),bd=8,width=10,textvariable=codTV,justify="left")
codE.grid(row=0,column=3)

coi=Label(f12a,text='Cost of Ice-cream   ',font=('arial',16,'bold'))
coi.grid(row=1,sticky=W)
coiE=Entry(f12a,font=('arial',16,'bold'),bd=8,width=10,textvariable=coiTV,justify="left")
coiE.grid(row=1,column=3)

st=Label(f12a,text='Service Tax   ',font=('arial',16,'bold'))
st.grid(row=2,sticky=W)
stE=Entry(f12a,font=('arial',16,'bold'),bd=8,width=10,textvariable=stTV,justify="left")
stE.grid(row=2,column=3)

pt=Label(f12b,text='Paid Tax   ',font=('arial',16,'bold'))
pt.grid(row=0,sticky=W)
ptE=Entry(f12b,font=('arial',16,'bold'),bd=8,width=10,textvariable=ptTV,justify="left")
ptE.grid(row=0,column=3)

subt=Label(f12b,text='Sub Total   ',font=('arial',16,'bold'))
subt.grid(row=1,sticky=W)
subtE=Entry(f12b,font=('arial',16,'bold'),bd=8,width=10,textvariable=subtTV,justify="left")
subtE.grid(row=1,column=3)

Totalc=Label(f12b,text='Total Cost   ',font=('arial',16,'bold'))
Totalc.grid(row=2,sticky=W)
TotalcE=Entry(f12b,font=('arial',16,'bold'),bd=8,width=10,textvariable=TotalcTV,justify="left")
TotalcE.grid(row=2,column=3)

#--------------------------------------------------Receipt---------------------------------------------------------

labelrec=Label(f2a,text='RECEIPT:',font=('arial',16,'bold'))
labelrec.grid(row=0,column=0,sticky=W)
labeltext=Text(f2a,font=('arial',11,'bold'),bd=8,width=60,height=23)
labeltext.grid(row=1,column=0)



#---------------------------------------------------------buttons----------------------------------------------------------------------------

total=Button(f2b,text="TOTAL",padx=5,pady=4,bd=4,width=8, command=amount_to_be_paid,font=('arial',16,'bold'))
total.grid(row=0,column=0)

reset=Button(f2b,text="RESET",width=8,command=start_again,padx=5,pady=4,bd=4,font=('arial',16,'bold'))
reset.grid(row=0,column=1)

receipt=Button(f2b,text="RECEIPT",width=8,command=bill_please,padx=5,pady=4,bd=4,font=('arial',16,'bold'))
receipt.grid(row=0,column=2)

exit=Button(f2b,text="EXIT",width=8,command=exit_pls,padx=5,pady=4,bd=4,font=('arial',16,'bold'))
exit.grid(row=0,column=3)



root.mainloop()
