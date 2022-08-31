#EP 1
#EX 1
def moyenne(liste):
    total = 0
    coef = 0
    for i in liste:
        total += i[0]*i[1]
        coef += i[1]
    return total/coef
l = [(15,2),(9,1),(12,3)]
#print(moyenne(l))



#EX 2

#def pascal(n):
#    C= [[1]]
#    for k in range(1,...):
#        Ck = [...]
#        for i in range(1,k):
#            Ck.append(C[...][i-1]+C[...][...] )
#        Ck.append(...)
#        C.append(Ck)
#    return C

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
#print(pascal(5))



#EP 2
#EX 1
def recherche(liste):
    result = []
    for i in range(1,len(liste)):
        if liste[i] == 1+liste[i-1]:
            result.append((liste[i-1],liste[i]))    
    return result
print(recherche([1,4,3,5]))
print(recherche([1,4,5,3]))
print(recherche([7,1,2,5,3,4]))
print(recherche([5,1,2,3,8,-5,-4,7]))


#EX 2
def propager(M, i, j, val):
    if M[i][j] == 0:
        return
    
    M[i][j]=val
    # l'élément en haut fait partie de la composante
    if ((i-1)>=0 and M[i-1][j]==1):
        propager(M, i-1, j, val)
        
    # l'élément en bas fait partie de la composante
    if((i+1)<len(M) and M[i+1][j]==1):
        propager(M, i+1, j, val)
        
    # l'élément àgauche fait partie de la composante
    if((j-1)>=0 and M[i][j-1]==1):
        propager(M, i, j-1, val)
        
    # l'élément àdroite fait partie de la composante
    if((j+1)<len(M)and M[i][j+1]==1):
        propager(M, i, j+1, val)

M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)





