liste = [1000,800,802,1000,1003]

def delta(liste):
    resultat = []
    resultat.append(liste[0])
    
    for i in range(1,len(liste)):
        resultat.append(liste[i] - liste[i-1])

    return resultat

        
