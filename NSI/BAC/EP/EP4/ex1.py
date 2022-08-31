def moyenne(tab):
    if not tab:
        return 'erreur'

    total = 0
    for i in tab:
        total += i
    return total/len(tab)
