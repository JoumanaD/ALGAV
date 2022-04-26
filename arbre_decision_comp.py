from echauffement import table

from graphviz import Digraph

import math
import random
import os


###############################    Partie II  Arbre de décision et compression     ###########################


'''Question 2.5'''

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

'''Question 2.6'''


def cons_abr(liste):
    taille = len(liste)
    if taille == 1:
        return ArbreBinaire(liste[0])
    mid = taille // 2
    return ArbreBinaire("x" + str(int(math.log2(taille))), cons_abr(liste[:mid]), cons_abr(liste[mid:]))


'''Question 2.7'''


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


'''Question 2.8'''


def compression(dicNoeud,Noeud):
    tree = dicNoeud.get(Noeud.get_luka())

    if(tree == None):
        dicNoeud[Noeud.get_luka()] = Noeud
        if(not isinstance(Noeud.valeur,bool)):
            Noeud.gauche = compression(dicNoeud,Noeud.gauche)
            Noeud.droit = compression(dicNoeud,Noeud.droit)
        return Noeud
    else:
        return tree


'''Question 2.9'''

listN = []


def listNoeud(Noeud):
    if Noeud.get_gauche() == None:
        listN.append([Noeud,None,None])
    if Noeud.get_gauche() != None and [Noeud, Noeud.gauche, Noeud.droit] not in listN:
        listN.append([Noeud, Noeud.gauche, Noeud.droit])
        listNoeud(Noeud.get_gauche())
        listNoeud(Noeud.get_droit())


# Créer un ficher dot
def dot(Noeud):
    listNoeud(Noeud)
    path = os. getcwd()
    f = open(path+'/arbre.dot', "a")
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


# Afficher le graph directement par python
def dot_py(Noeud):
    listNoeud(Noeud)
    #print(listN)
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
    path = os. getcwd()
    dot.view(filename="graph_test", directory=path)
    dot.render(filename='graph_test', directory=path, view=True)


##################################         Fin  Partie II         ###################################


####TEST1 cons_arb()####
'''
abd = cons_abr(table(38,8))
dot(abd)
dot_py(abd)
'''


####TEST2 luka()####
'''
abd = cons_abr(table(38,8))
luka(abd)
dot(abd)
dot_py(abd)
'''

####TEST3 compression()####
'''
abd = cons_abr(table(38,8))
luka(abd)
abd = compression({},abd)
dot(abd)
dot_py(abd)
'''


