a=int(input())
k=int(input())
lis=list(map(int,input().split()))
count=0

for i in lis:
    if i>a:
        for k in range(2,a):
            if i%k==0 and a%k==0:
                count=count+1
                break
    elif a>i:
        for k in range(2,i):
            if i%k==0 and a%k==0:
                count=count+1
                break
print(count)            
