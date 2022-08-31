import pygame
pygame.init()
from Classpieces import *
from copy import deepcopy


def coup_possible_reel(game, p, pl):
	#game.posssibiliter_adversaire = game.coup_possible_couleur('b')
	# piece_coup_possible_rect -> [(rect,(x,y)),(rect,(x,y)),(rect,(x,y)),...]
	piece_coup_possible_rect = []
	# Si la piece n'est pas le roi
	if type(p) != Roi:
		coup = p.coup_possible(pl)

		# test si ya echec sur le roi
		if roi_echec(game,p.couleur,pl):
			coup_definitif = []
			liste_rajout = []
			position_base = p.x,p.y
			plateau_test = deepcopy(pl)
			# pour chaque coup possible
			for coup_test in coup[0]:
				#print(coup_test)
				# deplace la piece dans un plateau fictif
				if pl[coup_test[0]][coup_test[1]]:
						
					# Parcours all_piece pour chercher la piece qui a pour coordonner la case coup_test[0],coup_test[1] pour la supprimer de la liste temporairement et la rajouter ensuite
					# pour chaque pieces dans la liste de toutes les pieces du plateau
					for piece in range(len(game.all_pieces)):
						# Si la piece a pour coordonnées la case de test
						if game.all_pieces[piece].x == coup_test[0] and game.all_pieces[piece].y == coup_test[1]:
							# Suppression de la piece et rajout dans la liste_rajout
							liste_rajout.append(game.all_pieces.pop(piece))
							break
				p.deplacer(coup_test[0],coup_test[1],plateau_test,True)
				#print(plateau_test)
				# si le roi n'est pas en echec dans cette position
				if not roi_echec(game,p.couleur,plateau_test):
					# ajout de la position dans les coup possibles
					coup_definitif.append(coup_test)

				#rajout des pieces dans all_pieces et suppression de celle de listerajout
				for i in range(len(liste_rajout)):
					game.all_pieces.append(liste_rajout[0])
					liste_rajout.pop(0)

				p.deplacer(position_base[0],position_base[1],plateau_test,True)
				#print(plateau_test)
				#plateau_test = deepcopy(pl)

			# repositionne la piece a sa place initiale
			#p.deplacer(position_base[0],position_base[1],pl)
			p.rect = pygame.Rect(position_base[1]*game.taille_case, position_base[0]*game.taille_case, game.taille_case,game.taille_case)
			for i in liste_rajout:
				game.all_pieces.append(i)
			#print(coup)
								
			#print(coup_definitif)

			# changement des coup par seulement les coups legaux
			coup = (coup_definitif,coup[1],coup[2])
								
			#print(coup)
							
		# Ajout pour l'affichage des cases possible pour la piece selectioné
		for i in range(len(coup[0])):
			#(rect(x,y,taille_x,taille_y),(x,y))
			piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*game.taille_case,coup[0][i][0]*game.taille_case,game.taille_case,game.taille_case),(coup[0][i][0],coup[0][i][1])))
								
	# Sinon pour le roi
	else:
		# verification 
		coup_adversaire = coup_possible_couleur(game,p.couleur,pl)
		coup = p.coup_possible(pl,coup_adversaire)

		# test si ya echec sur le roi
		if roi_echec(game,p.couleur,pl):
			coup_definitif = []
			liste_rajout = []
			position_base = p.x,p.y
			plateau_test = deepcopy(pl)
			# pour chaque coup possible
			for coup_test in coup[0]:
				#print(coup_test)
				# deplace la piece dans un plateau fictif
				if pl[coup_test[0]][coup_test[1]]:
						
					# Parcours all_piece pour chercher la piece qui a pour coordonner la case coup_test[0],coup_test[1] pour la supprimer de la liste temporairement et la rajouter ensuite
					# pour chaque pieces dans la liste de toutes les pieces du plateau
					for piece in range(len(game.all_pieces)):
						# Si la piece a pour coordonnées la case de test
						if game.all_pieces[piece].x == coup_test[0] and game.all_pieces[piece].y == coup_test[1]:
							# Suppression de la piece et rajout dans la liste_rajout
							liste_rajout.append(game.all_pieces.pop(piece))
							break
				p.deplacer(coup_test[0],coup_test[1],plateau_test,True)
				#print(plateau_test)
				# si le roi n'est pas en echec dans cette position
				if not roi_echec(game,p.couleur,plateau_test):
					# ajout de la position dans les coup possibles
					coup_definitif.append(coup_test)

				#rajout des pieces dans all_pieces et suppression de celle de listerajout
				for i in range(len(liste_rajout)):
					game.all_pieces.append(liste_rajout[0])
					liste_rajout.pop(0)

				p.deplacer(position_base[0],position_base[1],plateau_test,True)
				#print(plateau_test)
				#plateau_test = deepcopy(pl)
										
			# repositionne la piece a sa place initiale
			#p.deplacer(position_base[0],position_base[1],pl)
			p.rect = pygame.Rect(position_base[1]*game.taille_case, position_base[0]*game.taille_case, game.taille_case,game.taille_case)
			for i in liste_rajout:
				game.all_pieces.append(i)
			#print(coup)
								
			#print(coup_definitif)

			# changement des coup par seulement les coups legaux
			coup = (coup_definitif,coup[1],coup[2])
								
			#print(coup)
							
		# test les roques ( il ne faut pas être en echec et il faut selectionner le roi)
		elif type(p) == Roi :
			if p.couleur == "b" :
				if game.prb :
					plateau_test = deepcopy(pl)
					if not pl[7][5] and not pl[7][6] and pl[7][7] == "RB":
						p.deplacer(7,5,plateau_test,True)
						if not roi_echec(game,p.couleur,plateau_test):
							p.deplacer(7,6,plateau_test,True)
							if not roi_echec(game,p.couleur,plateau_test):
								coup=(coup[0]+[(7,6)],coup[1],coup[2])

					if game.grb :
						plateau_test = deepcopy(pl)
						if not pl[7][3] and not pl[7][2] and not pl[7][1] and pl[7][0] == "RB":
							p.deplacer(7,3,plateau_test,True)
							if not roi_echec(game,p.couleur,plateau_test):
								p.deplacer(7,2,plateau_test,True)
								if not roi_echec(game,p.couleur,plateau_test):
									coup=(coup[0]+[(7,2)],coup[1],coup[2])


			else :
				if game.prn :
					plateau_test = deepcopy(pl)
					if not pl[0][5] and not pl[0][6] and pl[0][7] == "RN":
						p.deplacer(0,5,plateau_test,True)
						if not roi_echec(game,p.couleur,plateau_test):
							p.deplacer(0,6,plateau_test,True)
							if not roi_echec(game,p.couleur,plateau_test):
								coup=(coup[0]+[(0,6)],coup[1],coup[2])

					if game.grn :
						plateau_test = deepcopy(pl)
						if not pl[0][3] and not pl[0][2] and not pl[0][1] and pl[0][0] == "RN":
							p.deplacer(0,3,plateau_test,True)
							if not roi_echec(game,p.couleur,plateau_test):
								p.deplacer(0,2,plateau_test,True)
								if not roi_echec(game,p.couleur,plateau_test):
									coup=(coup[0]+[(0,2)],coup[1],coup[2])





		for i in range(len(coup[0])):
			piece_coup_possible_rect.append((pygame.Rect(coup[0][i][1]*game.taille_case,coup[0][i][0]*game.taille_case,game.taille_case,game.taille_case),(coup[0][i][0],coup[0][i][1])))


	for c in piece_coup_possible_rect:
    piece_coup_possible = [i[1] for i in piece_coup_possible]
	
	

	return (piece_coup_possible_rect,piece_coup_possible)





def coup_possible_couleur(game,couleur,pl):
	""" Renvoie une liste de tout les coups possible de toutes les pieces d'une couleur sauf le roi """


	# Liste contenent toute les possibiliter [(x,y),(x,y),(x,y),...]
	posssibiliter_adversaire = []

	# Quand la piece selectionner est blanche
	if couleur == 'b':
		
		# Pour chaque pieces 
		for i in game.all_pieces:
			# Si la piece n'est pas le roi
			if type(i) != Roi:
				# Si la couleur de la piece est celle de l'adversaire
				if i.couleur == 'n':
					
					coup = i.coup_possible(pl)
					# Ajout des coup possible a posssibiliter_adversaire
					posssibiliter_adversaire += coup[0]
					# Ajout des cases que la piece protege a posssibiliter_adversaire
					posssibiliter_adversaire += coup[2]
			
		# Renvoie posssibiliter_adversaire
		return posssibiliter_adversaire

	# Quand la piece selectionner est noire
	elif couleur == 'n':

		# Pour chaque pieces
		for i in game.all_pieces:
			# Si la piece n'est pas le roi
			if type(i) != Roi:
				# Si la couleur de la piece est celle de l'adversaire
				if i.couleur == 'b':

					coup = i.coup_possible(pl)
					#print(f"test :{pl}")
					# Ajout des coup possible a posssibiliter_adversaire
					posssibiliter_adversaire += coup[0]
					# Ajout des cases que la piece protege a posssibiliter_adversaire
					posssibiliter_adversaire += coup[2]
					
		# Renvoie posssibiliter_adversaire
		return posssibiliter_adversaire


def roi_echec(game,c,pl):
	'''Test avec un plateau si le roi est en echec
		c = couleur de celui qui joue
		pl = plateau'''

	# regarde tous les coup d'une couleur
	if c == 'b':
		coup_possible = coup_possible_couleur(game,'b',pl)

		# parcours de chaque case pour trouver le roi
		for i in range(len(pl)):
			for j in range(len(pl[i])):
				if pl[i][j] == 'KB':

					# si le roi est dans ces cases return True
					if (i,j) in coup_possible:
						return True
					
	else:
		coup_possible = coup_possible_couleur(game,'n',pl)
		#print(coup_possible)


		# parcours de chaque case pour trouver le roi
		for i in range(len(pl)):
			for j in range(len(pl[i])):
				if pl[i][j] == 'KN':
					#print(i,j)
					# si le roi est dans ces cases return True
					if (i,j) in coup_possible:
						#print("echec")
						return True

	return False



def plateau_coup_n(game, pl, n, quijoue):
	""" Calcul tout les plateau possible au coup + n
	pl : plateau de base
	n : nombre de coup a calculer """

	plateau = deepcopy(pl)

	# n = 1
        
	for piece in game.all_pieces:
		if type(piece) != Roi:
			pass


















