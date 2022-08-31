# initialisation:
# --------------

# initialisation de la liste représentant les cases vides
case_exclue=[]
# initialisation des colonnes de l'échiquier
colonne=[1,2,3,4,5,6,7,8]
# initialisation des lignes de l'échiquier
ligne=[1,2,3,4,5,6,7,8]
# initialisation des différentes pièces existant au échec
type_piece=['pion','tour','cavalier','fou','reine','roi']
# initialisation de la valeur d'une pièce de l'échiquier
valeur_piece=int()
# initialisation de la présence d'une pièce sur l'échiquier
etat=['present','supprime']
# initialisation constituant la dangerosité de la pièce ennemie envers la pièce alliée
menace=False
# initialisation de la liste contenant les couleurs attribué à chaque pièce
couleur=['blanc','noir']
# initialisation de la variable de point servant à évaluer la pièce qui va se déplacer
eval_real=float()
# initialisation de la colonne de la case où la pièce voudrait se déplacer
colonne_propose=[1,2,3,4,5,6,7,8]
# initialisation de la ligne de la case où la pièce voudrait se déplacer
ligne_propose=[1,2,3,4,5,6,7,8]


# fonction servant à établir la position la position de chaque pièce lors du tour 0
def acquisition_conf_pieces(couleur,choix_str):

    # fonction servant à traduire les coordonnées de chaque pièce afin de les placer
    def convert_col(a):
        # initialisation de la colonne qui va servir a traduire les colonne de 'A' à 'H' dans l'échequier en une variable int()
        col=0
        # initialisation de la conversion des lettres en entier int() comme vrai
        convert=True
        # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'a' ou soit 'A'
        if a[0:1]=='a'or a[0:1]=='A':
            # alors la colonne de la pièce est à 1
            col=1
        else:
            # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'b' ou soit 'B'
            if a[0:1]=='b'or a[0:1]=='B':
                # alors la colonne de la pièce est à 2
                col=2
            else:
                # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'c' ou soit 'C'
                if a[0:1]=='c'or a[0:1]=='C':
                    # alors la colonne de la pièce est à 3
                    col=3
                else:
                    # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'd' ou soit 'D'
                    if a[0:1]=='d'or a[0:1]=='D':
                        # alors la colonne de la pièce est à 4
                        col=4
                    else:
                        # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'e' ou soit 'E'
                        if a[0:1]=='e'or a[0:1]=='E':
                            # alors la colonne de la pièce est à 5
                            col=5
                        else:
                            # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'f' ou soit 'F'
                            if a[0:1]=='f'or a[0:1]=='F':
                                # alors la colonne de la pièce est à 6
                                col=6
                            else:
                                # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'g' ou soit 'G'
                                if a[0:1]=='g'or a[0:1]=='G':
                                    # alors la colonne de la pièce est à 7
                                    col=7
                                else:
                                    # si le premier caractère de la variable input() "a" (donnant la position de la pièce) est soit 'h' ou soit 'H'
                                    if a[0:1]=='h'or a[0:1]=='H':
                                        # alors la colonne de la pièce est à 8
                                        col=8
                                    else:
                                        #ou sinon afficher que la valeur ne peut pas être reconnu
                                        print ('numéro de colonne non reconnu')
                                        # marquer que la conversion des lettres en entier int() est fausse
                                        convert=False
        # renvoie de la colonne et de la conversion des lettres en nombres afin de repérer les coordonnées des pièces
        return col,convert

    # initialisation de la variable permettant de choisir si le placement des pièces sont automatiques ou fait manuellement
    choix=int(choix_str)
    # si cette variable est égale à 1
    if choix==1:
        # si la couleur choisis des pièces est blanches
        if couleur=='blanc':
            print('Rentrez les cases des pièces blanches, les pieces sont presentées de gauche à droite vue des blancs')
            # initialisation de la liste contenant les caractéristiques de chaque pièce blanche
            pos_blanc=[]
            # le premier élément de cette liste (pos_blanc[0]) est vide
            pos_blanc.append('')
        if couleur=='noir':
            print('Maintenant rentrez les cases des pièces noires, les pieces sont presentées de gauche à droite vue des blancs')
            # initialisation de la liste contenant les caractéristiques de chaque pièce noire
            pos_noir=[]
            # le premier élément de cette liste (pos_noir[0]) est vide
            pos_noir.append('')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du premier pion (par exemple : C1)
            a=input('Pion 1 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # si la conversion est possible
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
                else:
                    # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                    print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du deuxième pion (par exemple : C2)
            a=input('Pion 2 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du troisième pion (par exemple : C3)
            a=input('Pion 3 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du quatrième pion (par exemple : C4)
            a=input('Pion 4 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du cinquième pion (par exemple : C5)
            a=input('Pion 5 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du sixième pion (par exemple : C6)
            a=input('Pion 6 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du septième pion (par exemple : C7)
            a=input('Pion 7: ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du huitième pion (par exemple : C8)
            a=input('Pion 8 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'pion',1,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'pion',1,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position de la première tour (par exemple : D1)
            a=input('Tour 1 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'tour',5,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'tour',5,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du premier cheval (par exemple : D2)
            a=input('Cheval 1 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'cheval',3,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'cheval',3,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du premier fou (par exemple : D3)
            a=input('Fou 1 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'fou',3,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'fou',3,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position de la reine (par exemple : D4)
            a=input('Reine : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'reine',10,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'reine',10,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du roi (par exemple : D5)
            a=input('Roi : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'roi',10,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'roi',10,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du second fou (par exemple : D6)
            a=input('Fou 2 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'fou',3,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'fou',3,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position du second cheval (par exemple : D7)
            a=input('Cheval 2 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # -
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'cheval',3,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'cheval',3,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # initialisation en booléen indiquant des lettres extérieurs au colonnes (c'est à dire de H à Z)
        convert=False
        # tant que la conversion n'est pas possible
        while convert==False:
            # demander la position de la seconde tour (par exemple : D8)
            a=input('Tour 2 : ')
            # appel de la fonction convert_col(a) afin d'extraire "col" vers "col_str" et "convert" vers "convert"
            col_str,convert=convert_col(a)
            # si la conversion est possible
            if convert==True:
                # la valeur de "col_str" est affecté à la valeur de colonne de la pièce
                col=int(col_str)
                # la valeur de la ligne est égale au second caractère envoyé dans "a"
                lig=int(a[1:2])
                # afficher la position de la pièce
                print('col=',col,'lig=',lig)
                # si sa couleur est blanche
                if couleur=='blanc':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_blanc
                    pos_blanc.append([col,lig,'tour',5,'present',False,0,col,lig])
                # si sa couleur est noire
                if couleur=='noir':
                    # alors on ajoute les caractéristiques de la pièce dans la liste pos_noir
                    pos_noir.append([col,lig,'tour',5,'present',False,0,col,lig])
            else:
                # afficher un message d'erreur si la pièce n'est ni blanche ni noire
                print('recommencez')

        # si la couleur choisie des pièces est blanche
        if couleur=='blanc':
            # renvoie de la liste donnant les caractériqtiques de chaque pièce blanche
            return pos_blanc
            # afficher la liste
            print('pos blanc acquis',pos_blanc)
        # si la couleur choisie des pièces est noire
        if couleur=='noir':
            # renvoie de la liste donnant les caractériqtiques de chaque pièce noire
            return pos_noir
            # afficher la liste
            print('pos noir acquis',pos_noir)

    else:
        # si on désire que les pièces soit placées de base automatiquement et que la couleur des pièces est blanche
        if choix==2 and couleur=='blanc':
            print('Position des blancs dans la configuration par défaut')
            # initialisation de la liste qui caractérise chaque pièce blanche
            pos_blanc=[]
            pos_blanc.append(0)
            pos_blanc.append([2,5,'pion',1,'present',False,0,2,5])
            print('pion1 en case (B,5)')
            pos_blanc.append([3,6,'pion',1,'present',False,0,3,6])
            print('pion2 en case (C,6)')
            pos_blanc.append([3,3,'pion',1,'present',False,0,3,3])
            print('pion3 en case (C,3)')
            pos_blanc.append([4,2,'pion',1,'present',False,0,4,2])
            print('pion4 en case (D,2)')
            pos_blanc.append([5,2,'pion',1,'present',False,0,5,2])
            print('pion5 en case (E,2)')
            pos_blanc.append([6,2,'pion',1,'present',False,0,6,2])
            print('pion6 en case (F,2)')
            pos_blanc.append([7,2,'pion',1,'present',False,0,7,2])
            print('pion7 en case (G,2)')
            pos_blanc.append([8,2,'pion',1,'present',False,0,8,2])
            print('pion8 en case (H,2)')
            pos_blanc.append([3,1,'tour',5,'present',False,0,3,1])
            print('tour en case (C,1)')
            pos_blanc.append([2,3,'cavalier',3,'present',False,0,2,3])
            print('cheval en case (B;3)')
            pos_blanc.append([5,3,'fou',3,'present',False,0,5,3])
            print('fou en case (E,3)')
            pos_blanc.append([4,1,'reine',10,'present',False,0,4,1])
            print('reine en case (D,1)')
            pos_blanc.append([5,1,'roi',10,'present',False,0,5,1])
            print('roi en case (E,1)')
            pos_blanc.append([5,4,'fou',3,'present',False,0,5,4])
            print('fou en case (E,4)')
            pos_blanc.append([7,1,'cavalier',3,'present',False,0,7,1])
            print('cavalier en case (G,1)')
            pos_blanc.append([8,1,'tour',5,'present',False,0,8,1])
            print('tour en case (H,1)')
            return pos_blanc

        else:
            # si on désire que les pièces soit placées de base automatiquement et que la couleur des pièces est noire
            if choix==2 and couleur=='noir':
                print('Position des noirs dans la configuration par défaut')
                # initialisation de la liste qui caractérise chaque pièce noire
                pos_noir=[]
                pos_noir.append('')
                pos_noir.append([1,5,'pion',1,'present',False,0,1,5])
                print('pion1 en case (A,5)')
                pos_noir.append([2,7,'pion',1,'present',False,0,2,7])
                print('pion2 en case (B,7)')
                pos_noir.append([3,7,'pion',1,'present',False,0,3,7])
                print('pion3 en case (C,7)')
                pos_noir.append([3,5,'pion',1,'present',False,0,3,5])
                print('pion4 en case (C,5)')
                pos_noir.append([5,7,'pion',1,'present',False,0,5,7])
                print('pion5 en case (E,7)')
                pos_noir.append([6,6,'pion',1,'present',False,0,6,6])
                print('pion6 en case (F,6)')
                pos_noir.append([7,5,'pion',1,'present',False,0,7,5])
                print('pion7 en case (G,5)')
                pos_noir.append([8,6,'pion',1,'present',False,0,8,6])
                print('pion8 en case (H,6)')
                pos_noir.append([1,8,'tour',5,'present',False,0,1,8])
                print('tour en case (A,8)')
                pos_noir.append([2,8,'cavalier',3,'present',False,0,2,8])
                print('cheval en case (B;8)')
                pos_noir.append([5,6,'fou',3,'present',False,0,5,6])
                print('fou en case (E,6)')
                pos_noir.append([4,7,'reine',10,'present',False,0,4,7])
                print('reine en case (D,7)')
                pos_noir.append([4,8,'roi',10,'present',False,0,4,8])
                print('roi en case (D,8)')
                pos_noir.append([6,8,'fou',3,'present',False,0,6,8])
                print('fou en case (F,8)')
                pos_noir.append([2,6,'cavalier',3,'present',False,0,2,6])
                print('cavalier en case (B,6)')
                pos_noir.append([8,5,'tour',5,'present',False,0,8,5])
                print('tour en case (H,5)')
                return pos_noir

# initialisation de la liste contenant les cases interdites aux pièces blanches
liste_positions_exclues_aux_blancs=[
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False]]

# initialisation de la liste contenant les cases interdites aux pièces noires
liste_positions_exclues_aux_noirs=[
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False]]

# initialisation du compteur parcourant les indices de la liste pos_blanc et pos_noir
p=0

# fonction servant à detecter si une case est interdite à franchir
def Bloque_par_autre_blanc(colonne,ligne,etat_bloque):
    # initialisation de la case interdite comme fausse (la case est donc franchissable)
    etat_bloque=False
    # initialisation du compteur parcourant les indices de la liste pos_blanc
    p=0
    # tant que la case interdite est fausse et que le compteur parcourant les indices de la liste est inférieur à 16
    while etat_bloque==False and p<16:
        # on rajoute 1 au compteur
        p+=1
        # si la colonne et la ligne exploitée est égale à la colonne et à la ligne d'une pièce blanche
        if colonne==pos_blanc[p][0] and ligne==pos_blanc[p][1]:
            # alors la case est infranchissable
            etat_bloque=True
        else:
            # sinon la case est franchissable
            etat_bloque=False
    # renvoie si la case est franchissable ou infranchissable
    return etat_bloque

# fonction servant à supprimer une pièce noire si la pièce blanche parvient à l'attraper
def Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression):
    # initialisation du compteur parcourant les indices de la liste pos_noir
    p=0
    # tant que la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper) et que le compteur parcourant les indices de la liste est inférieur à 16
    while etat_suppression==False and p<16:
        # on rajoute 1 au compteur
        p+=1
        # si la colonne et la ligne exploitée est égale à la colonne et à la ligne d'une pièce noir
        if colonne==pos_noir[p][0] and ligne==pos_noir[p][1]:
            # alors la valeur de la pièce noire est placé dans une variable qui stocke la valeur de la pièce
            valeur_piece_à_supprimer=pos_noir[p][3]
            # et la case permettant de supprimer la pièce est vrai
            etat_suppression=True
        else:
            # sinon la case permettant de supprimer la pièce est fausse
            etat_suppression=False
    # renvoie de la variable qui stocke la valeur de la pièce est renvoie si la case permettant de supprimer la pièce est vrai ou fausse
    return valeur_piece_à_supprimer, etat_suppression

# la fonction evaluation position des blancs: dans le cas où on n'est pas bloqué par une autre pièce blanche on examine si une autre pièce noire est atteignable à partir de la nouvelle position
# la variable "retour_eval" retourne la valeur de pièce noire atteignable directement par la nouvelle position du blanc. Cette valeur est réduite d’un facteur 2
def evaluation_position_blanc(type,colonne_visee,ligne_visee,retour_eval):
    # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
    retour_eval=0
    # intialisation d'une variable accumulant la valeur des pièces adverses afin de déterminer le meilleur déplacement
    valeur_piece_à_supprimer=0

    # si la pièce choisie est un fou
    if type=='fou':

        # première diagonale:
        # ------------------

        # initialisation d'un compteur pacourant les lignes et les colonnes
        n=1
        # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
        etat_suppression=False
        # initialisation de la case comme franchissable
        etat_bloque=False
        # la colonne après le déplacement potentiel de la pièce est affecté à la colonne où il se situe de base
        colonne=colonne_visee
        # la ligne après le déplacement potentiel de la pièce est affecté à la ligne où il se situe de base
        ligne=ligne_visee
        # tant qu'on ne peut pas attraper une pièce adverse ou qu'on ne peut pas franchir une case ou qu'on atteint le bord de l'échiquier
        while not(etat_suppression==True or etat_bloque==True or colonne==8 or ligne==8):
            # la colonne visée a avancée de 1 par rapport à la colonne de base
            colonne=colonne_visee+n
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+n
            # on affecte à "u" le booléen "etat_bloque" dans la fonction "Bloque_par_autre_blanc" afin de déterminer les cases infranchissables
            u=Bloque_par_autre_blanc(colonne,ligne,etat_bloque)
            # on affecte l'"etat_bloque" dans la fonction "Bloque_par_autre_blanc" vers l'"etat_bloque" de cette fonction
            etat_bloque=u
            # si "etat_bloque" est resté comme fausse
            if u==False:
                # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
                (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
                # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
                if y==True:
                    # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                    # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                    retour_eval+=x/2
                    # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                    etat_suppression=y
            # on ajoute 1 à n pour parcourir toute les cases du fou
            n+=1

        # deuxième diagonale:
        # ------------------

        # initialisation d'un compteur pacourant les lignes et les colonnes
        n=1
        # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
        etat_suppression=False
        # initialisation de la case comme franchissable
        etat_bloque=False
        # la colonne après le déplacement potentiel de la pièce est affecté à la colonne où il se situe de base
        colonne=colonne_visee
        # la ligne après le déplacement potentiel de la pièce est affecté à la ligne où il se situe de base
        ligne=ligne_visee
        # tant qu'on ne peut pas attraper une pièce adverse ou qu'on ne peut pas franchir une case ou qu'on atteint le bord de l'échiquier
        while not(etat_suppression==True or etat_bloque==True or colonne==8 or ligne==1):
            # la colonne visée a avancée de 1 par rapport à la colonne de base
            colonne=colonne_visee+n
            # la ligne visée a reculée de 1 par rapport à la ligne de base
            ligne=ligne_visee-n
            # on affecte à "u" le booléen "etat_bloque" dans la fonction "Bloque_par_autre_blanc" afin de déterminer les cases infranchissables
            u=Bloque_par_autre_blanc(colonne,ligne,etat_bloque)
            # on affecte l'"etat_bloque" dans la fonction "Bloque_par_autre_blanc" vers l'"etat_bloque" de cette fonction
            etat_bloque=u
            # si "etat_bloque" est resté comme fausse
            if u==False:
                # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
                (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
                # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
                if y==True:
                    # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                    # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                    retour_eval+=x/2
                    # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                    etat_suppression=y
            # on ajoute 1 à n pour parcourir toute les cases du fou
            n+=1

        # troisème diagonale:
        # ------------------

        # initialisation d'un compteur pacourant les lignes et les colonnes
        n=1
        # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
        etat_suppression=False
        # initialisation de la case comme franchissable
        etat_bloque=False
        # la colonne après le déplacement potentiel de la pièce est affecté à la colonne où il se situe de base
        colonne=colonne_visee
        # la ligne après le déplacement potentiel de la pièce est affecté à la ligne où il se situe de base
        ligne=ligne_visee
        # tant qu'on ne peut pas attraper une pièce adverse ou qu'on ne peut pas franchir une case ou qu'on atteint le bord de l'échiquier
        while not(etat_suppression==True or etat_bloque==True or colonne==1 or ligne==1):
            # la colonne visée a reculée de 1 par rapport à la colonne de base
            colonne=colonne_visee-n
            # la ligne visée a reculée de 1 par rapport à la ligne de base
            ligne=ligne_visee-n
            # on affecte à "u" le booléen "etat_bloque" dans la fonction "Bloque_par_autre_blanc" afin de déterminer les cases infranchissables
            u=Bloque_par_autre_blanc(colonne,ligne,etat_bloque)
            # on affecte l'"etat_bloque" dans la fonction "Bloque_par_autre_blanc" vers l'"etat_bloque" de cette fonction
            etat_bloque=u
            # si "etat_bloque" est resté comme fausse
            if u==False:
                # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
                (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
                # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
                if y==True:
                    # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                    # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                    retour_eval+=x/2
                    # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                    etat_suppression=y
            # on ajoute 1 à n pour parcourir toute les cases du fou
            n+=1

        # quatrième diagonale:
        # -------------------

        # initialisation d'un compteur pacourant les lignes et les colonnes
        n=1
        # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
        etat_suppression=False
        # initialisation de la case comme franchissable
        etat_bloque=False
        # la colonne après le déplacement potentiel de la pièce est affecté à la colonne où il se situe de base
        colonne=colonne_visee
        # la ligne après le déplacement potentiel de la pièce est affecté à la ligne où il se situe de base
        ligne=ligne_visee
        # tant qu'on ne peut pas attraper une pièce adverse ou qu'on ne peut pas franchir une case ou qu'on atteint le bord de l'échiquier
        while not(etat_suppression==True or etat_bloque==True or colonne==1 or ligne==8):
            # la colonne visée a reculée de 1 par rapport à la colonne de base
            colonne=colonne_visee-n
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+n
            # on affecte à "u" le booléen "etat_bloque" dans la fonction "Bloque_par_autre_blanc" afin de déterminer les cases infranchissables
            u=Bloque_par_autre_blanc(colonne,ligne,etat_bloque)
            # on affecte l'"etat_bloque" dans la fonction "Bloque_par_autre_blanc" vers l'"etat_bloque" de cette fonction
            etat_bloque=u
            # si "etat_bloque" est resté comme fausse
            if u==False:
                # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
                (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
                # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
                if y==True:
                    # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                    # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                    retour_eval+=x/2
                    # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                    etat_suppression=y
            # on ajoute 1 à n pour parcourir toute les cases du fou
            n+=1

    # si la pièce choisie est un pion
    if type=='pion':

        # verification à droite:
        # ---------------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee!=8 and ligne_visee!=8:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a avancée de 1 par rapport à la colonne de base
            colonne=colonne_visee+1
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # verification à gauche:
        # ---------------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee!=1 and ligne_visee!=8:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a reculée de 1 par rapport à la colonne de base
            colonne=colonne_visee-1
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

    # si la pièce choisie est un cavalier
    if type=='cavalier':
        # initialisation du booléen  des cases infranchissables comme fausse
        bloque_par_blanc=False

        # premier cas:
        # -----------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if  colonne_visee<=6 and ligne_visee<=7:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a avancée de 2 par rapport à la colonne de base
            colonne=colonne_visee+2
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # deuxième cas:
        # ------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee<=7 and ligne_visee<=6:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a avancée de 1 par rapport à la colonne de base
            colonne=colonne_visee+1
            # la ligne visée a avancée de 2 par rapport à la ligne de base
            ligne=ligne_visee+2
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

	    # troisième cas:
        # -------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee>=3 and ligne_visee>=2:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a reculée de 2 par rapport à la colonne de base
            colonne=colonne_visee-2
            # la ligne visée a reculée de 1 par rapport à la ligne de base
            ligne=ligne_visee-1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # quatrième cas:
        # -------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee>=2 and ligne_visee>=3:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a reculée de 1 par rapport à la colonne de base
            colonne=colonne_visee-1
            # la ligne visée a reculée de 2 par rapport à la ligne de base
            ligne=ligne_visee-2
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # cinquième cas:
        # -------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee<=6 and ligne_visee>=2:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a avancée de 2 par rapport à la colonne de base
            colonne=colonne_visee+2
            # la ligne visée a reculée de 1 par rapport à la ligne de base
            ligne=ligne_visee-1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0


        # sixième cas:
        # -----------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee>=2 and ligne_visee<=6:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a reculée de 1 par rapport à la colonne de base
            colonne=colonne_visee-1
            # la ligne visée a avancée de 2 par rapport à la ligne de base
            ligne=ligne_visee+2
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # septième cas:
        # ------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee>=3 and ligne_visee<=7:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a reculée de 2 par rapport à la colonne de base
            colonne=colonne_visee-2
            # la ligne visée a avancée de 1 par rapport à la ligne de base
            ligne=ligne_visee+1
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0

        # huitième cas:
        # ------------

        # si la colonne visée et la ligne visée n'est pas au-delà du bord de l'échiquier
        if colonne_visee<=7 and ligne_visee>=3:
            # initialisation de la case permettant de supprimer la pièce est fausse (c'est à dire que l'on ne peut rien attraper)
            etat_suppression=False
            # la colonne visée a avancée de 1 par rapport à la colonne de base
            colonne=colonne_visee+1
            # la ligne visée a reculée de 2 par rapport à la ligne de base
            ligne=ligne_visee-2
            # si l'"etat_suppre# alors grâce à la fonction "Noir_à_supprimer" on affecte à "x" la "valeur_piece_à_supprimer" et à "y" l'"etat_suppression"
            (x,y)=Noir_à_supprimer(colonne,ligne,valeur_piece_à_supprimer,etat_suppression)
            # si l'"etat_suppression" est vrai (donc que l'on peut attraper et supprimer la pièce adverse)
            if y==True:
                # estimation de l'efficacité offensive du nouvel emplacement de la pièce par le cumul des pièces noires atteignables
                # (avec une pondération de 50% tenant compte du fait que les noires peuvent déplacés leurs pièces nouvellement déplacées)
                retour_eval+=x/2
                # on affecte l'"etat_suppression" de la fonction "Noir_à_supprimer" vers l'"etat_suppression" de cette fonction
                etat_suppression=y
            else:
                # initialisation de la valeur de la meilleur case pour le déplacement de la pièce
                retour_eval=0
    # renvoie de la valeur de la meilleur case pour le déplacement de la pièce
    return retour_eval

# la fonction sert à exclure aux blancs les cases pouvant être menacées par les pièces noires
# on parcourt chaque case dans l'axe de mobilité de la pièce noire et pour chaque case on vérifie ou bien qu'il y a une pièce noire qui s'interpose (dans ce cas la recherhce s'arrête sur cette case)
# ou qu'il y a une pièce blanche sur cet axe dans ce cas cette pièce blanche sera attiegnable et cette case sera exclues des cases proposées pour le déplacement des blancs)
def positions_exclues_aux_blancs(liste_positions_exclues_aux_blancs,pos_blanc,pos_noir):

    # cas des fous et de la reine:
    # ---------------------------

    # de la onzième à la quinzième pièce de la liste pos_blanc et pos_noir
    for i in range(11,15):
        # la treizième pièce est exclue (car il s'agit du roi)
        if i!=13:

            # première diagonale:
            # ------------------

            # initialisation du compteur parcourant les diagonales
            p=0
            # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
            bloque_par_blanc=False
            # initialisation du booléen des cases adverses trouvées par les pièces noires comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces noires atteignables sur l'axe de mobilité de la pièce blanche)
            bloque_par_noir=False
            # tant qu'il n'y a pas de case menaçable et que la déplacement ne dépasse pas l'échiquier
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]+p==8 or pos_noir[i][1]+p==8):
                # ajout du compteur pour parcourir la diagonale
                p+=1
                # si la case de déplacement n'est pas au bord de l'échiquier
                if ((pos_noir[i][0]+p<=8) and ( pos_noir[i][1]+p<=8)):
                    # initialisation d'un autre compteur parcourant les les pièces des listes pos_blanc et pos_noir
                    q=0
                    # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
                    # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
                    bloque_par_blanc=False
                    # tant que les pièces ne sont pas parcourues ou que la pièce en question n'a pas trouvé de case adverse
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        # ajout du compteur parcourant les pièces des listes pos_blanc et pos_noir
                        q=q+1
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces noires
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+p) and (pos_noir[q][1]==pos_noir[i][1]+p))
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces blanches
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+p) and (pos_blanc[q][1]==pos_noir[i][1]+p))
                        # si le compteur a parcouru toutes les pièces ou qu'une pièce noire
                        if (q==16) or (bloque_par_blanc==True):
                            # on affecte dans la "liste_positions_exclues_aux_blancs" les cases où se trouve les pièces adverses
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+p-1][pos_noir[i][1]+p-1]=True

            # deuxième diagonale:
            # ------------------

            # initialisation du compteur parcourant les diagonales
            p=0
            # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
            bloque_par_blanc=False
            # initialisation du booléen des cases adverses trouvées par les pièces noires comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces noires atteignables sur l'axe de mobilité de la pièce blanche)
            bloque_par_noir=False
            # tant qu'il n'y a pas de case menaçable et que la déplacement ne dépasse pas l'échiquier
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]+p==8 or pos_noir[i][1]-p==1):
                # ajout du compteur pour parcourir la diagonale
                p+=1
                # si la case de déplacement n'est pas au bord de l'échiquier
                if ((pos_noir[i][0]+p<=8) and ( pos_noir[i][1]-p>=1)):
                    # initialisation d'un autre compteur parcourant les les pièces des listes pos_blanc et pos_noir
                    q=0
                    # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
                    # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
                    bloque_par_blanc=False
                    # tant que les pièces ne sont pas parcourues ou que la pièce en question n'a pas trouvé de case adverse
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        # ajout du compteur parcourant les pièces des listes pos_blanc et pos_noir
                        q=q+1
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces noires
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+p) and (pos_noir[q][1]==pos_noir[i][1]-p))
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces blanches
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+p) and (pos_blanc[q][1]==pos_noir[i][1]-p))
                        # si le compteur a parcouru toutes les pièces ou qu'une pièce noire
                        if (q==16) or (bloque_par_blanc==True):
                            # on affecte dans la "liste_positions_exclues_aux_blancs" les cases où se trouve les pièces adverses
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+p-1][pos_noir[i][1]-p-1]=True

            # troisième diagonale:
            # -------------------

            # initialisation du compteur parcourant les diagonales
            p=0
            # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
            bloque_par_blanc=False
            # initialisation du booléen des cases adverses trouvées par les pièces noires comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces noires atteignables sur l'axe de mobilité de la pièce blanche)
            bloque_par_noir=False
            # tant qu'il n'y a pas de case menaçable et que la déplacement ne dépasse pas l'échiquier
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]-p==1 or pos_noir[i][1]-p==1):
                # ajout du compteur pour parcourir la diagonale
                p+=1
                # si la case de déplacement n'est pas au bord de l'échiquier
                if ((pos_noir[i][0]-p>=1) and ( pos_noir[i][1]-p>=1)):
                    # initialisation d'un autre compteur parcourant les les pièces des listes pos_blanc et pos_noir
                    q=0
                    # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
                    # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
                    bloque_par_blanc=False
                    # tant que les pièces ne sont pas parcourues ou que la pièce en question n'a pas trouvé de case adverse
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        # ajout du compteur parcourant les pièces des listes pos_blanc et pos_noir
                        q=q+1
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces noires
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-p) and (pos_noir[q][1]==pos_noir[i][1]-p))
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces blanches
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-p) and (pos_blanc[q][1]==pos_noir[i][1]-p))
                        # si le compteur a parcouru toutes les pièces ou qu'une pièce noire
                        if (q==16) or (bloque_par_blanc==True):
                            # on affecte dans la "liste_positions_exclues_aux_blancs" les cases où se trouve les pièces adverses
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-p-1][pos_noir[i][1]-p-1]=True

            # quatrième diagonale:
            # -------------------

            # initialisation du compteur parcourant les diagonales
            p=0
            # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
            bloque_par_blanc=False
            # initialisation du booléen des cases adverses trouvées par les pièces noires comme fausse
            # (car on suppose au départ qu'il n'y a pas de pièces noires atteignables sur l'axe de mobilité de la pièce blanche)
            bloque_par_noir=False
            # tant qu'il n'y a pas de case menaçable et que la déplacement ne dépasse pas l'échiquier
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]-p==1 or pos_noir[i][1]+p==8):
                # ajout du compteur pour parcourir la diagonale
                p+=1
                # si la case de déplacement n'est pas au bord de l'échiquier
                if ((pos_noir[i][0]-p>=1) and ( pos_noir[i][1]+p<=8)):
                    # initialisation d'un autre compteur parcourant les les pièces des listes pos_blanc et pos_noir
                    q=0
                    # initialisation du booléen des cases adverses trouvées par les pièces blanches comme fausse
                    # (car on suppose au départ qu'il n'y a pas de pièces blanches atteignables sur l'axe de mobilité de la pièce noire)
                    bloque_par_blanc=False
                    # tant que les pièces ne sont pas parcourues ou que la pièce en question n'a pas trouvé de case adverse
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        # ajout du compteur parcourant les pièces des listes pos_blanc et pos_noir
                        q=q+1
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces noires
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-p) and (pos_noir[q][1]==pos_noir[i][1]+p))
                        # detection d'une autre pièce noir sur l'axe de recherche des cases atteignables par les pièces blanches
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-p) and (pos_blanc[q][1]==pos_noir[i][1]+p))
                        # si le compteur a parcouru toutes les pièces ou qu'une pièce noire
                        if (q==16) or (bloque_par_blanc==True):
                            # on affecte dans la "liste_positions_exclues_aux_blancs" les cases où se trouve les pièces adverses
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-p-1][pos_noir[i][1]+p-1]=True

    # cas des tours et de la reine:
    # ----------------------------

    # de la neuvième à la dix-septième pièce de la liste pos_blanc et pos_noir
    for i in range(9,17):
        # la dixième, la onzième, la treizième, la quatorzième et la quinzième pièce est exclue (car il s'agit des cavaliers, des fous et du roi)
        if i!=10 and i!=11 and i!=13 and i!=14 and i!=15:

            # colonne supérieure:
            # ------------------

            p=0
            bloque_par_blanc=False
            bloque_par_noir=False
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]+p==8):
                p+=1
                if (pos_noir[i][0]+p<=8):
                    q=0
                    bloque_par_blanc=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le fou noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=(pos_noir[q][0]==pos_noir[i][0]+p) and (pos_noir[q][1]==pos_noir[i][1])
                        bloque_par_blanc=(pos_blanc[q][0]==pos_noir[i][0]+p) and (pos_blanc[q][1]==pos_noir[i][1])
                        if (q==16) or (bloque_par_blanc==True):
                          #  print ('essai exclus tour 1 ',pos_noir[i][0]+p,pos_noir[i][1])
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+p-1][pos_noir[i][1]-1]=True
           #colonne inférieure
            p=0
            bloque_par_blanc=False
            bloque_par_noir=False
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][0]-p==1):
                p+=1
                if (pos_noir[i][0]-p>=1):
                    q=0
                    bloque_par_blanc=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le fou noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=(pos_noir[q][0]==pos_noir[i][0]-p) and (pos_noir[q][1]==pos_noir[i][1])
                        bloque_par_blanc=(pos_blanc[q][0]==pos_noir[i][0]-p) and (pos_blanc[q][1]==pos_noir[i][1])
                        if (q==16) or (bloque_par_blanc==True):
                        #    print ('essai exclus tour 2 ',pos_noir[i][0]-p,pos_noir[i][1])
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-p-1][pos_noir[i][1]-1]=True
           #ligne à droite
            p=0
            bloque_par_blanc=False
            bloque_par_noir=False
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][1]+p==8):
                p+=1
                if (pos_noir[i][1]+p<=8):
                    q=0
                    bloque_par_blanc=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le fou noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]) and (pos_noir[q][1]==pos_noir[i][1]+p))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]) and (pos_blanc[q][1]==pos_noir[i][1]+p))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus tour 3 ',pos_noir[i][0],pos_noir[i][1]+p)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-1][pos_noir[i][1]+p-1]=True
           #ligne à gauche
            p=0
            bloque_par_blanc=False
            bloque_par_noir=False
            while not(bloque_par_blanc==True or bloque_par_noir==True or pos_noir[i][1]-p==1):
                p+=1
                if (pos_noir[i][1]-p>=1):
                    q=0
                    bloque_par_blanc=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le fou noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]) and (pos_noir[q][1]==pos_noir[i][1]-p))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]) and (pos_blanc[q][1]==pos_noir[i][1]-p))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus tour 4 ',pos_noir[i][0],pos_noir[i][1]-p)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-1][pos_noir[i][1]-p-1]=True
    #cas des pions
    for i in range(1,9):
        if pos_noir[i][0]!=8 and pos_noir[i][1]!=1:
                q=0
                bloque_par_blanc=False
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le pion noir et doit être exclue pour les blancs
                while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                    q=q+1
                    bloque_par_noir=(pos_noir[q][0]==pos_noir[i][0]+1) and (pos_noir[q][1]==pos_noir[i][1]-1)
                    bloque_par_blanc=(pos_blanc[q][0]==pos_noir[i][0]+1) and (pos_blanc[q][1]==pos_noir[i][1]-1)
                    if (q==16) or (bloque_par_blanc==True):
                     #   print ('essai exclus pion 1 ',pos_noir[i][0]+1,pos_noir[i][1]-1)
                        liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]-1-1]=True
        if pos_noir[i][0]!=1 and pos_noir[i][1]!=1:
                q=0
                bloque_par_blanc=False
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le pion noir et doit être exclue pour les blancs
                while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                    q=q+1
                    bloque_par_noir=(pos_noir[q][0]==pos_noir[i][0]-1) and (pos_noir[q][1]==pos_noir[i][1]-1)
                    bloque_par_blanc=(pos_blanc[q][0]==pos_noir[i][0]-1) and (pos_blanc[q][1]==pos_noir[i][1]-1)
                    if (q==16) or (bloque_par_blanc==True):
                     #   print ('essai exclus pion 2 ',pos_noir[i][0]-1,pos_noir[i][1]-1)
                        liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]-1-1]=True
    #cas des cavaliers
    for i in range(10,16):
        if i!=11 and i!=12 and i!=13 and i!=14:
           #1er cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and  pos_noir[i][0]<=6 and pos_noir[i][1]<=7:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+2) and (pos_noir[q][1]==pos_noir[i][1]+1))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+2) and (pos_blanc[q][1]==pos_noir[i][1]+1))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus cavalier 1 ',pos_noir[i][0]+2,pos_noir[i][1]+1)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+2-1][pos_noir[i][1]+1-1]=True
            #2eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]<=7 and pos_noir[i][1]<=6:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+1) and (pos_noir[q][1]==pos_noir[i][1]+2))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+1) and (pos_blanc[q][1]==pos_noir[i][1]+2))
                        if (q==16) or (bloque_par_blanc==True):
                        #   print ('essai exclus cavalier 2 ',pos_noir[i][0]+1,pos_noir[i][1]+2)
                           liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]+2-1]=True
           #3eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]>=3 and pos_noir[i][1]>=2:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-2) and (pos_noir[q][1]==pos_noir[i][1]-1))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-2) and (pos_blanc[q][1]==pos_noir[i][1]-1))
                        if (q==16) or (bloque_par_blanc==True):
                         #  print ('essai exclus cavalier 3 ',pos_noir[i][0]-2,pos_noir[i][1]-1)
                           liste_positions_exclues_aux_blancs[pos_noir[i][0]-2-1][pos_noir[i][1]-1-1]=True
            #4eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]>=2 and pos_noir[i][1]>=3:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavaliernoir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-1) and (pos_noir[q][1]==pos_noir[i][1]-2))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-1) and (pos_blanc[q][1]==pos_noir[i][1]-2))
                        if (q==16) or (bloque_par_blanc==True):
                          #  print ('essai exclus cavalier 4 ',pos_noir[i][0]-1,pos_noir[i][1]-2)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]-2-1]=True
            #5eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]<=6 and pos_noir[i][1]>=2:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+2) and (pos_noir[q][1]==pos_noir[i][1]-1))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+2) and (pos_blanc[q][1]==pos_noir[i][1]-1))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus cavalier 5 ',pos_noir[i][0]+2,pos_noir[i][1]-1)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+2-1][pos_noir[i][1]-1-1]=True
            #6eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]>=2 and pos_noir[i][1]<=6:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-1) and (pos_noir[q][1]==pos_noir[i][1]+2))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-1) and (pos_blanc[q][1]==pos_noir[i][1]+2))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus cavalier 6 ',pos_noir[i][0]-1,pos_noir[i][1]+2)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]+2-1]=True
            #7eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]>=3 and pos_noir[i][1]<=7:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]-2) and (pos_noir[q][1]==pos_noir[i][1]+1))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]-2) and (pos_blanc[q][1]==pos_noir[i][1]+1))
                        if (q==16) or (bloque_par_blanc==True):
                          #  print ('essai exclus cavalier 7 ',pos_noir[i][0]-2,pos_noir[i][1]+1)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]-2-1][pos_noir[i][1]+1-1]=True
            #8eme cas
            while not(bloque_par_blanc==True or bloque_par_noir==True) and pos_noir[i][0]<=7 and pos_noir[i][1]>=3:
                    q=0
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le cavalier noir et doit être exclue pour les blancs
                    while not(q==16 or bloque_par_noir==True or bloque_par_blanc==True):
                        q=q+1
                        bloque_par_noir=((pos_noir[q][0]==pos_noir[i][0]+1) and (pos_noir[q][1]==pos_noir[i][1]-2))
                        bloque_par_blanc=((pos_blanc[q][0]==pos_noir[i][0]+1) and (pos_blanc[q][1]==pos_noir[i][1]-2))
                        if (q==16) or (bloque_par_blanc==True):
                         #   print ('essai exclus cavalier 8 ',pos_noir[i][0]+1,pos_noir[i][1]-2)
                            liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]-2-1]=True


        #cas du roi
    for i in range(13,14):

        if pos_noir[i][0]!=8 and pos_noir[i][1]!=8:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]+1) and (pos_noir[q][1]!=pos_noir[i][1]+1):
                        bloque_par_noir=True
                if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]+1-1]=True

        if pos_noir[i][1]!=8:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]) and (pos_noir[q][1]!=pos_noir[i][1]+1):
                        bloque_par_noir=True
                if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]-1][pos_noir[i][1]+1-1]=True

        if pos_noir[i][0]!=1 and pos_noir[i][1]!=8:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]-1) and (pos_noir[q][1]!=pos_noir[i][1]+1):
                        bloque_par_noir=True
                if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]+1-1]=True

        if pos_noir[i][0]!=1:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]-1) and (pos_noir[q][1]!=pos_noir[i][1]):
                        bloque_par_noir=True
                if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]-1]=True

        if pos_noir[i][0]!=1 and pos_noir[i][1]!=1:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]-1) and (pos_noir[q][1]!=pos_noir[i][1]-1):
                        bloque_par_noir=True
                    if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]-1-1][pos_noir[i][1]-1-1]=True

        if pos_noir[i][1]!=1:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]) and (pos_noir[q][1]!=pos_noir[i][1]-1):
                        bloque_par_noir=True
                    if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]-1][pos_noir[i][1]-1-1]=True

        if pos_noir[i][0]!=8 and pos_noir[i][1]!=1:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]+1) and (pos_noir[q][1]!=pos_noir[i][1]-1):
                        bloque_par_noir=True
                    if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]-1-1]=True

        if pos_noir[i][0]!=8:
                q=0
                bloque_par_noir=False
                #si on a atteint la fin de la liste des noirs et qu’aucun n’occupe cette case alors cette case est atteignable par le roi noir et doit être exclue pour les blancs
                while not(q==16) and bloque_par_noir==False:
                    q=q+1
                    if (pos_noir[q][0]!=pos_noir[i][0]+1) and (pos_noir[q][1]!=pos_noir[i][1]):
                        bloque_par_noir=True
                    if q==16: liste_positions_exclues_aux_blancs[pos_noir[i][0]+1-1][pos_noir[i][1]-1]=True

    #print('exclus aux blancs',liste_positions_exclues_aux_blancs)
    return liste_positions_exclues_aux_blancs

#fonction qui caractérise le déplacement automatique du joueur ennemi (c'est-à-dire l'IA)
def deplacement(couleur,pos_blanc,pos_noir):
    liste_positions_exclues_aux_blancs_=positions_exclues_aux_blancs(liste_positions_exclues_aux_blancs,pos_blanc,pos_noir)
    #print('bilan exclude=',liste_positions_exclues_aux_blancs_)
    #print ('extrait ',liste_positions_exclues_aux_blancs_[3][0],liste_positions_exclues_aux_blancs_[3][1],liste_positions_exclues_aux_blancs_[3][2],liste_positions_exclues_aux_blancs_[3][3],liste_positions_exclues_aux_blancs_[3][4],liste_positions_exclues_aux_blancs_[3][5],liste_positions_exclues_aux_blancs_[3][6],liste_positions_exclues_aux_blancs_[3][7])
#    positions_exclues_aux_noirs(liste_positions_exclues_aux_noirs)
    # les postions exclues pour les blancs sont celles atteignables par une pièce noire
    colonne_position_propose=0
    ligne_position_propose=0
    numero_piece=0
    eval=0

    def deplacement_possible(numero_piece,colonne_position_actuelle,ligne_position_actuelle,type,etat_piece,eval,colonne_position_propose,ligne_position_propose):
        #print(numero_piece,colonne_position_actuelle,ligne_position_actuelle,type,etat_piece,eval,colonne_position_propose,ligne_position_propose)
        max_eval=0
        def deplacement_pion(eval,colonne_position_propose,ligne_position_propose):
            max_eval=0
            if couleur=='blanc' and etat_piece!='supprime':
                print('pion ',numero_piece)
                n=1
                etat_suppression=False
                bloque_par_blanc=False
                bloque_par_noir=False
                colonne_visee=0
                ligne_visee=0
                eval=0
                eval_1=0
                eval_2=0
                eval_3=0
                retour_eval=0

                if pos_blanc[numero_piece][0]!=8 and pos_blanc[numero_piece][1]!=8:
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_1=1
                    else:
                        eval_1=0
                    colonne_visee=pos_blanc[numero_piece][0]+1
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    #if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                    p=0
                    while not(p==16) and bloque_par_blanc==False:
                        p+=1
                        if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                            bloque_par_blanc=True
                    if bloque_par_blanc==False:
                        q=0
                        pas_pris= True
                        while not(q==16) and pas_pris==True:
                            q=q+1
                            if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                eval_1+=pos_noir[q][3]
                                pas_pris=False
                            else:
                                eval_1=eval_1
                        y=evaluation_position_blanc('pion',colonne_visee,ligne_visee,retour_eval)
                        eval_1+=y

                    if eval_1 > 0 :
                        colonne_position_propose=colonne_visee
                        ligne_position_propose=ligne_visee
                        eval=eval_1


                if pos_blanc[numero_piece][0]!=1 and pos_blanc[numero_piece][1]!=8:
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_2=1
                    else:
                        eval_2=0
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    #if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                    p=0
                    while not(p==16) and bloque_par_blanc==False:
                        p+=1
                        if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                            bloque_par_blanc=True
                    if bloque_par_blanc==False:
                        q=0
                        pas_pris= True
                        while not(q==16) and pas_pris==True:
                            q=q+1
                            if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                eval_2+=pos_noir[q][3]
                                pas_pris=False
                            else:
                                eval_2=eval_2
                        y=evaluation_position_blanc('pion',colonne_visee,ligne_visee,retour_eval)
                        eval_2+=y


                    if eval_2 > eval_1 :
                        colonne_position_propose=colonne_visee
                        ligne_position_propose=ligne_visee
                        eval=eval_2


                if pos_blanc[numero_piece][1]!=8:
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_3=1
                    else:
                        eval_3=0
                    colonne_visee=pos_blanc[numero_piece][0]
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    bloque_par_blanc=False
                    bloque_par_noir=False
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False and bloque_par_noir==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True

                            if (colonne_visee==pos_noir[p][0]) and (ligne_visee==pos_noir[p][1]):
                                bloque_par_noir=True

                        if (bloque_par_blanc==True) or (bloque_par_noir==True):
                            colonne_visee=pos_blanc[numero_piece][0]
                            ligne_visee=pos_blanc[numero_piece][1]

                        else:
                            y=evaluation_position_blanc('pion',colonne_visee,ligne_visee,retour_eval)
                            eval_3+=y

                        if (eval_3 > eval_1) and (eval_3 > eval_2):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_3
                    else:
                        colonne_position_propose=pos_blanc[numero_piece][0]
                        ligne_position_propose=pos_blanc[numero_piece][1]



                if eval==0:
                    colonne_position_propose=pos_blanc[numero_piece][0]
                    ligne_position_propose=pos_blanc[numero_piece][1]


            return eval,colonne_position_propose,ligne_position_propose

        def deplacement_fou(eval,colonne_position_propose,ligne_position_propose):
            max_eval=0
            if couleur=='blanc' and etat_piece!='supprime':
                if numero_piece==11 or numero_piece==14:
                    print('fou ',numero_piece)
                else:
                    print('reine en diagonale ',numero_piece)
                #parcours de la première diagonale
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                retour_eval=0
                valeur_piece_à_supprimer=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==8 or ligne_position_actuelle==8 or colonne_visee==8 or ligne_visee==8):
                    #print('debut boucle',etat_suppression,etat_bloque,colonne_visee,ligne_visee)
                    colonne_visee=colonne_position_actuelle+n
                    ligne_visee=ligne_position_actuelle+n
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==11 or numero_piece==14:
                            eval=3
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    #print('x=',etat_bloque)
                    #print ('indice=',colonne_visee-1,ligne_visee-1)
                    #print(liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1])
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(colonne_visee==8 or ligne_visee==8):
                            y=evaluation_position_blanc('fou',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 1',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('eval de col',colonne_visee,'et lig',ligne_visee, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la deuxième diagonale
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==8 or ligne_position_actuelle==1 or colonne_visee==8 or ligne_visee==1):
                    colonne_visee=colonne_position_actuelle+n
                    ligne_visee=ligne_position_actuelle-n
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==11 or numero_piece==14:
                            eval=3
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(colonne_visee==8 or ligne_visee==1):
                            y=evaluation_position_blanc('fou',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 2',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('eval de col',colonne_visee,'et lig',ligne_visee, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la troisième diagonale
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==1 or ligne_position_actuelle==1 or colonne_visee==1 or ligne_visee==1):
                    colonne_visee=colonne_position_actuelle-n
                    ligne_visee=ligne_position_actuelle-n
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==11 or numero_piece==14:
                            eval=3
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(colonne_visee==1 or ligne_visee==1):
                            y=evaluation_position_blanc('fou',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 3',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('eval de col',colonne_visee,'et lig',ligne_visee, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la quatrième diagonale
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==1 or ligne_position_actuelle==8 or colonne_visee==1 or ligne_visee==8):
                    colonne_visee=colonne_position_actuelle-n
                    ligne_visee=ligne_position_actuelle+n
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==11 or numero_piece==14:
                            eval=3
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(colonne_visee==1 or ligne_visee==8):
                            y=evaluation_position_blanc('fou',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 4',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                    #5ème cas
                if eval==0:
                    colonne_position_propose=colonne_position_actuelle
                    ligne_position_propose=ligne_position_actuelle
                #print('eval de col',colonne_visee,'et lig',ligne_visee, '=',max_eval, 'etat bloque:',etat_bloque)
            return max_eval,colonne_position_propose,ligne_position_propose

        def deplacement_cavalier(eval,colonne_position_propose,ligne_position_propose):
            if couleur=='blanc' and etat_piece!='supprime':
                print('cavalier ',numero_piece)
            #1er cas
            bloque_par_blanc=False
            retour_eval=0
            eval_1=0
            if pos_blanc[numero_piece][0]<=6 and pos_blanc[numero_piece][1]<=7:
                colonne_visee=pos_blanc[numero_piece][0]+2
                ligne_visee=pos_blanc[numero_piece][1]+1
                if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                    eval_1=3
                else:
                    eval_1=0
                if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                    p=0
                    while not(p==16) and bloque_par_blanc==False:
                        p+=1
                        if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                            bloque_par_blanc=True
                    if bloque_par_blanc==False:
                        q=0
                        pas_pris= True
                        while not(q==16) and pas_pris==True:
                            q=q+1
                            if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                eval_1+=pos_noir[q][3]
                                pas_pris=False

                        y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                        eval_1+=y


                    if eval_1 >= 0 :
                        colonne_position_propose=colonne_visee
                        ligne_position_propose=ligne_visee
                        eval=eval_1
            #2eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_2=0
            if pos_blanc[numero_piece][0]<=7 and pos_blanc[numero_piece][1]<=6:
                    colonne_visee=pos_blanc[numero_piece][0]+1
                    ligne_visee=pos_blanc[numero_piece][1]+2
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_2=3
                    else:
                        eval_2=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris=True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_2+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_2+=y


                        if eval_2 > eval_1 :
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_2

             #3eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_3=0
            if pos_blanc[numero_piece][0]>=3 and pos_blanc[numero_piece][1]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]-2
                    ligne_visee=pos_blanc[numero_piece][1]-1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_3=3
                    else:
                        eval_3=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_3+=pos_noir[q][3]

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_3+=y


                        if (eval_3 > eval_1) and (eval_3 > eval_2) :
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_3
            #4eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_4=0
            if pos_blanc[numero_piece][0]>=2 and pos_blanc[numero_piece][1]>=3:
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]-2
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_4=3
                    else:
                        eval_4=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_4+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_4+=y


                        if (eval_4 > eval_1) and (eval_4 > eval_2) and (eval_4 > eval_3):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_4

            #5eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_5=0
            if pos_blanc[numero_piece][0]<=6 and pos_blanc[numero_piece][1]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]+2
                    ligne_visee=pos_blanc[numero_piece][1]-1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_5=3
                    else:
                        eval_5=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_5+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_5+=y


                        if (eval_5 > eval_1) and (eval_5 > eval_2) and (eval_5 > eval_3)and (eval_5 > eval_4):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_5

            #6eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_6=0
            if pos_blanc[numero_piece][0]>=2 and pos_blanc[numero_piece][1]<=6:
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]+2
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_6=3
                    else:
                        eval_6=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_6+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_6+=y


                        if (eval_6 > eval_1) and (eval_6 > eval_2) and (eval_6 > eval_3)and (eval_6 > eval_4) and (eval_6 > eval_5):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_6

            #7eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_7=0
            if pos_blanc[numero_piece][0]>=3 and pos_blanc[numero_piece][1]<=7:
                    colonne_visee=pos_blanc[numero_piece][0]-2
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_7=3
                    else:
                        eval_7=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_7+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_7+=y


                        if (eval_7 > eval_1) and (eval_7 > eval_2) and (eval_7 > eval_3)and (eval_7 > eval_4) and (eval_7 > eval_5) and (eval_7 > eval_6):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_7

            #8eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_8=0
            if pos_blanc[numero_piece][0]<=7 and pos_blanc[numero_piece][1]>=3:
                    colonne_visee=pos_blanc[numero_piece][0]+1
                    ligne_visee=pos_blanc[numero_piece][1]-2
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_8=3
                    else:
                        eval_8=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_8+=pos_noir[q][3]
                                    pas_pris=False

                            y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            eval_8+=y


                        if (eval_8>eval_1) and (eval_8>eval_2) and (eval_8>eval_3)and (eval_8>eval_4) and (eval_8>eval_5) and (eval_8>eval_6)and (eval_8>eval_7):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_8
            #9ème cas
            if eval==0:
                    colonne_position_propose=colonne_position_actuelle
                    ligne_position_propose=ligne_position_actuelle
            return eval,colonne_position_propose,ligne_position_propose

        def deplacement_tour(eval,colonne_position_propose,ligne_position_propose):
            max_eval=0
            if couleur=='blanc' and etat_piece!='supprime':
                if numero_piece==9 or numero_piece==16:
                    print('tour ',numero_piece)
                else:
                    print('reine en verticale et horizontale ',numero_piece)
                #parcours de la ligne à droite
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                retour_eval=0
                valeur_piece_à_supprimer=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==8 or colonne_visee==8):
                    #print('debut boucle',etat_suppression,etat_bloque,colonne_visee,ligne_visee)
                    colonne_visee=colonne_position_actuelle+n
                    ligne_visee=ligne_position_actuelle
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==9 or numero_piece==16:
                            eval=5
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    #print('x=',etat_bloque)
                    #print ('indice=',colonne_visee-1,ligne_visee-1)
                    #print(liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1])
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(ligne_visee==8):
                            y=evaluation_position_blanc('tour',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 1',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('tour lig droite eval de col',colonne_position_propose,'et lig',ligne_position_propose, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la colonne inférieure
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or ligne_position_actuelle==1 or ligne_visee==1):
                    colonne_visee=colonne_position_actuelle
                    ligne_visee=ligne_position_actuelle-n
                    print('vise:', colonne_visee,ligne_visee)
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==9 or numero_piece==16:
                            eval=5
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(ligne_visee==1):
                            y=evaluation_position_blanc('tour',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 2',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('tour col inf eval de col',colonne_position_propose,'et lig',ligne_position_propose, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la ligne à gauche
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or colonne_position_actuelle==1 or colonne_visee==1):
                    colonne_visee=colonne_position_actuelle-n
                    ligne_visee=ligne_position_actuelle
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==9 or numero_piece==16:
                            eval=5
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(colonne_visee==1):
                            y=evaluation_position_blanc('tour',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 3',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('tour lig gauche eval de col',colonne_position_propose,'et lig',ligne_position_propose, '=',max_eval, 'etat bloque:',etat_bloque)
                #parcours de la colonne supérieure
                n=1
                etat_suppression=False
                etat_bloque=False
                colonne_visee=0
                ligne_visee=0
                while not(etat_suppression==True or etat_bloque==True or ligne_position_actuelle==8 or ligne_visee==8):
                    colonne_visee=colonne_position_actuelle
                    ligne_visee=ligne_position_actuelle+n
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        if numero_piece==9 or numero_piece==16:
                            eval=5
                        else:
                            eval=10
                    else:
                        eval=0
                    x=Bloque_par_autre_blanc(colonne_visee,ligne_visee,etat_bloque)
                    etat_bloque=x
                    if x==False and liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        if not(ligne_visee==8):
                            y=evaluation_position_blanc('tour',colonne_visee,ligne_visee,retour_eval)
                            retour_eval=y
                            #print('sortie eval position 4',colonne_visee,ligne_visee,retour_eval)
                            eval+=y
                        (z,t)=Noir_à_supprimer(colonne_visee,ligne_visee,valeur_piece_à_supprimer,etat_suppression)
                        if t==True:
                            eval+=z
                            etat_bloque=etat_bloque or t
                        if eval>max_eval:
                            max_eval=eval
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                    n+=1
                #print('tour col supérieure : eval de col',colonne_position_propose,'et lig',ligne_position_propose, '=',max_eval, 'etat bloque:',etat_bloque)
                #5ème cas
                if eval==0:
                    colonne_position_propose=colonne_position_actuelle
                    ligne_position_propose=ligne_position_actuelle
            return max_eval,colonne_position_propose,ligne_position_propose

        #def deplacement_reine(eval,colonne_position_propose,ligne_position_propose):
            #fonction remplacée par double appel à deplacement fou et à deplacement tour
        def deplacement_roi(eval,colonne_position_propose,ligne_position_propose):
            if couleur=='blanc':
                print('roi ',numero_piece)
            #1er cas
            bloque_par_blanc=False
            retour_eval=0
            eval_1=0
            if pos_blanc[numero_piece][0]<=7 and pos_blanc[numero_piece][1]<=7:
                colonne_visee=pos_blanc[numero_piece][0]+1
                ligne_visee=pos_blanc[numero_piece][1]+1
                if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                    eval_1=99
                else:
                    eval_1=0
                if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                    p=0
                    while not(p==16) and bloque_par_blanc==False:
                        p+=1
                        if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                            bloque_par_blanc=True
                    if bloque_par_blanc==False:
                        q=0
                        pas_pris= True
                        while not(q==16) and pas_pris==True:
                            q=q+1
                            if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                eval_1+=pos_noir[q][3]
                                pas_pris=False

                        #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                        #eval_1+=y
                        # evaluation_position roi non implementee


                    if eval_1 >= 0 :
                        colonne_position_propose=colonne_visee
                        ligne_position_propose=ligne_visee
                        eval=eval_1
            #2eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_2=0
            if  pos_blanc[numero_piece][1]<=7:
                    colonne_visee=pos_blanc[numero_piece][0]
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_2=99
                    else:
                        eval_2=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris=True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_2+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_2+=y
                            # evaluation_position roi non implementee

                        if eval_2 > eval_1 :
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_2

             #3eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_3=0
            if pos_blanc[numero_piece][0]>=2 and pos_blanc[numero_piece][1]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]-1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_3=99
                    else:
                        eval_3=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_3+=pos_noir[q][3]

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_3+=y
                            # evaluation_position roi non implementee

                        if (eval_3 > eval_1) and (eval_3 > eval_2) :
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_3
            #4eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_4=0
            if pos_blanc[numero_piece][1]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]
                    ligne_visee=pos_blanc[numero_piece][1]-1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_4=99
                    else:
                        eval_4=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_4+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_4+=y
                            # evaluation_position roi non implementee

                        if (eval_4 > eval_1) and (eval_4 > eval_2) and (eval_4 > eval_3):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_4

            #5eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_5=0
            if pos_blanc[numero_piece][0]<=7 and pos_blanc[numero_piece][1]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]+1
                    ligne_visee=pos_blanc[numero_piece][1]-1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_5=99
                    else:
                        eval_5=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_5+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_5+=y
                            # evaluation_position roi non implementee

                        if (eval_5 > eval_1) and (eval_5 > eval_2) and (eval_5 > eval_3)and (eval_5 > eval_4):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_5

            #6eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_6=0
            if pos_blanc[numero_piece][0]>=2 and pos_blanc[numero_piece][1]<=7:
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]+1
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_6=99
                    else:
                        eval_6=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_6+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_6+=y
                            # evaluation_position roi non implementee

                        if (eval_6 > eval_1) and (eval_6 > eval_2) and (eval_6 > eval_3)and (eval_6 > eval_4) and (eval_6 > eval_5):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_6

            #7eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_7=0
            if pos_blanc[numero_piece][0]<=7:
                    colonne_visee=pos_blanc[numero_piece][0]+1
                    ligne_visee=pos_blanc[numero_piece][1]
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_7=99
                    else:
                        eval_7=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_7+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_7+=y
                            # evaluation_position roi non implementee

                        if (eval_7 > eval_1) and (eval_7 > eval_2) and (eval_7 > eval_3)and (eval_7 > eval_4) and (eval_7 > eval_5) and (eval_7 > eval_6):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_7

            #8eme cas
            bloque_par_blanc=False
            retour_eval=0
            eval_8=0
            if pos_blanc[numero_piece][0]>=2:
                    colonne_visee=pos_blanc[numero_piece][0]-1
                    ligne_visee=pos_blanc[numero_piece][1]
                    if liste_positions_exclues_aux_blancs_[colonne_position_actuelle-1][ligne_position_actuelle-1]==True:
                        eval_8=99
                    else:
                        eval_8=0
                    if liste_positions_exclues_aux_blancs_[colonne_visee-1][ligne_visee-1]==False:
                        p=0
                        while not(p==16) and bloque_par_blanc==False:
                            p+=1
                            if (colonne_visee==pos_blanc[p][0]) and (ligne_visee==pos_blanc[p][1]):
                                bloque_par_blanc=True
                        if bloque_par_blanc==False:
                            q=0
                            pas_pris= True
                            while not(q==16) and pas_pris==True:
                                q=q+1
                                if colonne_visee==pos_noir[q][0] and ligne_visee==pos_noir[q][1]:
                                    eval_8+=pos_noir[q][3]
                                    pas_pris=False

                            #y=evaluation_position_blanc('cavalier',colonne_visee,ligne_visee,retour_eval)
                            #eval_8+=y
                            # evaluation_position roi non implementee

                        if (eval_8>eval_1) and (eval_8>eval_2) and (eval_8>eval_3)and (eval_8>eval_4) and (eval_8>eval_5) and (eval_8>eval_6)and (eval_8>eval_7):
                            colonne_position_propose=colonne_visee
                            ligne_position_propose=ligne_visee
                            eval=eval_8
            #9ème cas
            if eval==0:
                    colonne_position_propose=colonne_position_actuelle
                    ligne_position_propose=ligne_position_actuelle
            return eval,colonne_position_propose,ligne_position_propose

        if etat_piece=='present':
            x=0
            y=0
            z=0
            x1=0
            y1=0
            z1=0
            if type=='pion':
                (x,y,z)=deplacement_pion(eval,colonne_position_propose,ligne_position_propose)
                max_eval=x
                colonne_position_propose=y
                ligne_position_propose=z

            if type=='fou':
                (x,y,z)=deplacement_fou(eval,colonne_position_propose,ligne_position_propose)
                max_eval=x
                colonne_position_propose=y
                ligne_position_propose=z
            if type=='cavalier':
                (x,y,z)=deplacement_cavalier(eval,colonne_position_propose,ligne_position_propose)
                max_eval=x
                colonne_position_propose=y
                ligne_position_propose=z
            if type=='tour':
                (x,y,z)=deplacement_tour(eval,colonne_position_propose,ligne_position_propose)
                max_eval=x
                colonne_position_propose=y
                ligne_position_propose=z
            if type=='reine':
                (x,y,z)=deplacement_tour(eval,colonne_position_propose,ligne_position_propose)
                (x1,y1,z1)=deplacement_fou(eval,colonne_position_propose,ligne_position_propose)
                if x> x1:
                    max_eval=x
                    colonne_position_propose=y
                    ligne_position_propose=z
                else:
                    max_eval=x1
                    colonne_position_propose=y1
                    ligne_position_propose=z1

            if type=='roi':
                deplacement_roi(eval,colonne_position_propose,ligne_position_propose)
        return etat_piece,max_eval,colonne_position_propose,ligne_position_propose

    print(' ')
    print('evaluation du déplacement optimal de chaque pion, tour, fou et cavalier puis de la piece au deplacement optimal parmi toutes')
    for n in range(1,17):
        colonne_position_actuelle=pos_blanc[n][0]
        ligne_position_actuelle=pos_blanc[n][1]
        type=pos_blanc[n][2]
        etat_piece=pos_blanc[n][4]
        (x,y,z,t)=deplacement_possible(n,colonne_position_actuelle,ligne_position_actuelle,type,etat_piece,eval,colonne_position_propose,ligne_position_propose)
        #print('n=',n,'val col lig ',x,y,z,t)
        pos_blanc[n][6]=y
        pos_blanc[n][7]=z
        pos_blanc[n][8]=t
        if z!=colonne_position_actuelle or t!=ligne_position_actuelle:
            if n<9:
                print('pion ',n,'deplaçable de la case colonne',colonne_position_actuelle,'et de la ligne',ligne_position_actuelle,'vers la colonne',z,'et la ligne',t)
            else:
                if n==11 or n==14:
                    print('fou deplaçable de la case colonne',colonne_position_actuelle,'et de la ligne',ligne_position_actuelle,'vers la colonne',z,'et la ligne',t)
                else:
                    if n==10 or n==15:
                        print('cavalier deplaçable de la case colonne',colonne_position_actuelle,'et de la ligne',ligne_position_actuelle,'vers la colonne',z,'et la ligne',t)
                    else:
                        if n==9 or n==16:
                            print('tour deplaçable de la case colonne',colonne_position_actuelle,'et de la ligne',ligne_position_actuelle,'vers la colonne',z,'et la ligne',t)
                        else:
                            if n==9 or n==16:
                                print('reine deplaçable de la case colonne',colonne_position_actuelle,'et de la ligne',ligne_position_actuelle,'vers la colonne',z,'et la ligne',t)

        #print('final', n, y)
    max=0
    piece_deplace=0
    for n in range(1,17):
        if pos_blanc[n][6]>=max:
            piece_deplace=n
            max=pos_blanc[n][6]
    print('La decision optimale est la suivante:')
    if piece_deplace<9:
                p=pos_blanc[piece_deplace][0]
                q=pos_blanc[piece_deplace][1]
                pos_blanc[piece_deplace][0]=pos_blanc[piece_deplace][7]
                pos_blanc[piece_deplace][1]=pos_blanc[piece_deplace][8]
                print('Pion ', piece_deplace,'deplace de la case colonne',p,'et de la ligne',q,'vers la colonne',pos_blanc[piece_deplace][0],'et la ligne',pos_blanc[piece_deplace][1])
    else:
                if piece_deplace==11 or piece_deplace==14:
                    p=pos_blanc[piece_deplace][0]
                    q=pos_blanc[piece_deplace][1]
                    pos_blanc[piece_deplace][0]=pos_blanc[piece_deplace][7]
                    pos_blanc[piece_deplace][1]=pos_blanc[piece_deplace][8]
                    print('Fou ', piece_deplace,'deplace de la colonne',p,'et de la ligne',q,'vers la colonne',pos_blanc[piece_deplace][0],'et la ligne',pos_blanc[piece_deplace][1])
                else:
                    if piece_deplace==10 or piece_deplace==15:
                        p=pos_blanc[piece_deplace][0]
                        q=pos_blanc[piece_deplace][1]
                        pos_blanc[piece_deplace][0]=pos_blanc[piece_deplace][7]
                        pos_blanc[piece_deplace][1]=pos_blanc[piece_deplace][8]
                        print('Cheval ', piece_deplace,'deplace de la colonne',p,'et de la ligne',q,'vers la colonne',pos_blanc[piece_deplace][0],'et la ligne',pos_blanc[piece_deplace][1])
                    else:
                        if piece_deplace==9 or piece_deplace==16:
                            p=pos_blanc[piece_deplace][0]
                            q=pos_blanc[piece_deplace][1]
                            pos_blanc[piece_deplace][0]=pos_blanc[piece_deplace][7]
                            pos_blanc[piece_deplace][1]=pos_blanc[piece_deplace][8]
                            print('Tour ', piece_deplace,'deplace de la colonne',p,'et de la ligne',q,'vers la colonne',pos_blanc[piece_deplace][0],'et la ligne',pos_blanc[piece_deplace][1])
                        else:
                            if piece_deplace==12:
                                p=pos_blanc[piece_deplace][0]
                                q=pos_blanc[piece_deplace][1]
                                pos_blanc[piece_deplace][0]=pos_blanc[piece_deplace][7]
                                pos_blanc[piece_deplace][1]=pos_blanc[piece_deplace][8]
                                print('Reine ', piece_deplace,'deplace de la colonne',p,'et de la ligne',q,'vers la colonne',pos_blanc[piece_deplace][0],'et la ligne',pos_blanc[piece_deplace][1])
            #print(pos_blanc[piece_deplace][0],pos_blanc[piece_deplace][1])
    for n in range(1,17):
            if pos_blanc[piece_deplace][7]==pos_noir[n][0] and pos_blanc[piece_deplace][8]==pos_noir[n][1]:
                pos_noir[n][4]='supprime'
                print('Pièce noire supprimée :',pos_noir[n][2])




pat=False
mat=False
choix=input('2 choix possibles: pour positionner les pièces une par une: tapez 1 sinon une configuration type est introduite: tapez 2')
blanc=' '
pos_blanc= acquisition_conf_pieces('blanc',choix)
noir=' '
pos_noir= acquisition_conf_pieces('noir',choix)
#while (pat==False and mat==False):
if (pat==False and mat==False):
        x=deplacement('blanc',pos_blanc,pos_noir)
#if (pat==False and mat==False):
#        x=deplacement('noir',pos_blanc,pos_noir)