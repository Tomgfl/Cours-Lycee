import pygame
from pion import *
pygame.init()


# Classe du jeu d'echec
class Game:
    def __init__(self):

        # Initialisation des parametres
        self.taille_case = 96
        self.dossier_image = "images_ombre/"

        # creation de la fenetre
        self.longueur_fenetre = self.taille_case*8
        self.hauteur_fenetre = self.taille_case*8
        self.fenetre = pygame.display.set_mode((self.longueur_fenetre, self.hauteur_fenetre))



        # Initialisation du plateau
        self.plateau = [["RN", "NN", "BN", "QN", "KN", "BN", "NN", "RN"],
                        ["N", "N", "N", "N", "N", "N", "N", "N"],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        ["B", "B", "B", "B", "B", "B", "B", "B"],
                        ["RB", "NB", "BB", "QB", "KB", "BB", "NB", "RB"]]
        # R_ -> Tour
        # N_ -> Cavalier
        # B_ -> Fou
        # Q_ -> Dame
        # K_ -> Roi
        # _N -> Piece noire
        # _B -> Piece blanche
        # N -> Pion noir
        # B -> Pion blanc

        # Initialisation des images
        self.image_fond = pygame.image.load(self.dossier_image+'plateau.png').convert_alpha()
        self.image_fond = pygame.transform.scale(self.image_fond, (self.taille_case*8, self.taille_case*8))

        # Pieces blanches
        # Chargement de l'image
        self.image_pion_B = pygame.image.load(self.dossier_image+'Pion_blanc.png').convert_alpha()
        # Changement de la taille de l'image
        self.image_pion_B = pygame.transform.scale(self.image_pion_B, (self.taille_case, self.taille_case))

        self.image_cavalier_B = pygame.image.load(self.dossier_image+'Cavalier_blanc.png').convert_alpha()
        self.image_cavalier_B = pygame.transform.scale(self.image_cavalier_B, (self.taille_case, self.taille_case))

        self.image_fou_B = pygame.image.load(self.dossier_image+'Fou_blanc.png').convert_alpha()
        self.image_fou_B = pygame.transform.scale(self.image_fou_B, (self.taille_case, self.taille_case))

        self.image_tour_B = pygame.image.load(self.dossier_image+'Tour_blanc.png').convert_alpha()
        self.image_tour_B = pygame.transform.scale(self.image_tour_B, (self.taille_case, self.taille_case))

        self.image_dame_B = pygame.image.load(self.dossier_image+'Dame_blanc.png').convert_alpha()
        self.image_dame_B = pygame.transform.scale(self.image_dame_B, (self.taille_case, self.taille_case))

        self.image_roi_B = pygame.image.load(self.dossier_image+'Roi_blanc.png').convert_alpha()
        self.image_roi_B = pygame.transform.scale(self.image_roi_B, (self.taille_case, self.taille_case))

        # Pieces noires
        self.image_pion_N = pygame.image.load(self.dossier_image+'Pion_noir.png').convert_alpha()
        self.image_pion_N = pygame.transform.scale(self.image_pion_N, (self.taille_case, self.taille_case))

        self.image_cavalier_N = pygame.image.load(self.dossier_image+'Cavalier_noir.png').convert_alpha()
        self.image_cavalier_N = pygame.transform.scale(self.image_cavalier_N, (self.taille_case, self.taille_case))

        self.image_fou_N = pygame.image.load(self.dossier_image+'Fou_noir.png').convert_alpha()
        self.image_fou_N = pygame.transform.scale(self.image_fou_N, (self.taille_case, self.taille_case))

        self.image_tour_N = pygame.image.load(self.dossier_image+'Tour_noir.png').convert_alpha()
        self.image_tour_N = pygame.transform.scale(self.image_tour_N, (self.taille_case, self.taille_case))

        self.image_dame_N = pygame.image.load(self.dossier_image+'Dame_noir.png').convert_alpha()
        self.image_dame_N = pygame.transform.scale(self.image_dame_N, (self.taille_case, self.taille_case))

        self.image_roi_N = pygame.image.load(self.dossier_image+'Roi_noir.png').convert_alpha()
        self.image_roi_N = pygame.transform.scale(self.image_roi_N, (self.taille_case, self.taille_case))

        self.creation_class_piece()

    def creation_class_piece(self):
        # Initialisation liste contenant toutes les instances des pieces
        self.all_pieces = []
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                if self.plateau[i][j] == "N":
                    self.all_pieces.append(Pion(i,j,'n'))
                    



    def actualiser(self):
        # Gestion des evenements
        for event in pygame.event.get():
            # Gestion de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()


    def affichage(self):
        # Affichage echiquier
        self.fenetre.blit(self.image_fond, (0, 0))

        # Affichage chaque piece
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                # Si la case contient "N" (pion noir)
                if self.plateau[i][j] == "N":
                    # Affichage du pion noir
                    self.fenetre.blit(self.image_pion_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "RN":
                    self.fenetre.blit(self.image_tour_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "NN":
                    self.fenetre.blit(self.image_cavalier_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "BN":
                    self.fenetre.blit(self.image_fou_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "KN":
                    self.fenetre.blit(self.image_roi_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "QN":
                    self.fenetre.blit(self.image_dame_N, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "B":
                    self.fenetre.blit(self.image_pion_B, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "RB":
                    self.fenetre.blit(self.image_tour_B, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "NB":
                    self.fenetre.blit(self.image_cavalier_B, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "BB":
                    self.fenetre.blit(self.image_fou_B, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "KB":
                    self.fenetre.blit(self.image_roi_B, (j*self.taille_case, i*self.taille_case))

                elif self.plateau[i][j] == "QB":
                    self.fenetre.blit(self.image_dame_B, (j*self.taille_case, i*self.taille_case))

        # Actualisation
        pygame.display.flip()



# Début du programme

game = Game()
while True:
    game.actualiser()
    game.affichage()
