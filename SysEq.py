l= [[1,2,8],[0,3,1],[0,0,2]]
m= [3,2,1]

def resoudre(l,m):
    s=[0 for k in range(len(l))]
    for k in range(len(l)):
        reste = 0
        for n in range(len(l[0])):
            reste+=s[n]*l[-k-1][n]
        print(reste)
        s[-k-1]= (1/l[-k-1][-k-1])*(m[-k-1]-reste)
        
    return(s)
