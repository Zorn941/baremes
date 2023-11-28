import string
import bareme as br
import sys
from datetime import date

# NIGEND,NAISSANCE,SEXE,AGE,STATUT,TYPE,Course,,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats
# Suppression age et type d'épreuves ouvertes
# NIGEND,NAISSANCE,SEXE,STATUT,Course,,Natation,Rameur,Pompes,Tractions,Medecine-ball,Abdominaux,Gainage,Squats

def Convertir(chaine):
    if "mn" in chaine:
        mn,s=chaine.split("mn")
        mn=int(mn)
        if s!="":
            s=int(s[:-1])
        else:
            s=0
    elif "s" in chaine:
        mn=0
        s=int(chaine[:-1])
    res=mn*60+s
    return res

    return perf

def Exploite(candidat_epreu): # Convertit en seconde les épreuves de temps et ajoute -1 lorsqu'il n'y a pas de résultat renvoi un string
    candidat=candidat_epreu.split(",")
    i=0
    while i<len(candidat):
        if candidat[i]=="" or candidat[i]=="\n":
            candidat[i]=-1
        i+=1
    i=4
    for i in range(4,12):
        if isinstance(candidat[i],str):
            if ("s" in candidat[i] or "mn" in candidat[i]):
                candidat[i]=Convertir(candidat[i])
            else:
                candidat[i]=int(candidat[i])
    lcandidat=""
    for i in candidat:
        lcandidat=lcandidat+str(i)+","
    lcandidat=lcandidat[:-1]
    return lcandidat

def Convertit(source):
    f=open(source,"r")
    resultat="Conv_"+source
    g=open(resultat,"w")
    entete=f.readline()
    entete=entete.split(",")
    entete.insert(4,"AGE")
    entete.insert(5,"ALTERNATIVES")
    entete=List_string(entete)
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
    candidat=[] # Elément d'identification du candidat NIGEND, DDN, SEXE, STATUT
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
    candidat=ligne.split(",")
    resultat=candidat[4:13]
    for i in range(0,9):
        resultat[i]=int(resultat[i])
    candidat=candidat[0:4]
    # Ajout de l'âge et de la possibilité des alternatives
    candidat.append(Age(candidat[1]))
    candidat.append(Alternative(candidat[4]))
    return candidat,resultat

def Age(ne):
    j,m,a=Naissance(ne)
    annee=date.today()
    annee=int(annee.strftime("%Y"))
    age=annee-a
    if (age<18 and age<70):
        print("Age invalide - personne à moins de 18 ou de plus de 70")
        return -1
    return age


def Alternative(age):
    alter=False
    if age>=40:
        alter=True
    else:
        if (can_t[4]=="OCTA" or can_t[4]=="CSTAGN"):
            alter=True
    return alter

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

def Naissance(ddn):
    # Séparation par les /
    datesplit=ddn.split('/')
    jour=int(datesplit[0])
    mois=int(datesplit[1])
    an=int(datesplit[2])
    if an<1000:
        if (an>50 and an<100):
            an=an+1900
        else:
            an=an+2000
    return jour,mois,an      

def Resultat(can_t,res_t):
    # Chargement des barèmes par sexe en 1 tableau 6 colonnes
    # Colonne 0: Notes 
    # Colonne 1: 18-29
    # Colonne 2: 30-39
    # Colonne 3: 40-49
    # Colonne 4: 50-69
    # Colonne 5: +70
    basse=int(can_t[4]/10)*10
    if basse==10 or basse==20:
        col=1
    elif basse==30:
        col=2
    elif basse==40:
        col=3
    else:
        col=4
    coef=(can_t[4]-basse)/10

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
        # Choix du bareme sexe
        if can_t[2]=="M":
            epreuve=br.squats_H
        else:
            epreuve=br.squats_F
        # Selection bareme bas 
        for i in epreuve[col]:
            if res_t[8]>=i and i!=-1:
                not_b=float(epreuve[0][epreuve[col].index(i)])
                break
            
        # Selection bareme haut
        for i in epreuve[col+1]:
            if res_t[8]>=i and i!=-1:
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
    return ret
if len(sys.argv)==1:
    source="candid.csv"
else:
    source=sys.argv[1]
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
    # Vérifie la validité de la ligne
    print(cand)
    print(res)
    if Validite(res,cand[5]):
        # Si la ligne est valide l'écrit dans le fichier RESULTAT_Conv_xxxxxx.csv
        ligne=List_string(cand)+","+List_string(res)+","+List_string(Resultat(cand,res))
        print(entete)
        print(ligne)
        h.write(ligne)
f.close()
h.close()

