def rotatelist(l,k):
    s=len(l)
    m=l
    for i in range(k):
        k=m[0]
        for j in range(s):
            if j==(s-1):
                m[j]=k
            else:
                m[j]=m[j+1]
    return m


b=rotatelist([1,2,3,4,5,6,7,8],30)
print(b)
                
        
