from random import * 
def placement(n):
    places = [0,0]
    while(places[0] == places[1]):
        places = [randint(1,n) for  k in range(2)]
    return(max(places)-min(places)-1)
def moyenne(n,o):
    a = 0
    for k in range(o):
        a+=placement(n)
    return(a/o)
    

    
def comptage(n,o):
    i = 0
    for k in range(o):
        if(placement(n) == 5):
            i+=1
    return(i/o)
