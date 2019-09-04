n=int(input())
num=[]
num=list(map(int,input().strip()))
bite=[]
bito=[]

def bitscore(y):
    highest=0
    smallest=9
    while y>0:
        rem=y%10
        if rem>highest:
            highest=rem
        if rem<smallest:
            smallest=rem
        y=y//10

    z=highest*11+smallest*7
    if len(str(z)) is 3:
        z=z%100

    return z       
            
            
for i in range(n):
    if i%2 is 0:
        k=bitscore(num[i])
        bite.append(k)
    else:
        j=bitscore(num[i])
        bito.append(j)

        
def count(array):
    s=0
    m=0
    for i in array:
        k=i//10
        m=m+1
        for j in array[m:]:
            if j//10 is k:
                s=s+1
                break

    return s        
                
print(count(bito)+count(bite))            
























    
        
        
        
    
    
    
