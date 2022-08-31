
class Palindrome:
    def __init__(self,chaine):
        self.chaine = chaine
        self.modifi_chaine()

    def modifi_chaine(self):
        cara_invalide = ' ,;:!?./()-_'
        chaine_list = [cara for cara in self.chaine if cara not in cara_invalide]
        self.chaine = ''.join(chaine_list)
        
    
    def estPalindrome(self):      
        chaine = self.chaine
        if len(chaine) == 1 or len(chaine) == 0:
            return True

        while len(chaine) > 1:
            if chaine[0] == chaine[-1]:
                chaine = chaine[1:-1]

            else:
                return False
        return True
