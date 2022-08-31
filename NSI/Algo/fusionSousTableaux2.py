# coding utf-8
# nom : fusionTableaux_algo.py
# rôle : fusionne deux tableaux tab1 et tab2 triés de 4 éléments
# résultat : un tableau tabFusion de 8 éléments

# Constantes et Variables
# tab1, tab2, tabFusion : tableaux de dimension 1
# x, y : entiers

# Initialisations
# indice de tab1 x <-- 0
x = 0

# indice de tab2 y <-- 0
y = 0

# indice de tabFusion i <-- 0
i = 0

# tab <-- [8,15,46,72,9,26,33,46]
tab = [8,15,46,72,9,26,33,46]

# tabFusion <-- [0, 0, 0, 0, 0, 0, 0, 0]
tabFusion = [0, 0, 0, 0, 0, 0, 0, 0]

# Boucle de construction de tabFusion: elle détermine l’un après
# l’autre les éléments du tableau résultat.
# L’indice i désigne la prochaine case à remplir dans tabFusion.
# Les indices x et y désignent le prochain élément de tab1 et tab2
# non encore recopiés.

#Pour i allant de 0 à 7 incrément 1
for i in range(8):
    
    # Si tab[0:4] ET tab[4:] non pleins ET tab[0:4][x] <= tab[4:][y] OU tab[4:] plein
    
    if x < len(tab[0:4]) and y < len(tab[4:]) and tab[0:4][x] <= tab[4:][y] or y >= len(tab[4:]):
     
        # tabFusion[i] <-- tab[0:4][x]
        tabFusion[i] = tab[0:4][x]
         
        # incrémenter x + 1
        x += 1
        
        
    # si non
    else:
    
        # tabFusion[i] <-- tab[4:][y]
        tabFusion[i] = tab[4:][y]
        
        # incrémenter y + 1
        y += 1

        

# Afficher le résultat
print(tabFusion)
