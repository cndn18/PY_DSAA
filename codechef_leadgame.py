a=int(input())
dic={}
maxi=0
for i in range(a):
    (x,y)=map(int,input().split())
    if(x>y and x-y>maxi):
        maxi=x-y
        dic[1]=maxi
    if(y>x and y-x>maxi):
        maxi=y-x
        dic[2]=maxi
m=max(dic,key=dic.get)
print(m," ",dic[m])
    
