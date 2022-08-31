import pygame
pygame.init()
plateau = [["RN","NN","BN","QN","KN","BN","NN","RN"],           
["N" ,"N" ,"N" ,"N" ,"N" ,"N" ,"N" ,"N"],           
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],            
[0,0,0,0,0,0,0,0],            
[0,0,0,0,0,0,0,0],            
["B" ,"B" ,"B" ,"B" ,"B" ,"B" ,"B" ,"B"],            
["RB","NB","BB","QB","KB","BB","NB","RB"]]

#les pièces ont les attribut x et y qui désignent leur coordonnées
#couleur qui vaut "b" pour les pièces blanches et peu importe pour les noires
#après avoir appelé la méthode coup_possible la pièce aura les attributs listecoups qui donnent tout les coup possibles dans la configuration présente
#listesipiecebouge qui donne les coups que pourrait faire un pièce si la pièce adverse qui la bloque bouge
#la clef est la pièce qui peut bouger et la valeurs les cases qui seront accessibles
#en gros faudra vérifier quand on essaie de bouger une pièce que le roi ne soit pas dans la liste des listesipiecebouge[self.x,self.y] des pièces adverses
#et listeprotege qui contient les cases protégées par la pièce mais où elle ne peut pas se déplacer immédiatement(si une pièce alliée y est par exemple)

# coup_possible renvoie listecoups, listesipiecebouge, listeprotege


class Pion:

	def __init__(self,x,y,couleur,game):
		self.x = x
		self.y = y
		self.couleur = couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		
		

	def deplacer(self,xf,yf,pl):

		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf

	def coup_possible(self,plateau):
		x,y = self.x,self.y
		listecoups = []
		listeprotege = []

		if self.couleur == "b":

			if plateau[x-1][y] == 0:
				listecoups.append((x-1,y))

				if x == 6 :
					if plateau[4][y] == 0:
						listecoups.append((4,y))

			try :
				if plateau[x-1][y-1] != 0 and plateau[x-1][y-1][-1] == "N":
					listecoups.append((x-1,y-1))
				else :
					listeprotege.append((x-1,y-1))
			except :
				pass

			try :
				if plateau[x-1][y+1] != 0 and plateau[x-1][y+1][-1] == "N":
					listecoups.append((x-1,y+1))
				else :
					listeprotege.append((x-1,y+1))
			except :
				pass 

		else :

			if plateau[x+1][y] == 0:
				listecoups.append((x+1,y))

				if x == 1 :
					if plateau[3][y] == 0:
						listecoups.append((3,y))
			try:
				if plateau[x+1][y-1] != 0 and plateau[x+1][y-1][-1] == "B":
					listecoups.append((x+1,y-1))
				else :
					listeprotege.append((x+1,y-1))
			except:
				pass
			try:
				if plateau[x+1][y+1] != 0 and plateau[x+1][y+1][-1] == "B":
					listecoups.append((x+1,y+1))
				else :
					listeprotege.append((x+1,y+1))
			except:
				pass

		self.listecoups = listecoups
		self.listesipiecebouge = {}
		self.listeprotege = listeprotege
		
		return listecoups, {}, listeprotege

class Tour:

	def __init__(self,x,y,couleur,game):
		self.x = x
		self.y = y
		self.couleur = couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		

	def deplacer(self,xf,yf,pl):
		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf


	def coup_possible(self,plateau):
		x,y = self.x,self.y
		#liste des coups possibles immédiatement
		listecoups = []
		#dictionnaire des coups si une piece adverse bouge ( pour empêcher l'adversaire de se mettre lui même en échec en bougeant une de ses pièces)
		#la clef est la pièce qui peut bouger et la valeurs les cases qui seront accessibles
		#en gros faudra vérifier quand on essaie de bouger une pièce que le roi ne soit pas dans la liste des listesipiecebouge[self.x,self.y] des pièces adverses.
		listesipiecebouge = {}

		listeprotege = []
		if self.couleur == "b": 
			c= "N"
		else : 
			c="B"

		max_haut, max_bas,max_gauche,max_droite = x,7-x, y,7-y
		ok = True
		n = 1
		while ok and n <= max_haut:
			if plateau[x-n][y] == 0 :
				listecoups.append((x-n,y))
				n+=1
			elif plateau[x-n][y][-1] == c:
				listecoups.append((x-n,y))
				xbloque,ybloque = x-n, y
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_haut:
					if plateau[x-n][y] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y))
					elif plateau[x-n][y][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y))
				ok = False

		ok = True
		n = 1

		while ok and n <= max_bas:
			if plateau[x+n][y] == 0 :
				listecoups.append((x+n,y))
				n+=1
			elif plateau[x+n][y][-1] == c:
				listecoups.append((x+n,y))
				xbloque,ybloque = x+n, y
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_bas:
					if plateau[x+n][y] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y))
					elif plateau[x+n][y][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y))
				ok = False

		ok = True
		n = 1
		while ok and n <= max_gauche:
			if plateau[x][y-n] == 0 :
				listecoups.append((x,y-n))
				n+=1
			elif plateau[x][y-n][-1] == c:
				listecoups.append((x,y-n))
				xbloque,ybloque = x, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_gauche:
					if plateau[x][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x,y-n))
					elif plateau[x][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x,y-n))
				ok = False

		ok = True
		n = 1

		while ok and n <= max_droite:
			if plateau[x][y+n] == 0 :
				listecoups.append((x,y+n))
				n+=1
			elif plateau[x][y+n][1] == c:
				listecoups.append((x,y+n))
				xbloque,ybloque = x, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_droite:
					if plateau[x][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x,y+n))
					elif plateau[x][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x,y+n))
				ok = False
		
		

		self.listesipiecebouge = listesipiecebouge
		self.listecoups = listecoups
		self.listeprotege = listeprotege
		
		return listecoups, listesipiecebouge, listeprotege

class Fou:
	def __init__(self,x,y,couleur,game):
		self.x = x
		self.y = y
		self.couleur = couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		

	def deplacer(self,xf,yf,pl):
		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf

	def coup_possible(self,plateau):
		x,y = self.x,self.y
		listecoups = []
		listesipiecebouge = {}
		listeprotege = []
		if self.couleur == "b": 
			c= "N"
		else : 
			c="B"

		max_haut, max_bas,max_gauche,max_droite = x,7-x, y,7-y
		ok = True
		n = 1
		while ok and n <= min(max_haut,max_gauche):
			if plateau[x-n][y-n] == 0 :
				listecoups.append((x-n,y-n))
				n+=1
			elif plateau[x-n][y-n][-1] == c:
				listecoups.append((x-n,y-n))
				xbloque,ybloque = x-n, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_haut,max_gauche):
					if plateau[x-n][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y-n))
					elif plateau[x-n][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y-n))
				ok = False

		ok = True
		n = 1

		while ok and n <= min(max_bas,max_droite):
			if plateau[x+n][y+n] == 0 :
				listecoups.append((x+n,y+n))
				n+=1
			elif plateau[x+n][y+n][-1] == c:
				listecoups.append((x+n,y+n))
				xbloque,ybloque = x+n, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_bas,max_droite):
					if plateau[x+n][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y+n))
					elif plateau[x+n][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y+n))
				ok = False

		ok = True
		n = 1
		while ok and n <= min(max_haut,max_droite):
			if plateau[x-n][y+n] == 0 :
				listecoups.append((x-n,y+n))
				n+=1
			elif plateau[x-n][y+n][-1] == c:
				listecoups.append((x-n,y+n))
				xbloque,ybloque = x-n, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_haut,max_droite):
					if plateau[x-n][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y+n))
					elif plateau[x-n][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y+n))
				ok = False

		ok = True
		n = 1

		while ok and n <= min(max_bas,max_gauche):
			if plateau[x+n][y-n] == 0 :
				listecoups.append((x+n,y-n))
				n+=1
			elif plateau[x+n][y-n][-1] == c:
				listecoups.append((x+n,y-n))
				xbloque,ybloque = x+n, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_bas,max_gauche):
					if plateau[x+n][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y-n))
					elif plateau[x+n][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y-n))
				ok = False
		
		

		self.listesipiecebouge = listesipiecebouge
		self.listecoups = listecoups
		self.listeprotege = listeprotege

		return listecoups, listesipiecebouge, listeprotege

class Dame :
	def __init__(self,x,y,couleur,game):
		self.x,self.y,self.couleur = x,y,couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		

	def deplacer(self,xf,yf,pl):
		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf

	def coup_possible(self,plateau):

		x,y = self.x,self.y
		listecoups = []
		listesipiecebouge = {}
		listeprotege = []
		if self.couleur == "b": 
			c= "N"
		else : 
			c="B"

		max_haut, max_bas,max_gauche,max_droite = x,7-x, y,7-y
		ok = True
		n = 1
		while ok and n <= min(max_haut,max_gauche):
			if plateau[x-n][y-n] == 0 :
				listecoups.append((x-n,y-n))
				n+=1
			elif plateau[x-n][y-n][-1] == c:
				listecoups.append((x-n,y-n))
				xbloque,ybloque = x-n, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_haut,max_gauche):
					if plateau[x-n][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y-n))
					elif plateau[x-n][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y-n))
				ok = False

		ok = True
		n = 1

		while ok and n <= min(max_bas,max_droite):
			if plateau[x+n][y+n] == 0 :
				listecoups.append((x+n,y+n))
				n+=1
			elif plateau[x+n][y+n][-1] == c:
				listecoups.append((x+n,y+n))
				xbloque,ybloque = x+n, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_bas,max_droite):
					if plateau[x+n][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y+n))
					elif plateau[x+n][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y+n))
				ok = False

		ok = True
		n = 1
		while ok and n <= min(max_haut,max_droite):
			if plateau[x-n][y+n] == 0 :
				listecoups.append((x-n,y+n))
				n+=1
			elif plateau[x-n][y+n][-1] == c:
				listecoups.append((x-n,y+n))
				xbloque,ybloque = x-n, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_haut,max_droite):
					if plateau[x-n][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y+n))
					elif plateau[x-n][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y+n))
				ok = False

		ok = True
		n = 1

		while ok and n <= min(max_bas,max_gauche):
			if plateau[x+n][y-n] == 0 :
				listecoups.append((x+n,y-n))
				n+=1
			elif plateau[x+n][y-n][-1] == c:
				listecoups.append((x+n,y-n))
				xbloque,ybloque = x+n, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= min(max_bas,max_gauche):
					if plateau[x+n][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y-n))
					elif plateau[x+n][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y-n))
				ok = False
		
		

		ok = True
		n = 1
		while ok and n <= max_haut:
			if plateau[x-n][y] == 0 :
				listecoups.append((x-n,y))
				n+=1
			elif plateau[x-n][y][-1] == c:
				listecoups.append((x-n,y))
				xbloque,ybloque = x-n, y
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_haut:
					if plateau[x-n][y] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y))
					elif plateau[x-n][y][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x-n,y))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x-n,y))
				ok = False

		ok = True
		n = 1

		while ok and n <= max_bas:
			if plateau[x+n][y] == 0 :
				listecoups.append((x+n,y))
				n+=1
			elif plateau[x+n][y][-1] == c:
				listecoups.append((x+n,y))
				xbloque,ybloque = x+n, y
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_bas:
					if plateau[x+n][y] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y))
					elif plateau[x+n][y][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x+n,y))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x+n,y))
				ok = False

		ok = True
		n = 1
		while ok and n <= max_gauche:
			if plateau[x][y-n] == 0 :
				listecoups.append((x,y-n))
				n+=1
			elif plateau[x][y-n][-1] == c:
				listecoups.append((x,y-n))
				xbloque,ybloque = x, y-n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_gauche:
					if plateau[x][y-n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x,y-n))
					elif plateau[x][y-n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x,y-n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x,y-n))
				ok = False

		ok = True
		n = 1

		while ok and n <= max_droite:
			if plateau[x][y+n] == 0 :
				listecoups.append((x,y+n))
				n+=1
			elif plateau[x][y+n][1] == c:
				listecoups.append((x,y+n))
				xbloque,ybloque = x, y+n
				listesipiecebouge[(xbloque,ybloque)] = []
				n+=1
				while ok and n <= max_droite:
					if plateau[x][y+n] == 0 :
						listesipiecebouge[(xbloque,ybloque)].append((x,y+n))
					elif plateau[x][y+n][-1] == c:
						listesipiecebouge[(xbloque,ybloque)].append((x,y+n))
						ok = False
					else :
						ok = False
					n+=1
			else :
				listeprotege.append((x,y+n))
				ok = False
		
		

		self.listesipiecebouge = listesipiecebouge
		self.listecoups = listecoups
		self.listeprotege = listeprotege

		return listecoups, listesipiecebouge, listeprotege

class Cavalier :

	def __init__(self,x,y,couleur,game):
		self.x = x
		self.y = y
		self.couleur = couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		

	def deplacer(self,xf,yf,pl):
		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf

	def coup_possible(self,plateau):
		x,y = self.x,self.y
		listecoups = []
		listeprotege = []

		if self.couleur == "b":
			c = "N"
		else : 
			c = "B"

		try :
			if plateau[x+2][y+1] == 0 or plateau[x+2][y+1][-1] == c:
				listecoups.append((x+2,y+1))
			else : 
				listeprotege.append((x+2,y+1))
		except :
			pass

		try :
			if x >1 and (plateau[x-2][y+1] == 0 or plateau[x-2][y+1][-1] == c):
				listecoups.append((x-2,y+1))
			elif x >1:
				listeprotege.append((x-2,y+1))

		except :
			pass

		try :
			if y>0 and (plateau[x+2][y-1] == 0 or plateau[x+2][y-1][-1] == c):
				listecoups.append((x+2,y-1))
			elif y>0 :
				listeprotege.append((x+2,y-1))
		except :
			pass

		try :
			if x >1 and y> 0 and (plateau[x-2][y-1] == 0 or plateau[x-2][y-1][-1] == c):
				listecoups.append((x-2,y-1))
			elif x >1 and y> 0 :
				listeprotege.append((x-2,y-1))
		except :
			pass

		try :
			if plateau[x+1][y+2] == 0 or plateau[x+1][y+2][-1] == c:
				listecoups.append((x+1,y+2))
			else :
				listeprotege.append((x+1,y+2))
		except :
			pass

		try :
			if x >0 and (plateau[x-1][y+2] == 0 or plateau[x-1][y+2][-1] == c):
				listecoups.append((x-1,y+2))
			elif x>0 :
				listeprotege.append((x-1,y+2))

		except :
			pass

		try :
			if y >1 and (plateau[x+1][y-2] == 0 or plateau[x+1][y-2][-1] == c):
				listecoups.append((x+1,y-2))
			elif y >1 :
				listeprotege.append((x+1,y-2))
		except :
			pass

		try :
			if  y >1 and x> 0 and (plateau[x-1][y-2] == 0 or plateau[x-1][y-2][-1] == c):
				listecoups.append((x-1,y-2))
			elif y>1 and x>0 :
				listeprotege.append((x-1,y-2))
		except :
			pass 

		

		self.listecoups = listecoups	
		self.listesipiecebouge = {}
		self.listeprotege = []

		return listecoups, {}, []

class Roi :
	def __init__(self,x,y,couleur,game):
		self.x = x
		self.y = y
		self.couleur = couleur
		self.game = game
		self.rect = pygame.Rect(self.y*self.game.taille_case, self.x*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		

	def deplacer(self,xf,yf,pl):
		pl[xf][yf] = pl[self.x][self.y]
		pl[self.x][self.y] = 0
		self.rect = pygame.Rect(yf*self.game.taille_case, xf*self.game.taille_case, self.game.taille_case,self.game.taille_case)
		self.x, self.y = xf, yf

	def coup_possible(self,plateau,listecoupadverse):
		#listecoupadverse est une liste composée des listecoups et listeprotege des pièces adverses
		listecoups = []
		listeprotege = []

		x,y = self.x,self.y

		if self.couleur == "b":
			c = "N"
		else : 
			c = "B"

		try :
			if plateau[x+1][y+1] == 0 or plateau[x+1][y+1][-1] == c:
				listecoups.append((x+1,y+1))
			else : 
				listeprotege.append((x+1,y+1))
		except :
			pass

		try :
			if x >0 and (plateau[x-1][y+1] == 0 or plateau[x-1][y+1][-1] == c):
				listecoups.append((x-1,y+1))
			else : 
				listeprotege.append((x-1,y+1))
		except :
			pass

		try :
			if y>0 and (plateau[x+1][y-1] == 0 or plateau[x+1][y-1][-1] == c):
				listecoups.append((x+1,y-1))

			else : 
				listeprotege.append((x+1,y-1))
		except :
			pass

		try :
			if x >0 and y> 0 and (plateau[x-1][y-1] == 0 or plateau[x-1][y-1][-1] == c):
				listecoups.append((x-1,y-1))
			else : 
				listeprotege.append((x-1,y-1))
		except :
			pass

		try :
			if x >0 and (plateau[x-1][y] == 0 or plateau[x-1][y][-1] == c):
				listecoups.append((x-1,y))
			else : 
				listeprotege.append((x-1,y))
		except :
			pass
		try :
			if y>0 and (plateau[x][y-1] == 0 or plateau[x][y-1][-1] == c):
				listecoups.append((x,y-1))
			else : 
				listeprotege.append((x,y-1))
		except :
			pass

		try :
			if plateau[x][y+1] == 0 or plateau[x][y+1][-1] == c:
				listecoups.append((x,y+1))
			else : 
				listeprotege.append((x,y+1))
		except :
			pass
		try :
			if plateau[x+1][y] == 0 or plateau[x+1][y][-1] == c:
				listecoups.append((x+1,y))
			else : 
				listeprotege.append((x+1,y))

		except :
			pass
		print(listecoups)
		listepop = []
		for i in range(len(listecoups)) :
			if listecoups[i] in listecoupadverse :
				listepop.append(i)
		
		n = 0
		for i in listepop :
			listecoups.pop(i-n)
			n+=1
		listepop = []
		for i in range(len(listeprotege)) :
			if listeprotege[i] in listecoupadverse:
				listepop.append(i)
		n = 0
		for i in listepop:
			listeprotege.pop(i-n)
			n+=1

		self.listecoups = listecoups
		self.listesipiecebouge = {}
		self.listeprotege = listeprotege

		return listecoups, {}, listeprotege

		



#test
#l = []
#for x in range(8):
	#for y in range(8):
		#if plateau[x][y] != 0 and plateau[x][y] != "K" and plateau[x][y][0] == "K":
			#l.append(roi(x,y,plateau[x][y][-1].lower()))
#d={}
 #for i in l:
	#i.coup_possible(plateau,[(2,1)])
	#d[(i.x,i.y)] = (i.listecoups,i.listesipiecebouge)

#print(d)
