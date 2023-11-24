a=[20.0, -1, -1, 18, -1, -1, -1, 18, -1]
def str_list(liste):
    res=""
    for i in liste:
        res=res+","+str(i)
    if res[0]==",":
        res=res[1:]
    return res