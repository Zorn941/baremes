# baremes Optimisé
A ce stade, le projet lit un fichier csv de résultats qu'il convertit le fichier en résultats en seconde puis calcule les résultats.

Dans le fichier candid.csv, les résultats apparaissent en mn s.
NIGEND,NAISSANCE,SEXE,STATUT,Course,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats
156354,07/05/1965,M,OG,14mn20s,,,30,,,,2mn,

Application Calcul_resultat.py exploite le fichier candid.csv pour retourner un fichier Conv_candid.csv avec les résultats en secondes puis un fichier RESULTATS_Conv_candid.csv avec les réusltats aux épreuves.
NIGEND,NAISSANCE,SEXE,STATUT,AGE,Alternatives,Course,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats,R_Course,R_Natation,R_Rameur,R_Pompes,R_Tractions,R_Medecine-ball,R_Abdominaux,R_Gainage,R_Squats
156354,07/05/1965,M,OG,58,True,860,-1,-1,30,-1,-1,-1,120,-1,20.0,-1,-1,19.5,-1,-1,-1,19.5,-1

Lorsqu'il n'y a pas de résultat à conervtir le résultat de la conversion est -1
