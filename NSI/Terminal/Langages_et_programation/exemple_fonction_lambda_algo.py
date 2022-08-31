#Declaration de la fonction image qui prend comme argument une fonction
def image(fct):
    #pour i allant de 10 a 20
    for i in range(10,21):
        #on affiche le message "a x on associe fonction(x)
        print("a ",i," on associe ",fct(i))
