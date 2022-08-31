

def estPalindromeRecu(chaine):
    if len(chaine) < 1:
        return True
        
    if chaine[0] == chaine[-1]:
        return estPalindromeRecu(chaine[1:-1])

    else:
        return False
