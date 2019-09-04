from math import sqrt
def is_square(n):
    if(sqrt(n) % 1 == 0):
        return True
    else:
        return False
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primesquare(l):
    if len(l)==0:
        return False
    if len(l)==1 and (is_square(l[0]) or is_prime(l[0]) is True):
        return True
    else:
        if is_square(l[0]) is True:
            for i in range(2,len(l),2):
                if(is_square(l[i]) is False):
                    return False
            for i in range(1,len(l),2):
                if(is_prime(l[i]) is False):
                    return False
            return True
        elif is_prime(l[0]) is True:
           for i in range(2,len(l),2):
               if(is_prime(l[i]) is False):
                   return False
           for i in range(1,len(l),2):
               if(is_square(l[i]) is False):
                   return False
           return True
            
                    
                
k=primesquare([5,16,101,36,27])
print(k)
    
