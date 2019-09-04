a=int(input())
x=[]
if(a>1 and a<=5):
    for i in range(a):
        y=int(input())
        x.append(y)
for e in x:
    num=e
    count=0
    for i in range(12,0,-1):
        if num>=(2**(i-1)):
            num=num-(2**(i-1))
            count=count+1
            if num==0:
                print(count)
            if num>1024    
