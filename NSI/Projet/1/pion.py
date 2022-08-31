class Pion:

    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def deplacer(self, x, y):
        self.x = x
        self.y = y

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

        self.listecoups = listecoups
