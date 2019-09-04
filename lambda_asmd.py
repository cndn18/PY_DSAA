a=lambda x,y:x+y
b=lambda x,y:x-y
c=lambda x,y:x*y
d=lambda x,y:x/y
k=int(input("enter 1 for add,2for sub,3 for mul,4 for div"))
if(k==1):
    abc=a(4,3)
    print(abc)
elif(k==2):
    abc=b(4,3)
    print(abc)
elif(k==3):
    abc=c(4,3)
    print(abc)
elif(k==4):
    abc=d(4,3)
    print(abc)
else:
    print("invalid")
