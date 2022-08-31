
def estPalindrome(chaine):
    
    if len(chaine) == 1 or len(chaine) == 0:
        return True

    
    

    while len(chaine) > 1:

        # Si le 1er caractere est egal au dernier
        if chaine[0] == chaine[-1]:

            # Supression du 1er et dernier caractere
            chaine = chaine[1:-1]

        # Si le 1er caractere est different du dernier
        else:

            # Renvoie Faux
            return False

    # Renvoie True
    return True
