from tkinter import*
from tkinter.filedialog import askopenfilename
def newfile():
    print("new file!")
def openfile():
    name=askopenfilename()
    print(name)
def about():
    print("this is a simple example of a menu")

root=Tk()
menu=Menu(root)
root.config(menu=menu,bg="red"  )
filemenu=Menu(menu)
menu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="new",command=newfile)
filemenu.add_command(label="open",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_cascade(label="about",command=about)
mainloop()
    
    
