import math
import random
from graphviz import Digraph
from matplotlib import pyplot as plt
import time


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
    #print(listBi)
    return listBi


#decomposition(5895)


def completion(liste, size):
    if size < len(liste):
        #print(liste[0:size])
        return liste[0:size]
    else:
        for i in range(len(liste), size):
            liste.append(False)
        # print(liste)
        return liste


# completion([False, True, True, False, False, True],4)
# completion([False, True, True, False, False, True],8)

def table(x, n):
    liste1 = decomposition(x)
    liste2 = completion(liste1, n)
    #print(liste2)
    return liste2


#table(38, 8)

COUNT = [50]
ID = [1]


class ArbreBinaire:
    def __init__(self, valeur, gauche=None, droit=None, lukaval=None):
        self.valeur = valeur
        self.lukaval = lukaval
        self.gauche = gauche
        self.droit = droit
        self.id = str(round(random.uniform(0, 1), 20))

    def insert_gauche(self, valeur):
        if self.gauche == None:
            self.droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.gauche = self.gauche
            self.gauche = new_node

    def insert_droit(self, valeur):
        if self.droit == None:
            self.droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.droit = self.droit
            self.droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.gauche

    def get_droit(self):
        return self.droit

    def get_id(self):
        return self.id

    def get_luka(self):
        return self.lukaval


#######fin de la classe########


######début de la construction de l'arbre binaire###########
def cons_abr(liste):
    taille = len(liste)
    if taille == 1:
        return ArbreBinaire(liste[0])
    mid = taille // 2
    return ArbreBinaire("x" + str(int(math.log2(taille))), cons_abr(liste[:mid]), cons_abr(liste[mid:]))


######fin de la construction de l'arbre binaire###########


###### le mot de Lukasiewicz ###########
# on utilise un parcours postfixe pour créer l'arbre luka
def luka(Noeud):
    if Noeud == None:
        return

    if Noeud.gauche != None:
        luka(Noeud.gauche)

    if Noeud.droit != None:
        luka(Noeud.droit)

    if not isinstance(Noeud.valeur, bool):
        Noeud.lukaval = str(Noeud.valeur) + "(" + str(Noeud.gauche.get_luka()) + ")" + "(" + str(
            Noeud.droit.get_luka()) + ")"
        # print(str(Noeud.valeur)+"("+str(Noeud.gauche.get_valeur())+")"+"("+str(Noeud.droit.get_valeur())+")")
    else :
        Noeud.lukaval = Noeud.valeur
    return Noeud

###### fin fonction Lukasiewicz ###########

tab = []
tabn = []


def rech_val(tab, val):
    for i in range(len(tab)):
        if not isinstance(val, bool):
            if tab[i][0] == val:
                return tab[i][3]
        else:
            if tab[i][0] == val:
                return tab[i][1]


def exist_struc(tab, struc):
    for i in range(len(tab)):
        if tab[i][0] == struc:
            return True
    return False


def rech_noeud(tab, val):
    for i in range(len(tab)):
        if tab[i][1] == val:
            return tab[i][0]

def compression(dicMap,Noeud):
    tree = dicMap.get(Noeud.get_luka())

    if(tree == None):
        dicMap[Noeud.get_luka()] = Noeud
        if(not isinstance(Noeud.valeur,bool)):
            Noeud.gauche = compression(dicMap,Noeud.gauche)
            Noeud.droit = compression(dicMap,Noeud.droit)
        return Noeud
    else:
        return tree




''' old version'''
'''
def compression(Noeud):
    if Noeud == None:
        return

    if Noeud.gauche != None:
        compression(Noeud.gauche)
    if Noeud.droit != None:
        compression(Noeud.droit)

    if not isinstance(Noeud.lukaval, bool) and not exist_struc(tab, Noeud.lukaval):
        ng = rech_val(tab, Noeud.gauche.lukaval)
        nd = rech_val(tab, Noeud.droit.lukaval)
        tab.append([Noeud.lukaval, ng, nd, len(tab)])
        tabn.append([Noeud, len(tabn)])
        Noeud.gauche = rech_noeud(tabn, ng)
        Noeud.droit = rech_noeud(tabn, nd)

    else:
        if not exist_struc(tab, Noeud.valeur):
            tab.append([Noeud.lukaval, len(tab)])
            tabn.append([Noeud, len(tabn)])

    return Noeud
'''

def compression_bdd(Noeud):

    if isinstance(Noeud.lukaval,bool):
        return Noeud
    else:
        Noeud.gauche = compression_bdd(Noeud.gauche)
        Noeud.droit = compression_bdd(Noeud.droit)

        if(Noeud.gauche.get_id()==Noeud.droit.get_id()):
            return Noeud.get_droit()

        return Noeud



'''

la plus proche

    if Noeud == None:
        return

    if Noeud.gauche.gauche != None:
        if not isinstance(Noeud.gauche.gauche.lukaval, bool):
            compression_bdd(Noeud.gauche)
        if not isinstance(Noeud.droit.gauche.lukaval, bool):
            compression_bdd(Noeud.droit)

    if isinstance(Noeud.gauche.lukaval, bool):
        if Noeud.gauche.get_luka() == Noeud.droit.get_luka():
            #print(Noeud.lukaval)
            #print(Noeud.gauche.get_luka())
            #print(Noeud.droit.get_luka())
            Noeud=Noeud.gauche
            #print(Noeud.lukaval)
    else:
        if (Noeud.gauche.get_luka() == Noeud.droit.get_luka()) and Noeud.gauche.gauche.get_luka()==Noeud.gauche.droit.get_luka():
            Noeud = Noeud.gauche.gauche
        elif (Noeud.gauche.get_luka() == Noeud.droit.get_luka()) and Noeud.gauche.gauche.get_luka()!=Noeud.gauche.droit.get_luka():
            Noeud = Noeud.gauche
        else:
            if Noeud.gauche.gauche.get_luka() == Noeud.gauche.droit.get_luka():
                #print(Noeud.gauche.gauche.get_luka())
                #print(Noeud.gauche.droit.get_luka())
                Noeud.gauche = Noeud.gauche.gauche
                compression_bdd(Noeud)
            if Noeud.droit.gauche.get_luka() == Noeud.droit.droit.get_luka():
                #print(Noeud.droit.gauche.get_luka())
                #print(Noeud.droit.droit.get_luka())
                Noeud.droit = Noeud.droit.gauche

    return Noeud


ancien
    if not isinstance(Noeud.get_luka(), bool) and not isinstance(Noeud.get_gauche().get_luka(),bool):
        if Noeud.gauche.gauche.get_luka() == Noeud.gauche.droit.get_luka():
            print(Noeud.valeur)
            Noeud.gauche = Noeud.gauche.gauche
    elif not isinstance(Noeud.lukaval, bool) and not isinstance(Noeud.droit.lukaval,bool):
        if Noeud.droit.gauche.lukaval == Noeud.droit.droit.lukaval:
            Noeud.droit = Noeud.droit.gauche

    if not isinstance(Noeud.lukaval, bool) and isinstance(Noeud.gauche.lukaval,bool):
        if Noeud.gauche.lukaval == Noeud.droit.lukaval:
            print(Noeud.valeur)
            return Noeud.gauche
    elif not isinstance(Noeud.lukaval, bool) and isinstance(Noeud.droit.lukaval,bool):
        if Noeud.gauche.lukaval == Noeud.droit.lukaval:
            print(Noeud.valeur)
            return Noeud.gauche

    return Noeud



joumana
    if Noeud == None:
        return

    if Noeud.gauche != None:
        compression_bdd(Noeud.gauche)
    if Noeud.droit != None:
        compression_bdd(Noeud.droit)

    if not isinstance(Noeud.lukaval, bool) and not exist_struc(tab,
                                                               Noeud.lukaval) and Noeud.gauche != None and Noeud.droit != None:
        if Noeud.gauche.gauche != None and Noeud.gauche.gauche == Noeud.gauche.droit:
            Noeud.gauche = Noeud.gauche.gauche
        elif Noeud.droit.droit != None and Noeud.droit.gauche == Noeud.droit.droit:
            Noeud.droit = Noeud.droit.droit

        ng = rech_val(tab, Noeud.gauche.lukaval)
        nd = rech_val(tab, Noeud.droit.lukaval)
        tab.append([Noeud.lukaval, ng, nd, len(tab)])
        tabn.append([Noeud, len(tabn)])
        Noeud.gauche = rech_noeud(tabn, ng)
        Noeud.droit = rech_noeud(tabn, nd)

    else:
        if not exist_struc(tab, Noeud.valeur):
            tab.append([Noeud.lukaval, len(tab)])
            tabn.append([Noeud, len(tabn)])

    return Noeud

'''


##### Question 2.9 #######
listN = []


def listNoeud(Noeud):
    if Noeud.get_gauche() == None:
        listN.append([Noeud,None,None])
    if Noeud.get_gauche() != None and [Noeud, Noeud.gauche, Noeud.droit] not in listN:
        listN.append([Noeud, Noeud.gauche, Noeud.droit])
        listNoeud(Noeud.get_gauche())
        listNoeud(Noeud.get_droit())


def dot(Noeud):
    listNoeud(Noeud)
    f = open('/Users/yvo/Desktop/final.dot', "a")
    f.write("digraph test {\n")

    if len(listN) > 1:
        for node in listN:
            if node[1] != None:
                f.write(node[0].get_id() + "   [ label=\" " + node[0].valeur + " \"];\n")
                f.write(node[1].get_id() + "   [ label=\" " + str(node[1].valeur) + " \"];\n")
                f.write(node[2].get_id() + "   [ label=\" " + str(node[2].valeur) + " \"];\n")
                f.write(node[0].get_id() + " -> " + str(node[1].get_id()) + "   [ style=dashed  ];\n")
                f.write(node[0].get_id() + " -> " + str(node[2].get_id()) + "   [ style=solid  ];\n")
    else:
        for node in listN:
            f.write(node[0].get_id() + "   [ label=\" " + node[0].valeur + " \"];\n")
    f.write("}")

    f.close()
    #return len(listN) + 2

def dot_py(Noeud):
    listNoeud(Noeud)
    print(listN)
    dot = Digraph(name="Tree", comment="Tree graph", format="png")
    if len(listN)>1:
        for node in listN:
            if node[1] != None:
                dot.node(name=str(node[0].get_id()), label=str(node[0].valeur))
                dot.node(name=str(node[1].get_id()), label=str(node[1].valeur))
                dot.node(name=str(node[2].get_id()), label=str(node[2].valeur))
                dot.edge(str(node[0].get_id()), str(node[1].get_id()),_attributes={'style':'dotted'})
                dot.edge(str(node[0].get_id()), str(node[2].get_id()))
    else:
        for node in listN:
            dot.node(name=str(node[0].get_id()), label=str(node[0].valeur))

    print(dot.source)
    dot.view(filename="graph_test", directory="/Users/yvo/Desktop")
    dot.render(filename='graph_test', directory="/Users/yvo/Desktop", view=True)

#arbre = cons_abr(table(38,8))
#dot_py(arbre)
####### fin Question 2.9 #########

def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.droit, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.get_id() + ": " + str(root.valeur))

    # Process left child
    print2DUtil(root.gauche, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def printluka2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    printluka2DUtil(root.droit, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.get_id() + ": " + str(root.lukaval))

    # Process left child
    printluka2DUtil(root.gauche, space)


# Wrapper over print2DUtil()
def printluka2D(root):
    # space=[0]
    # Pass initial space count as 0
    printluka2DUtil(root, 0)


######partie pour tester###########
# abd = cons_abr([True, True, False, True, False, True, False, False, True, False, True, False, False, True, True, False])

# arbre_luka = luka(abd)
# print2D(abd)
# luka(abd)

'''
a = cons_abr([False, False])
luka(a)
a = compression_bdd(a, None)
print2D(a)


a = cons_abr([False, True, True, False, False, True, False, False])
luka(a)

a  = compression_bdd(a, None)
print2D(a)
print(len(tabn))
print(tab)
dot(a)

'''

#abd = cons_abr(table(38,8))
#dot(abd)
#luka(abd)
#compression(abd)
#dot(abd)
#compression_bdd(abd)
#dot(abd)
#tree = cons_abr([False,False,False,True])
#luka(tree)
#tree = compression({},tree)
#tree=compression_bdd(tree)
#print(new_tree.valeur)
#dot_py(tree)
#luka(tree)
#compression(tree)
#print2D(new_tree)


######fin des tests###########

##### Exprimentale #####
nbNode=[]
def size(tree):
    if tree == None:
        return

    if tree.id not in nbNode:
        nbNode.append(tree.id)
    size(tree.get_gauche())
    size(tree.get_droit())

'''
def experimentation(nbVariable):
    resultDic = {}
    tailleTable = pow(2, nbVariable)
    maxValeur = pow(2, tailleTable) - 1
    for value in range(0, maxValeur + 1):
        nbNode.clear()
        tree = cons_abr(table(value, tailleTable))
        print(table(value, tailleTable))
        luka(tree)
        compression(tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        print(nbNoeud)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic
    '''
#size(new_tree)
#print(len(nbNode))




tableVertie=[]

def newTest1():
    resultDic = {}
    for value in range(0, 4):
        tableVertie.append(table(value, 2))
    for i in range(0, 3):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic
def newTest2():
    resultDic = {}
    for value in range(0, 16):
        tableVertie.append(table(value, 4))
    for i in range(0, 15):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic
def newTest3():
    resultDic = {}
    for value in range(0, 256):
        tableVertie.append(table(value, 8))
    for i in range(0, 255):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic
def newTest4():
    resultDic = {}
    for value in range(0, 65536):
        tableVertie.append(table(value, 16))
    for i in range(0, 65535):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest5():
    resultDic = {}
    for simple in range(0, 500003):
        randomNum = random.randint(0,pow(2,32)-1)
        tableVertie.append(table(randomNum, 32))
    for i in range(0, 500002):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest6():
    resultDic = {}
    for simple in range(0, 400003):
        randomNum = random.randint(0,pow(2,64)-1)
        tableVertie.append(table(randomNum, 64))
    for i in range(0, 400003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest7():
    resultDic = {}
    for simple in range(0, 486892):
        randomNum = random.randint(0,pow(2,128)-1)
        tableVertie.append(table(randomNum, 128))
    for i in range(0, 486892):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest6():
    resultDic = {}
    for simple in range(0, 400003):
        randomNum = random.randint(0,pow(2,64)-1)
        tableVertie.append(table(randomNum, 64))
    for i in range(0, 400003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest6():
    resultDic = {}
    for simple in range(0, 400003):
        randomNum = random.randint(0,pow(2,64)-1)
        tableVertie.append(table(randomNum, 64))
    for i in range(0, 400003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def newTest6():
    resultDic = {}
    for simple in range(0, 400003):
        randomNum = random.randint(0,pow(2,64)-1)
        tableVertie.append(table(randomNum, 64))
    for i in range(0, 400003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def graphy_test_1():
    dicRes = newTest2()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 1 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 4, 0, 5])
    plt.show()
def graphy_test_2():
    dicRes = newTest2()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 2 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 6, 0, 10])
    plt.show()
def graphy_test_3():
    dicRes = newTest3()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 3 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 10, 0, 100])
    plt.show()

def graphy_test_4():
    dicRes = newTest4()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 4 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 12, 0, 25000])
    plt.show()

def graphy_test_5():
    dicRes = newTest5()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 8589 for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 5 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 20, 0, 2*pow(10,9)])
    plt.show()

def graphy_test_6():
    dicRes = newTest6()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 4611 * pow(10,10) for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 6 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 35, 0, 5*pow(10,18)])
    plt.show()

'''
tree = cons_abr([False, False])
luka(tree)
compression(tree)
tree = compression_bdd(tree)
size(tree)
print(len(nbNode))
dot_py(tree)
'''


#graphy_test(1)
#graphy_test(2)
#graphy_test(3)
#graphy_test(4)
#graphy_test_4(4)

#graphy_test_1()
#graphy_test_2()
#graphy_test_3()
#graphy_test_4()
#graphy_test_5()

start =time.perf_counter()
graphy_test_6()
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))
