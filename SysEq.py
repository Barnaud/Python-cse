l= [[2,2,8],[1,3,1],[3,0,2]]
m= [3,2,1]

def resoudre(l):
    s=[0 for k in range(len(l))]
    for k in range(len(l)):
        reste = 0
        for n in range(len(l[0])):
            reste+=s[n]*l[-k-1][n]
        print(reste)
        s[-k-1]= (1/l[-k-1][-k-1])*(m[-k-1]-reste)
        
    return(s)

def bonPivot(liste):
    for k in range(len(liste)):
        if liste[k][0] == 1:
                liste[k], liste[0] = liste[0], liste[k]
                return (liste)
def produitListe(liste, nb):
    return([liste[k]*nb for k in range(len(liste))])
def difference(l1,l2):
    return([l1[k]-l2[k] for k in range(len(l1))])

def triangle(liste):
    for i in range(1,len(liste)):
        for k in range(i,len(liste)):
            liste[k]=difference(liste[k],produitListe(liste[i-1],liste[k][i-1]/liste[i-1][i-1]))
    return(liste)
            
def fin(liste):
    return(resoudre(triangle(liste)))
