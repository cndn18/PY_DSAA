
a=int(input("enter any1 number"))
b=int(input("enter any2 number"))
c=int(input("enter any3 number"))
d=int(input("enter any4 number"))
e=int(input("enter any5 number"))
f=int(input("enter any6 number"))
g=int((a+b+c+d+e+f)/6)
print(g)
if(g<=100 and g>90):
    print("excellent")
elif(90>g>80):
    print("very good")
elif(80>g>70):
    print("good")
elif(70>g>60):
    print("fair")
elif(40<g<60):
    print("luck next time")
else:
    print("fail")
