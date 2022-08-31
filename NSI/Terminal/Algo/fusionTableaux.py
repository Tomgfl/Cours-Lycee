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

# tab1 <-- [8,15,46,72]
tab1 = [8,15,46,72]

# tab2 <-- [9,26,33,46]
tab2 = [9,26,33,46]

# tabFusion <-- [0, 0, 0, 0, 0, 0, 0, 0]
tabFusion = [0, 0, 0, 0, 0, 0, 0, 0]


# Boucle de construction de tabFusion: elle détermine l’un après
# l’autre les éléments du tableau résultat.
# L’indice i désigne la prochaine case à remplir dans tabFusion.
# Les indices x et y désignent le prochain élément de tab1 et tab2
# non encore recopiés.

#Pour i allant de 0 à 7 incrément 1
for i in range(8):
    
    # Si tab1 ET tab2 non pleins ET tab1[x] <= tab2[y] OU tab2 plein
    
    if x < len(tab1) and y < len(tab2) and tab1[x] <= tab2[y] or y >= len(tab2):
     
        # tabFusion[i] <-- tab1[x]
        tabFusion[i] = tab1[x]
         
        # incrémenter x + 1
        x += 1
        
        
    # si non
    else:
    
        # tabFusion[i] <-- tab2[y]
        tabFusion[i] = tab2[y]
        
        # incrémenter y + 1
        y += 1

# Afficher le résultat
print(tabFusion)


