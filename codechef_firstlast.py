a=int(input())
j=[]
for i in range(a):
    k=input()
    j.append(k)
for b in j:
    l=len(b)
    b=int(b)
    m=b%10
    n=b//(10**(l-1))
    print(m+n)
    #print(int(b)%10 + int(b)//(10**(l-1)))
    
    
    
