def facto_recu(n):
    f = 1
    if n == 0: return f
    if n != 1:
        f = n*facto_recu(n-1)
    return f
    
