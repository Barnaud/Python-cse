def choix(choixA, choixB, fonctionA, fonctionB, msg):
    print (msg)
    inp = input()
    if inp == str(choixA):
        fonctionA()
    elif inp == str(choixB):
        fonctionB()
    else:
        print("erreur")
        choix(choixA, choixB, fonctionA, fonctionB, msg)
def non():
    print("à la prochaine")
    return(0) 
def Nbjoueur():
    choix(1,2,un,deux, "combien de joueurs êtes vous?")

def jeu():
    choix("y","n",Nbjoueur, non, "Voulez vous jouer?")

def un():
    print("vous avez choisi un joueur")
def deux():
    print("vous avez choisi deux joueurs")
