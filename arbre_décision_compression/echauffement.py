def decomposition(num):
    listBi = []
    bi = format(num, "b")
    bi = str(bi)
    for i in bi:
        if i == "1":
            listBi.append(True)
        else:
            listBi.append(False)
    listBi.reverse()
    print(listBi)
    return listBi

decomposition(38)

def completion(liste,size):
    if size < len(liste):
        print(liste[0:size])
        return liste[0:size] 
    else:
        for i in range(len(liste), size):
            liste.append(False)
        #print(liste)
        return liste
    
#completion([False, True, True, False, False, True],4)
#completion([False, True, True, False, False, True],8)

def table(x,n):
    liste1 = decomposition(x)
    liste2 = completion(liste1,n)
    print(liste2)
    return liste2
    
#table(38,8)