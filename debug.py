import bareme as br

def Arrondi(note):
    if note-int(note)==0:
        res=note
    elif note-int(note)<=0.25:
        res=int(note)
    elif (note-int(note) and note-int(note)<0.75):
        res=int(note)+0.5
    elif note-int(note)>=0.75:
        res=int(note)+1
    return res

def Resultat(can_t,res_t):
    # Chargement des barèmes par sexe en 1 tableau 6 colonnes
    # Colonne 0: Notes 
    # Colonne 1: 18-29
    # Colonne 2: 30-39
    # Colonne 3: 40-49
    # Colonne 4: 50-69
    # Colonne 5: +70

    # Gestion de l'âge
    age=int(can_t[3])
    if (age<18 and age<70):
        print("Age invalide - personne à moins de 18 ou de plus de 70")
        return -1
    basse=int(age/10)*10
    if basse==10 or basse==20:
        col=1
    elif basse==30:
        col=2
    elif basse==40:
        col=3
    else:
        col=4
    coef=(age-basse)/10
    # retour des resultats
    ret=[]
    # Calcul résultat course
    not_b=-2
    not_h=-2
    if res_t[0]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.course_H
        else:
            epreuve=br.course_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[0]<=i:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[0]<=i:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat natation
    not_b=-2
    not_h=-2
    if res_t[1]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.natation_H
        else:
            epreuve=br.natation_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[1]<=i:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[1]<=i:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat rameur
    not_b=-2
    not_h=-2
    if res_t[2]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.rameur_H
        else:
            epreuve=br.rameur_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[2]<=i:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[2]<=i:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat pompes
    not_b=-2
    not_h=-2
    if res_t[3]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.pompes_H
        else:
            epreuve=br.pompes_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[3]>=i and i!=-1:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[3]>=i and i!=-1:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat tractions
    not_b=-2
    not_h=-2
    if res_t[4]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.tractions_H
        else:
            epreuve=br.tractions_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[4]>=i and i!=-1:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[4]==i and i!=-1:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)    
    # Calcul résultat medecine-ball
    not_b=-2
    not_h=-2
    if res_t[5]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.medecine_ball_H
        else:
            epreuve=br.medecine_ball_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[5]>=i and i!=-1:
                    not_b=float(epreuve[0][epreuve[col].index(i)])
                    break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[5]>=i and i!=-1:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat abdominaux
    not_b=-2
    not_h=-2
    if res_t[6]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.abdominaux_H
        else:
            epreuve=br.abdominaux_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[6]>=i and i!=-1:
                not_b=float(epreuve[0][epreuve[col].index(i)])
                break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[6]>=i and i!=-1:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat gainage
    not_b=-2
    not_h=-2
    if res_t[7]!=-1:
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.gainage_H
        else:
            epreuve=br.gainage_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[7]>=i:
                not_b=float(epreuve[0][epreuve[col].index(i)])
                break
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[7]>=i:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    # Calcul résultat squats
    not_b=-2
    not_h=-2
    if res_t[8]!=-1:
        print(res_t[8])
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.squats_H
        else:
            epreuve=br.squats_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[8]>=i and i!=-1:
                not_b=float(epreuve[0][epreuve[col].index(i)])
                print(not_b)
                break
            
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[8]>=i and i!=-1:
                not_h=float(epreuve[0][epreuve[col+1].index(i)])
                print(not_h)
                break
        if not_b==-2:
            if not_h==-2:
                not_b=0
                not_h=0
            else:
                not_b=5
        note=Arrondi((not_h-not_b)*coef+not_b)
        ret.append(note)
    else:
        ret.append(-1)
    return ret
cand=['176454', '07/05/1975', 'M', '48', 'OG', True]
res=[860, 700, 910, 15 , 4 , 7.75, 12, 92, 25]
print(cand)
print(res)
print(Resultat(cand, res))