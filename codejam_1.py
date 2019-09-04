import random as rd

x=int(input())
y=[]

#enter the number to be printed on the check
for i in range(0,x):
    y.append(input())
for i in range(x):
    while '4' in y[i]:
        z=rd.randint(1,int(y[i]))
        a=int(y[i])-z
        if '4' not in str(z) and '4' not in str(a):
            print(r"case #"+str(i+1)+":"+" "+str(z)+" "+str(a))
            break
