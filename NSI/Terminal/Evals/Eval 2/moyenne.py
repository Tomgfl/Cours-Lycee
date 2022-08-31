# Nom du fichier : moyenne.py



# Initialisation de la variable resultats
resultats = {'Dupond':{'DS1':[15.5,4],
                       'DM1':[14.5,1],
                       'DS2':[13,4],
                       'PROJET1':[16,3],
                       'DS3':[14,4]},
             'Durand':{'DS1':[6,4],
                       'DM1':[14.5,1],
                       'DS2':[8,4],
                       'PROJET1':[9,3],
                       'IE1':[7,2],
                       'DS3':[8,4],
                       'DS4':[15,4]}}


# Declaration de la fonction moyenne
def moyenne(nom):
    
    # Si nom est dans les clefs de resultat 
    if nom in resultats.keys():

        # Recuperation des notes de l'eleve
        notes = resultats[nom]

        # Initialisation des variables
        # total_points <- 0
        total_points = 0
        # total_coefficients <- 0
        total_coefficients = 0

        # Balayage de chaque note,coefficient de l'eleve
        for valeurs in notes.values():

            # Recuperation de la note et du coefficient
            note, coefficient = valeurs

            # Ajout au total_points de la note fois son coefficient
            # total_points <- total_points + note * coefficient
            total_points = total_points + note * coefficient

            # Ajout du coefficient au total_coefficients
            # total_coefficients <- total_coefficients + coefficient
            total_coefficients = total_coefficients + coefficient

        # Renvoie le total_points / total_coefficients arrondie au dixieme
        return round(total_points/total_coefficients,1)

    # Sinon
    else:

        # Renvoie -1
        return -1

    
            
