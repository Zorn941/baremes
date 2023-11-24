import string
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
        print(chaine)
        return int(chaine)
    if (minutes=="" and secondes==""):
        perf=-1 # Pas de performance
    elif minutes=="":
        perf=secondes
    else:
        perf=minutes*60+secondes
    print("mn ",minutes)
    print("sec ",secondes)
    print("perf ",perf)
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
    print(position_epreu)
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


f=open("candidat.csv","r")
g=open("candidat_sec.csv","w")
entete=f.readline()
g.write(entete)
for i in f:
    g.write(Exploite(i))
f.close()
g.close()

    
    
