def pascal(n):
    C = [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C


#def pascal(n):
#    C = [[1]]
#    for k in range(1,n):
#        Ck = [...]
#        for i in range(1,k):
#            Ck.append(C[...][i-1]+C[...][...])
#        Ck.append(...)
#        C.append(Ck)
#    return C
