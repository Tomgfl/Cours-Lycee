from sys import path
path.append("c:\\users\\titouan\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\\localcache\\local-packages\\python310\\site-packages")
import pygame
from copy import deepcopy
from Classpieces import *
import Calculs

pygame.init()


# Classe du jeu d'echec
class Game:
	def __init__(self):

		# Initialisation des parametres
		self.taille_case = 96
		self.dossier_image = "images_ombre/"
		self.qui_joue = "b"
		# Petits roque et grand roque
		self.prb = True
		self.prn = True
		self.grb = True
		self.grn = True
		# en passant pour les pions(pour les manger)
		self.enpassant = False
		# pion promu en fin de plateau
		self.promotion = False

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

		self.roi_noir_echec = False
		self.roi_blanc_echec = False

		

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


	def actualiser(self):
		
		# Position de la souris
		mx, my = pygame.mouse.get_pos()
		
		# Gestion des evenements
		for event in pygame.event.get():
			# Gestion de la fermeture de la fenetre
			if event.type == pygame.QUIT:
				pygame.quit()

			
			if self.promotion :
				for p in range(len(self.all_pieces)) :
					if type(self.all_pieces[p]) == enpromotion :
						for r in self.all_pieces[p].rect :
							if r.collidepoint(mx, my) and pygame.mouse.get_pressed()[0]:
								#Si on clique sur la dame
								if r == pygame.Rect(self.all_pieces[p].y*self.taille_case, self.all_pieces[p].x*self.taille_case, 47,47) :
									#Promotion en dame
									self.all_pieces.append(Dame(self.all_pieces[p].x,self.all_pieces[p].y,self.all_pieces[p].couleur,self))
									self.plateau[self.all_pieces[p].x][self.all_pieces[p].y] = "Q"+self.all_pieces[p].couleur.capitalize()
									del self.all_pieces[p]
									self.promotion = False

								elif r == pygame.Rect(self.all_pieces[p].y*self.taille_case+47, self.all_pieces[p].x*self.taille_case, 47,47) :
									self.all_pieces.append(Tour(self.all_pieces[p].x,self.all_pieces[p].y,self.all_pieces[p].couleur,self))
									self.plateau[self.all_pieces[p].x][self.all_pieces[p].y] = "R"+self.all_pieces[p].couleur.capitalize()
									del self.all_pieces[p]
									self.promotion = False

								elif r == pygame.Rect(self.all_pieces[p].y*self.taille_case, self.all_pieces[p].x*self.taille_case+47, 47,47) :
									self.all_pieces.append(Fou(self.all_pieces[p].x,self.all_pieces[p].y,self.all_pieces[p].couleur,self))
									self.plateau[self.all_pieces[p].x][self.all_pieces[p].y] = "B"+self.all_pieces[p].couleur.capitalize()
									del self.all_pieces[p]
									self.promotion = False

								elif r == pygame.Rect(self.all_pieces[p].y*self.taille_case+47, self.all_pieces[p].x*self.taille_case+47, 47,47) :
									self.all_pieces.append(Cavalier(self.all_pieces[p].x,self.all_pieces[p].y,self.all_pieces[p].couleur,self))
									self.plateau[self.all_pieces[p].x][self.all_pieces[p].y] = "N"+self.all_piecse[p].couleur.capitalize()
									del self.all_pieces[p]
									self.promotion = False
									

			else :
				# Pour chaque piece 
				for p in self.all_pieces:

					# Si la piece est de la couleur du joueur
					if p.couleur == self.quijoue:

					
				
						# Si la souris touche la case et clique
						if p.rect.collidepoint(mx, my) and pygame.mouse.get_pressed()[0]:
                                                        
							# piece est selectionner
							self.piece = p

						
							

							#self.posssibiliter_adversaire = self.coup_possible_couleur('b')
					
							# piece_coup_possible_rect -> [(rect,(x,y)),(rect,(x,y)),(rect,(x,y)),...]
							self.piece_coup_possible_rect = []
							# Si la piece n'est pas le roi
							if type(p) != Roi:
								coup = p.coup_possible(self.plateau)
							
								# test si ya echec sur le roi
								if Calculs.roi_echec(self,p.couleur,self.plateau):
									coup_definitif = []
									liste_rajout = []
									position_base = p.x,p.y
									self.plateau_test = deepcopy(self.plateau)
									# pour chaque coup possible
									for coup_test in coup[0]:
										#print(coup_test)
										# deplace la piece dans un plateau fictif
										if self.plateau[coup_test[0]][coup_test[1]]:
						
											# Parcours all_piece pour chercher la piece qui a pour coordonner la case coup_test[0],coup_test[1] pour la supprimer de la liste temporairement et la rajouter ensuite
											# pour chaque pieces dans la liste de toutes les pieces du plateau
											for piece in range(len(self.all_pieces)):
												# Si la piece a pour coordonnées la case de test
												if self.all_pieces[piece].x == coup_test[0] and self.all_pieces[piece].y == coup_test[1]:
													# Suppression de la piece et rajout dans la liste_rajout
													liste_rajout.append(self.all_pieces.pop(piece))
													break
										p.deplacer(coup_test[0],coup_test[1],self.plateau_test,True)
										#print(self.plateau_test)
										# si le roi n'est pas en echec dans cette position
										if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
											# ajout de la position dans les coup possibles
											coup_definitif.append(coup_test)

										#rajout des pieces dans all_pieces et suppression de celle de listerajout
										for i in range(len(liste_rajout)):
											self.all_pieces.append(liste_rajout[0])
											liste_rajout.pop(0)

										p.deplacer(position_base[0],position_base[1],self.plateau_test,True)
										#print(self.plateau_test)
										#self.plateau_test = deepcopy(self.plateau)
										
									# repositionne la piece a sa place initiale
									#p.deplacer(position_base[0],position_base[1],self.plateau)
									p.rect = pygame.Rect(position_base[1]*self.taille_case, position_base[0]*self.taille_case, self.taille_case,self.taille_case)
									for i in liste_rajout:
										self.all_pieces.append(i)
									#print(coup)
								
									#print(coup_definitif)

									# changement des coup par seulement les coups legaux
									coup = (coup_definitif,coup[1],coup[2])
								
									#print(coup)
							
								# Ajout pour l'affichage des cases possible pour la piece selectioné
								for i in range(len(coup[0])):
									#(rect(x,y,taille_x,taille_y),(x,y))
									self.piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*self.taille_case,coup[0][i][0]*self.taille_case,self.taille_case,self.taille_case),(coup[0][i][0],coup[0][i][1])))
								
							# Sinon pour le roi
							else:
								# verification 
								coup_adversaire = Calculs.coup_possible_couleur(self,p.couleur,self.plateau)
								coup = p.coup_possible(self.plateau,coup_adversaire)

								# test si ya echec sur le roi
								if Calculs.roi_echec(self,p.couleur,self.plateau):
									coup_definitif = []
									liste_rajout = []
									position_base = p.x,p.y
									self.plateau_test = deepcopy(self.plateau)
									# pour chaque coup possible
									for coup_test in coup[0]:
										#print(coup_test)
										# deplace la piece dans un plateau fictif
										if self.plateau[coup_test[0]][coup_test[1]]:
						
											# Parcours all_piece pour chercher la piece qui a pour coordonner la case coup_test[0],coup_test[1] pour la supprimer de la liste temporairement et la rajouter ensuite
											# pour chaque pieces dans la liste de toutes les pieces du plateau
											for piece in range(len(self.all_pieces)):
												# Si la piece a pour coordonnées la case de test
												if self.all_pieces[piece].x == coup_test[0] and self.all_pieces[piece].y == coup_test[1]:
													# Suppression de la piece et rajout dans la liste_rajout
													liste_rajout.append(self.all_pieces.pop(piece))
													break
										p.deplacer(coup_test[0],coup_test[1],self.plateau_test,True)
										#print(self.plateau_test)
										# si le roi n'est pas en echec dans cette position
										if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
											# ajout de la position dans les coup possibles
											coup_definitif.append(coup_test)

										#rajout des pieces dans all_pieces et suppression de celle de listerajout
										for i in range(len(liste_rajout)):
											self.all_pieces.append(liste_rajout[0])
											liste_rajout.pop(0)

										p.deplacer(position_base[0],position_base[1],self.plateau_test,True)
										#print(self.plateau_test)
										#self.plateau_test = deepcopy(self.plateau)
										
									# repositionne la piece a sa place initiale
									#p.deplacer(position_base[0],position_base[1],self.plateau)
									p.rect = pygame.Rect(position_base[1]*self.taille_case, position_base[0]*self.taille_case, self.taille_case,self.taille_case)
									for i in liste_rajout:
										self.all_pieces.append(i)
									#print(coup)
								
									#print(coup_definitif)

									# changement des coup par seulement les coups legaux
									coup = (coup_definitif,coup[1],coup[2])
								
									#print(coup)
							
								# test les roques ( il ne faut pas être en echec et il faut selectionner le roi)
								elif type(p) == Roi :
									if p.couleur == "b" :
										if self.prb :
											self.plateau_test = deepcopy(self.plateau)
											if not self.plateau[7][5] and not self.plateau[7][6] and self.plateau[7][7] == "RB":
												p.deplacer(7,5,self.plateau_test,True)
												if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
													p.deplacer(7,6,self.plateau_test,True)
													if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
														coup=(coup[0]+[(7,6)],coup[1],coup[2])

											if self.grb :
												self.plateau_test = deepcopy(self.plateau)
												if not self.plateau[7][3] and not self.plateau[7][2] and not self.plateau[7][1] and self.plateau[7][0] == "RB":
													p.deplacer(7,3,self.plateau_test,True)
													if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
														p.deplacer(7,2,self.plateau_test,True)
														if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
															coup=(coup[0]+[(7,2)],coup[1],coup[2])


									else :
										if self.prn :
											self.plateau_test = deepcopy(self.plateau)
											if not self.plateau[0][5] and not self.plateau[0][6] and self.plateau[0][7] == "RN":
												p.deplacer(0,5,self.plateau_test,True)
												if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
													p.deplacer(0,6,self.plateau_test,True)
													if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
														coup=(coup[0]+[(0,6)],coup[1],coup[2])

											if self.grn :
												self.plateau_test = deepcopy(self.plateau)
												if not self.plateau[0][3] and not self.plateau[0][2] and not self.plateau[0][1] and self.plateau[0][0] == "RN":
													p.deplacer(0,3,self.plateau_test,True)
													if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
														p.deplacer(0,2,self.plateau_test,True)
														if not Calculs.roi_echec(self,p.couleur,self.plateau_test):
															coup=(coup[0]+[(0,2)],coup[1],coup[2])





								for i in range(len(coup[0])):
						
									self.piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*self.taille_case,coup[0][i][0]*self.taille_case,self.taille_case,self.taille_case),(coup[0][i][0],coup[0][i][1])))
			
					# Pour chaque case possible ou peut aller la piece selectionné
					for i in range(len(self.piece_coup_possible_rect)):
						# Si la case est cliquer
						if self.piece_coup_possible_rect[i][0].collidepoint(mx, my) and pygame.mouse.get_pressed()[0]:
							roque = False
							#si on fait un petit roque blanc
							if self.prb and self.piece_coup_possible_rect[i][1] == (7,6) and type(p) == Roi:
								roque = True
								self.piece.deplacer(7,6,self.plateau)
								#balayage des piece pour trouver la tour
								for piececherche in self.all_pieces :
									if type(piececherche) == Tour and piececherche.couleur == "b" and piececherche.x == 7 and piececherche.y == 7:
										piececherche.deplacer(7,5,self.plateau)

							#si on fait un grand roque blanc
							if self.grb and self.piece_coup_possible_rect[i][1] == (7,2) and type(p) == Roi:
								roque = True
								self.piece.deplacer(7,2,self.plateau)
								#balayage des piece pour trouver la tour
								for piececherche in self.all_pieces :
									if type(piececherche) == Tour and piececherche.couleur == "b" and piececherche.x == 7 and piececherche.y == 0:
										piececherche.deplacer(7,3,self.plateau)

							#si on fait un petit roque noir
							if self.prn and self.piece_coup_possible_rect[i][1] == (0,6) and type(p) == Roi :
								roque = True
								self.piece.deplacer(0,6,self.plateau)
								#balayage des piece pour trouver la tour
								for piececherche in self.all_pieces :
									if type(piececherche) == Tour and piececherche.couleur == "n" and piececherche.x == 0 and piececherche.y == 7:
										piececherche.deplacer(0,5,self.plateau)

							#si on fait un grand roque noir
							if self.grn and self.piece_coup_possible_rect[i][1] == (0,2) and type(p) == Roi:
								roque = True
								self.piece.deplacer(0,2,self.plateau)
								#balayage des piece pour trouver la tour
								for piececherche in self.all_pieces :
									if type(piececherche) == Tour and piececherche.couleur == "n" and piececherche.x == 0 and piececherche.y == 0:
										piececherche.deplacer(0,3,self.plateau)

							#si on ne joue pas un roque
							if not roque:
								#print(self.piece.x,self.piece.y)
								#x_depart ,y_depart
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
								self.piece.deplacer(x_f,y_f,self.plateau)
					
					
							# Deselection de la piece (et des rect)
							self.piece = None
							self.piece_coup_possible_rect = []

							#if not self.promotion :
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
				elif self.plateau[i][j] == "EN" :
					self.fenetre.blit(pygame.transform.scale(self.image_dame_N,(47,47)), (j*self.taille_case, i*self.taille_case))
					self.fenetre.blit(pygame.transform.scale(self.image_tour_N,(47,47)), (j*self.taille_case+47, i*self.taille_case))
					self.fenetre.blit(pygame.transform.scale(self.image_fou_N,(47,47)), (j*self.taille_case, i*self.taille_case+47))
					self.fenetre.blit(pygame.transform.scale(self.image_cavalier_N,(47,47)), (j*self.taille_case+47, i*self.taille_case+47))

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
					# Affichage du pion blanc
					self.fenetre.blit(self.image_pion_B, (j*self.taille_case, i*self.taille_case))
				elif self.plateau[i][j] == "EB" :
					self.fenetre.blit(pygame.transform.scale(self.image_dame_B,(47,47)), (j*self.taille_case, i*self.taille_case))
					self.fenetre.blit(pygame.transform.scale(self.image_tour_B,(47,47)), (j*self.taille_case+47, i*self.taille_case))
					self.fenetre.blit(pygame.transform.scale(self.image_fou_B,(47,47)), (j*self.taille_case, i*self.taille_case+47))
					self.fenetre.blit(pygame.transform.scale(self.image_cavalier_B,(47,47)), (j*self.taille_case+47, i*self.taille_case+47))

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
			if p.couleur == self.quijoue and not self.promotion:
				try :
					pygame.draw.rect(self.fenetre, (0, 0, 255), p.rect, 2)
				except :
					pass

			else :
				if type(p) == enpromotion :
					for r in p.rect :
						pygame.draw.rect(self.fenetre, (0, 0, 255), r, 2)

		for i in self.piece_coup_possible_rect:
			pygame.draw.rect(self.fenetre, (255, 255, 0), i[0], 4)

		
		#for i in self.posssibiliter_adversaire:
		#    pygame.draw.rect(self.fenetre,(0,128,255), pygame.Rect(i[1]*self.taille_case, i[0]*self.taille_case, self.taille_case,self.taille_case),2)
			

		
		
		# Actualisation
		pygame.display.flip()



# Début du programme

game = Game()
while True:
	game.actualiser()
	game.affichage()
