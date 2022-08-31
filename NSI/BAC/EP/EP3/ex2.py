M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]

def propager(M,i,j,val):
    if M[i][j] == 0:
        return

    M[i][j] = val

    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M,i-1,j,val)

    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M,i+1,j,val)

    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M,i,j-1,val)

    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M,i,j+1,val)
