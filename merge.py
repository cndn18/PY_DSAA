def merge(a,b):
    c=[]
    m=len(a)
    n=len(b)
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j=j+1
        elif j==n:
            c.append(a[i])
            i=i+1
        elif a[i]<b[j]:
            c.append(a[i])
            i=i+1            
        elif b[j]<a[i]:
            c.append(b[j])
            j=j+1
    return c


a=[1,3,5,7,9]
b=[2,4,6,8,10]
d=merge(a,b)
print(d)
