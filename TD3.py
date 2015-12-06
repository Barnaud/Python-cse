def h(chaine):
    sortie = ''
    compteur = 1
    while compteur <= len(chaine):
        sortie+= chaine[compteur*-1]
        compteur +=1
    sortie.replace(' ', '')
    chaine.replace(' ', '')
    if chaine == sortie :
        print ('palyndrome!') 
        
    
