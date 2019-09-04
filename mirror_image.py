def matrixflip(l,d):
    if d is not'v' and d is not 'h':
        print(l)
    else:
        if d=='v':
            print(l[::-1])
        if d=='h':
            m=[]
            for i in l:
                m.append(i[::-1])
            print(m)
          
                
            
            


matrixflip([[1, 2], [3, 4]],'v')
matrixflip([[1, 2], [3, 4]],'h')

