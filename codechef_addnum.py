(x,y)=map(int,input().split())
l=0
for i in range(x):
    z=int(input())
    if z%y==0:
        l=l+1
print(l)        
        
