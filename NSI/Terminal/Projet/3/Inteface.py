import pygame
from Classpieces import *
pygame.init()


# Classe du jeu d'echec
class Game:
    def __init__(self):

        # Initialisation des parametres
        self.taille_case = 96
        self.dossier_image = "images_ombre/"
        self.qui_joue = "Blanc"

        # creation de la fenetre
        self.longueur_fenetre = self.taille_case*8
        self.hauteur_fenetre = self.taille_case*8
        self.fenetre = pygame.display.set_mode((self.longueur_fenetre, self.hauteur_fenetre))



        # Initialisation du plateau
        #self.plateau = [["RN", "NN", "BN", "QN", "KN", "BN", "NN", "RN"],
        #                ["N", "N", "N", "N", "N", "N", "N", "N"],
        #                [0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0],
        #                ["B", "B", "B", "B", "B", "B", "B", "B"],
        #                ["RB", "NB", "BB", "QB", "KB", "BB", "NB", "RB"]]
        
        self.plateau = [["RN", "NN", "BN", "QN", "KN", "BN", "NN", "RN"],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, "N", 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, "B", 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, "B", 0, 0, 0, 0, 0],
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

        # Initialisation piece selectionné
        self.piece = None
        self.piece_coup_possible_rect = []

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

        #self.coup_possible_couleur("Noir")
        #self.posssibiliter_adversaire = []

        # initialisation de quijoue
        self.quijoue = 'b'

    def creation_class_piece(self):
        # Initialisation liste contenant toutes les instances des pieces
        self.all_pieces = []

        # Pour chaque case 
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):

                # Si la case contient un pion noir
                if self.plateau[i][j] == "N":
                    # Ajout a la liste de toutes les pieces le pion
                    self.all_pieces.append(Pion(i,j,'n', self))
                    
                if self.plateau[i][j] == "B":
                    self.all_pieces.append(Pion(i,j,'b', self))

                if self.plateau[i][j] == "RB":
                    self.all_pieces.append(Tour(i,j,'b', self))
                    
                if self.plateau[i][j] == "RN":
                    self.all_pieces.append(Tour(i,j,'n', self))

                if self.plateau[i][j] == "NB":
                    self.all_pieces.append(Cavalier(i,j,'b', self))
                    
                if self.plateau[i][j] == "NN":
                    self.all_pieces.append(Cavalier(i,j,'n', self))

                if self.plateau[i][j] == "BB":
                    self.all_pieces.append(Fou(i,j,'b', self))
                    
                if self.plateau[i][j] == "BN":
                    self.all_pieces.append(Fou(i,j,'n', self))

                if self.plateau[i][j] == "QB":
                    self.all_pieces.append(Dame(i,j,'b', self))
                    
                if self.plateau[i][j] == "QN":
                    self.all_pieces.append(Dame(i,j,'n', self))

                if self.plateau[i][j] == "KB":
                    self.all_pieces.append(Roi(i,j,'b', self))
                    
                if self.plateau[i][j] == "KN":
                    self.all_pieces.append(Roi(i,j,'n', self))

                
                    
    def coup_possible_couleur(self,couleur):
        """ Renvoie une liste de tout les coups possible de toutes les pieces d'une couleur sauf le roi """

        # Quand la piece selectionner est blanche
        if couleur == 'b':
            
            # Liste contenent toute les possibiliter [(x,y),(x,y),(x,y),...]
            self.posssibiliter_adversaire = []

            # Pour chaque pieces 
            for i in self.all_pieces:
                # Si la piece n'est pas le roi
                if type(i) != Roi:
                    # Si la couleur de la piece est celle de l'adversaire
                    if i.couleur == 'n':
                        
                        coup = i.coup_possible(self.plateau)                       
                        # Ajout des coup possible a posssibiliter_adversaire
                        self.posssibiliter_adversaire += coup[0]
                        # Ajout des cases que la piece protege a posssibiliter_adversaire
                        self.posssibiliter_adversaire += coup[2]
            
            # Renvoie posssibiliter_adversaire            
            return self.posssibiliter_adversaire

        # Quand la piece selectionner est noire
        elif couleur == 'n':
            
            # Liste contenent toute les possibiliter [(x,y),(x,y),(x,y),...]
            self.posssibiliter_adversaire = []

            # Pour chaque pieces
            for i in self.all_pieces:
                # Si la piece n'est pas le roi
                if type(i) != Roi:
                    # Si la couleur de la piece est celle de l'adversaire
                    if i.couleur == 'b':

                        coup = i.coup_possible(self.plateau)                       
                        # Ajout des coup possible a posssibiliter_adversaire
                        self.posssibiliter_adversaire += coup[0]
                        # Ajout des cases que la piece protege a posssibiliter_adversaire
                        self.posssibiliter_adversaire += coup[2]
                        
            # Renvoie posssibiliter_adversaire           
            return self.posssibiliter_adversaire
                        
                    
                    

    def actualiser(self):
        
        # Position de la souris
        mx, my = pygame.mouse.get_pos()
        
        # Gestion des evenements
        for event in pygame.event.get():
            # Gestion de la fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()

            
            
            # Pour chaque piece 
            for p in self.all_pieces:

                # Si la piece est de la couleur du joueur
                if p.couleur == self.quijoue:
                
                    # Si la souris touche la case et clique
                    if p.rect.collidepoint(mx, my) and pygame.mouse.get_pressed()[0]:
                        # piece est selectionner
                        self.piece = p
                    
                        # piece_coup_possible_rect -> [(rect,(x,y)),(rect,(x,y)),(rect,(x,y)),...]
                        self.piece_coup_possible_rect = []
                        # Si la piece n'est pas le roi
                        if type(p) != Roi:
                            coup = p.coup_possible(self.plateau)
                            #print(p)
                            #print(coup)
                            # Ajout pour l'affichage des cases possible pour la piece selectioné
                            for i in range(len(coup[0])):
                        
                                self.piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*self.taille_case,coup[0][i][0]*self.taille_case,self.taille_case,self.taille_case),(coup[0][i][0],coup[0][i][1])))
                        # Sinon pour le roi
                        else:
                            coup_adversaire = self.coup_possible_couleur(p.couleur)
                            coup = p.coup_possible(self.plateau,coup_adversaire)
                        
                            for i in range(len(coup[0])):
                        
                                self.piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*self.taille_case,coup[0][i][0]*self.taille_case,self.taille_case,self.taille_case),(coup[0][i][0],coup[0][i][1])))
            
                # Pour chaque case possible ou peut aller la piece selectionné
                for i in range(len(self.piece_coup_possible_rect)):
                    # Si la case est cliquer
                    if self.piece_coup_possible_rect[i][0].collidepoint(mx, my) and pygame.mouse.get_pressed()[0]:
                        #print(self.piece.x,self.piece.y)
                        # x_depart ,y_depart
                        x_d, y_d = self.piece.x, self.piece.y
                    
                        #print(self.piece_coup_possible_rect[i][1])
                        # x_fin, y_fin
                        x_f, y_f = self.piece_coup_possible_rect[i][1][0],self.piece_coup_possible_rect[i][1][1]

                        # Verifier si la case n'est pas vide
                        if self.plateau[x_f][y_f]:
                        
                            # Parcours all_piece pour chercher la piece qui a pour coordonner la case x_f,y_f pour la supprimer de la liste
                            # pour chaque pieces dans la liste de toutes les pieces du plateau
                            for piece in range(len(self.all_pieces)):
                                # Si la piece a pour coordonnées la case finale
                                if self.all_pieces[piece].x == x_f and self.all_pieces[piece].y == y_f:
                                    # Suppression de la piece
                                    del self.all_pieces[piece]
                                    break


                        # deplace la piece
                        self.piece.deplacer(x_f,y_f)
                    
                    

                        # Deselection de la piece (et des rect)
                        self.piece = None
                        self.piece_coup_possible_rect = []

                        # Changement du joueur
                        if self.quijoue == 'b':
                            self.quijoue = 'n'
                        else:
                            self.quijoue = 'b'
                        break
            


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
                    
        # affichage des hitbox
        for p in self.all_pieces:
            pygame.draw.rect(self.fenetre, (0, 0, 255), p.rect, 2)

        for i in self.piece_coup_possible_rect:
            pygame.draw.rect(self.fenetre, (255, 255, 0), i[0], 4)

        #for i in self.posssibiliter_adversaire:
        #    pygame.draw.rect(self.fenetre,(0,0,255), pygame.Rect(i[1]*self.taille_case, i[0]*self.taille_case, self.taille_case,self.taille_case),2)
            

        
        
        # Actualisation
        pygame.display.flip()



# Début du programme

game = Game()
while True:
    game.actualiser()
    game.affichage()
