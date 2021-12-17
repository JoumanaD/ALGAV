
##################################    Partie I  Echauffement     ###################################


'''Question 1.2'''


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
    return listBi



'''Question 1.3'''


def completion(liste, size):
    if size < len(liste):
        return liste[0:size]
    else:
        for i in range(len(liste), size):
            liste.append(False)
        return liste



'''Question 1.4'''


def table(x, n):
    liste1 = decomposition(x)
    liste2 = completion(liste1, n)
    return liste2


##################################         Fin  Partie I         ###################################



##################################         Test  Partie I         ###################################
def test_1():
    print("decomposition(38) = "+ str(decomposition(38)))
    '''[False, True, True, False, False, True]'''
    print("completion([False, True, True, False, False, True],4) = " + str(completion([False, True, True, False, False, True],4)))
    '''[False, True, True, False]'''
    print("completion([False, True, True, False, False, True],8) = " + str(completion([False, True, True, False, False, True],8)))
    '''[False, True, True, False, False, True, False, False]'''

    print("table(38, 8) = " + str(table(38, 8)))
    '''[False, True, True, False, False, True, False, False]'''


#test_1()