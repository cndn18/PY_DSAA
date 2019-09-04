a=int(input())
k=0
while a>0:
    m=a%10
    k=k*10+m
    a=a//10
print(k)    
