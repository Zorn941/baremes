# baremes
A ce stade, le projet lit un fichier csv de résultats qu'il convertit en résultats qu'il ajoute au fichier initial dans un autre fichier.

Dans le fichier candidat.csv, les résultats apparaissent en mn s.
NIGEND,NAISSANCE,SEXE,AGE,STATUT,TYPE,Course,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats
156354,07/05/1965,M,58,OG,Alternatives,14mn20s,,,30,,,,2mn,

Application convertisseur_res.py convertit les résultats en s et retourne un fichier candidat_res.csv
NIGEND,NAISSANCE,SEXE,AGE,STATUT,TYPE,Course,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats
156354,07/05/1965,M,58,OG,Alternatives,860,,,30,,,,120,

Application aff_resultats.py exploite le fichier candidat_res.csv pour retourner un fichier resultats.csv.
NIGEND,NAISSANCE,SEXE,AGE,STATUT,TYPE,Course,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats,R_Course,R_Natation,R_Rameur,R_Pompes,R_Tractions,R_Medecine-ball,R_Abdominaux,R_Gainage,R_Squats
156354,07/05/1965,M,58,OG,True,860,-1,-1,30,-1,-1,-1,120,-1,20.0,-1,-1,19.5,-1,-1,-1,19.5,-1

Lorsqu'il n'y a pas de résultat à conervtir le résultat de la conversion est -1

Branch Unique : le processus est effectué en une seule passe
