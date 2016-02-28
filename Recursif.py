nombres = [3*k+7 for k in range(100)]

def recherche3(liste,cible, min = 0, max = None):
    if(max == None):
        max = len(liste)-1
    if(liste[min] == cible):
        print(min, liste[min])
        return (0)
    elif(liste[max] == cible):
        print(max, liste[max])
        return(0)
    elif(cible < liste[min] or cible > liste[max] or max-min <=1):
        print("aucune occurence")
        return (0)
    elif(cible>liste[int((min+max)/2)]):
        recherche3(liste, cible, int((min+max)/2), max)
    else:
        recherche3(liste, cible, min, int((min+max)/2))