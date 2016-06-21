def rm(liste,i=1):
    return(liste[:i]+liste[i+1:])

def petite(mat,i):
    mat = rm(mat,i)
    
    for k in range(len(mat)):
        
        mat[k] = rm(mat[k],0)
    return(mat)
    
    
def det(mat):
    if(len(mat[1]) == 2):
        return(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])
    deter = 0
    for k in range(len(mat)):
        print(det(petite(mat,k)))
        deter += mat[k][0]*det(petite(mat,k))
    
    
