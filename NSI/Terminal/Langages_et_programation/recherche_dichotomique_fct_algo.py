def recherche_dico(mot_chercher,dansUneListe):
    """Recherche dichotomique"""
    
    file = open(dansUneListe,'r')
    liste_mots = []
    for mots in file:
        mots = mots.strip()
        liste_mots.append(mots)
    file.close()
    
    i_debut = 0
    i_fin = len(liste_mots)-1
    i_mil = (i_debut + i_fin)//2 
    nb_comp = 0
    
    while i_debut < i_fin:
        i_mil = (i_debut + i_fin)//2
        nb_comp += 1
        
        if liste_mots[i_mil] == mot_chercher:
            i_debut,i_fin = i_mil,i_mil
                
        elif mot_chercher < liste_mots[i_mil]:
            i_fin = i_mil - 1

        else :
            i_debut = i_mil + 1


        i_mil = (i_debut + i_fin)//2
    if liste_mots[i_mil] == mot_chercher:
        print("position :",i_mil+1," /nombre de comparaison :",nb_comp)
        return True
        
    else:
        print(liste_mots[i_mil] , mot_chercher)
        print('non',mot_chercher)
        return False

def recherche_mot(mot,liste="liste_francais.txt",debut=0,fin=0):
    """Recherche dichotomique recursive"""
    if liste == "liste_francais.txt":        
        with open("liste_francais.txt","r") as f:
            liste = [i.strip() for i in f]
            debut,fin = 0,len(liste)-1
            
    print(debut,fin)
    print((debut+fin)//2)
    if liste[(debut+fin)//2]==mot:
        return True,((debut+fin)//2)+1

    elif debut == fin:
        return False,mot
    
    elif mot < liste[(debut+fin)//2]:
        print(mot,"<",liste[(debut+fin)//2])
        return recherche_mot(mot,liste,debut,((debut+fin)//2)-1)

    else:
        print(mot,">",liste[(debut+fin)//2])
        return recherche_mot(mot,liste,((debut+fin)//2)+1,fin)

        
    
    
#with open("liste_francais.txt","r") as f:
#    l = [i.strip() for i in f]
#for i in l:
#    recherche_mot(i)


    




