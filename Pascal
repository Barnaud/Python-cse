def pascal(n):
    T=[[1],[1,1],[1,2,1]]
    for i in range (2,n):
        T.append([1])
        for t in range (i):
            T[i+1].append(T[i][t]+T[i][t+1]) 
        T[i+1].append(1)
    
    
    
    print (T)
