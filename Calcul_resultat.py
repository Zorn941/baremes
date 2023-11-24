import string
import bareme as br
# NIGEND,NAISSANCE,SEXE,AGE,STATUT,TYPE,Course,,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats
def extraction_val(chaine,position_dep):
    res=""
    i=position_dep+1
    if chaine[i]==",":
        return "",position_dep
    while (chaine[i]!="," and (i<len(chaine)-1)):
        res=res+chaine[i]
        i+=1
    return res,i

def convertir(chaine):
    minutes=""
    secondes=""
    if "mn" in chaine:
        chai=chaine.split('mn')
        minutes=int(chai[0])
        secondes=chai[1].strip('s')
        if len(secondes)!=0:
            secondes=int(secondes)
        else:
            secondes=0
    elif "s" in chaine:
        secondes=int(chaine.strip('s'))
    elif len(chaine)==0:
        return -1
    else:
        return int(chaine)
    if (minutes=="" and secondes==""):
        perf=-1 # Pas de performance
    elif minutes=="":
        perf=secondes
    else:
        perf=minutes*60+secondes
    return perf

def Exploite(candidat_epreu):
    cpt_virg=0
    candidat=""
    position_epreu=-1
    for j in candidat_epreu:
        if j==",":
            cpt_virg+=1
        candidat+=j
        position_epreu+=1
        if cpt_virg==6:
            candidat=candidat[:-1]
            break
    while position_epreu<len(candidat_epreu)-1:
        res,position_epreu=extraction_val(candidat_epreu, position_epreu)
        conv=convertir(res)
        if conv==-1:
            candidat=candidat+","
        else:
            candidat=candidat+","+str(conv)+","
        position_epreu+=1
    print("Résultat ", candidat)
    return candidat

def Convertit(source):
    f=open(source,"r")
    resultat="Conv_"+source
    g=open(resultat,"w")
    entete=f.readline()
    g.write(entete)
    for i in f:
        g.write(Exploite(i))
    f.close()
    g.close()
    return resultat

# Exploitation des resultats
# Issu du programme aff_resultats.py


def Lit_b(epreuve): # Lit la ligne du bareme
    ligne=epreuve
    i=0
    nom=""
    while ligne[i]!="=":
        nom+=ligne[i]
        i+=1
    ligne=ligne[len(nom)+1:]
    bareme=[]
    i=1
    lec=""
    b_age=[]
    while i<len(ligne)-1:
        if ligne[i]=="[":
            b_age=[]
            lec=""
        elif ligne[i]=="]":
            if b_age!=[]:
                bareme.append(b_age)
                b_age=[]
                lec=""
        elif ligne[i]==",":
            if lec!="":
                b_age.append(float(lec))
                lec=""
        else:
            lec=lec+ligne[i]
        i+=1
    return nom,bareme

def extraction_val(chaine,position_dep):
    res=""
    i=position_dep+1
    if chaine[i]==",":
        return "",position_dep
    while (chaine[i]!="," and (i<len(chaine)-1)):
        res=res+chaine[i]
        i+=1
    return res,i

def ExploiteL(ligne):
    print(ligne)
    cpt_virg=0
    candidat=""
    candidat_t=[] # Elément d'identification du candidat NIGEND, DDN, AGE, STATUT, ALTERNATIVES OUVERTES = True/False
    resultats=""
    resultats_t=[] # Résultats des épreuves -1 si vide pour distinguer du 0 
    # Exemple [860, -1, -1, 30, -1, -1, -1, 120, -1] 860s en course 30 tractions 120s de gainage
    # 0 course 
    # 1 natation
    # 2 rameur
    # 3 tractions 
    # 4 pompes 
    # 5 medecine-ball 
    # 6 abdominaux 
    # 7 gainage 
    # 8 squats 
    position_epreu=-1
    for j in ligne:
        if j==",":
            cpt_virg+=1
        candidat+=j
        position_epreu+=1
        if cpt_virg==6:
            resultats=ligne[len(candidat)-1:]
            resultats=resultats[1:]
            candidat=candidat[:-1]
            break
    i=0
    val=""
    while i<len(candidat)-1:
        if candidat[i]==",":
            candidat_t.append(val)
            val=""
        else:
            val+=candidat[i]
        i+=1
    candidat_t.append(val)
    # Recodage en binaire alternatives
    if candidat_t[5]=="Alternative":
        candidat_t[5]=True
    i=0
    val=""
    while i<len(resultats)-1:
        if resultats[i]==",":
            if val=="":
                resultats_t.append(-1) # Pas de valeur
            else:
                print(val)
                resultats_t.append(int(val))
            val=""
        else:
            val+=resultats[i]
        i+=1
    if val!="":
        resultats_t.append(int(val))
    if len(resultats_t)<10:
        resultats_t.append(-1)
    return candidat_t,resultats_t

def Validite(res_t,alter):
    ecr=False
    cmg1=False
    cmg2=False
    val=False
    if alter:
        if (res_t[0]!=-1 or res_t[1]!=-1 or res_t[2]!=-1):
            ecr=True
        if (res_t[3]!=-1 or res_t[4]!=-1 or res_t[5]!=-1):
            cmg1=True
        if (res_t[6]!=-1 or res_t[7]!=-1 or res_t[8]!=-1):
            cmg2=True
    else:
        if (res_t[0]!=-1):
            ecr=True
        if (res_t[3]!=-1 or res_t[4]!=-1):
            cmg1=True
        if (res_t[6]!=-1 or res_t[7]!=-1):
            cmg2=True
    if (ecr and cmg1 and cmg2):
        return True
    else:
        return False

def List_string(liste):
    res=""
    for i in liste:
        res=res+","+str(i)
    if res[0]==",":
        res=res[1:]
    return res

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

source="candid.csv"
source=Convertit(source)
f=open(source,"r")
# Exploite le fichier transformé ligne par ligne
entete=f.readline()
cible="RESULTATS_"+source
h=open(cible,"w")
entete=entete[:-1]
entete=entete+",R_Course,R_Natation,R_Rameur,R_Pompes,R_Tractions,R_Medecine-ball,R_Abdominaux,R_Gainage,R_Squats\n"
h.write(entete)
for i in f:
    ligne=""
    print(i)
    # Extrait les informations sur le candidat et ses résultats
    cand,res=ExploiteL(i)
    print(cand)
    print("\n",res)
    # Vérifie la validité de la ligne
    if Validite(res,cand[5]):
        # Si la ligne est valide l'écrit dans le fichier resultats.csv
        ligne=List_string(cand)+","+List_string(res)+","+List_string(Resultat(cand,res))
        h.write(ligne)
f.close()
h.close()

