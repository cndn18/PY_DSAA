def sumprimes(l):
    but=0
    for item in l:
        if item>=2:
          c=0
          for i in range(1,item+1):
            if item%i==0:
              c=c+1
          if c==2:
            but=but+item
    return but
    
m=[1,65,7,9,31]
j = sumprimes(m)
print(j)
                    
                    

                
        
        














  

  
