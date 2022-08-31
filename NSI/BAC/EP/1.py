class Pile:
    """ Classe dÃ©finissant une pile """
    def __init__(self, valeurs=[]):
        self.valeurs = valeurs

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.valeurs == []

    def empiler(self, c):
        """Place lâ€™Ã©lÃ©ment c au sommet de la pile"""
        self.valeurs.append(c)

    def depiler(self):
        """Supprime lâ€™Ã©lÃ©ment placÃ© au sommet de la pile, Ã  condition quâ€™elle soit non vide"""
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage (ch):
    """Renvoie True si la chaÃ®ne ch est bien parenthÃ©sÃ©e et False sinon"""
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert parenthesage("((()())(()))") == True
assert parenthesage("())(()") == False
assert parenthesage("(())(()") == False
