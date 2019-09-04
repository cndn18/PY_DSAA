tc=int(input())
app=[]
for i in range(tc):
    k=input()
    app.append(k)
for i in app:
    t=0
    m=len(i)
    for a in i:
        if a in "aeiouAEIOU":
            t=t+1
    print("{}/{}".format(m-t-3,m))        
