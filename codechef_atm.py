x,y=input().split()
if((int(x)%5==0) and int(x)<=(float(y)+0.50)):
   print(float(y)-0.50-int(x))
else:
   print("{:.2f}".format(float(y)))
   
         
