import pygame
pygame.init()

class Pion:

    def __init__(self, x, y, couleur, game):
        # Placement dans la matrice plateau
        self.x = x
        self.y = y
        
        # couleur 'b'/'n'
        self.couleur = couleur
        
        # attribut pour avoir acces au attributs de la partie
        self.game = game
        
        # "Hit_box" de la piece
        self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
        
    def deplacer(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.y, self.x, self.x*self.game.taille_case,self.y*self.game.taille_case)

    def coup_possible(self, plateau):
        x, y = self.x, self.y
        listecoups = []
        if self.couleur == "b":
            if plateau[x - 1][y] == 0:
                listecoups.append((x - 1, y))
                if x == 6:
                    if plateau[4][y] == 0:
                        listecoups.append((4, y))
            try:
                if plateau[x - 1][y - 1] != 0 and plateau[x - 1][y - 1][-1] == "N":
                    listecoups.append((x - 1, y - 1))
            except:
                pass
            try:
                if plateau[x - 1][y + 1] != 0 and plateau[x - 1][y + 1][-1] == "N":
                    listecoups.append((x - 1, y + 1))
            except:
                pass
        else:
            if plateau[x + 1][y] == 0:
                listecoups.append((x + 1, y))

                if x == 1:
                    if plateau[3][y] == 0:
                        listecoups.append((3, y))
            try:
                if plateau[x + 1][y - 1] != 0 and plateau[x + 1][y - 1][-1] == "N":
                    listecoups.append((x + 1, y - 1))
            except:
                pass
            try:
                if plateau[x + 1][y + 1] != 0 and plateau[x + 1][y + 1][-1] == "N":
                    listecoups.append((x + 1, y + 1))
            except:
                pass
        return listecoups
        #self.listecoups = listecoups
