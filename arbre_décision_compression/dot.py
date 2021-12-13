import math
import random
import numpy as np
import matplotlib.pyplot as plt

from arbre_décision_compression import echauffement

COUNT = [50]


class ArbreBinaire:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        self.id = str(round(random.uniform(0,1),20))

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

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.droit is None and self.gauche is None:
            line = '%s' % self.valeur
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.droit is None:
            lines, n, p, x = self.gauche._display_aux()
            s = '%s' % self.valeur
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.gauche is None:
            lines, n, p, x = self.droit._display_aux()
            s = '%s' % self.valeur
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        gauche, n, p, x = self.gauche._display_aux()
        droit, m, q, y = self.droit._display_aux()
        s = '%s' % self.valeur
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            gauche += [n * ' '] * (q - p)
        elif q < p:
            droit += [m * ' '] * (p - q)
        zipped_lines = zip(gauche, droit)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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
        Noeud.valeur = str(Noeud.valeur) + "(" + str(Noeud.gauche.get_valeur()) + ")" + "(" + str(
            Noeud.droit.get_valeur()) + ")"
        # print(str(Noeud.valeur)+"("+str(Noeud.gauche.get_valeur())+")"+"("+str(Noeud.droit.get_valeur())+")")
    return Noeud


###### fin fonction Lukasiewicz ###########


##### Question 2.9 #######
listN = []
listid = []


def listNoeud(Noeud):
    if Noeud.get_gauche() != None:
        listIntern = [Noeud, Noeud.gauche, Noeud.droit]
        listN.append(listIntern)
        listNoeud(Noeud.get_gauche())
        listNoeud(Noeud.get_droit())


def dot(Noeud):
    listNoeud(abd)
    f = open('/Users/yvo/Desktop/final.txt', "a")
    f.write("digraph test {\n")

    for node in listN:
        
        f.write(node[0].get_id() + "   [ label=\" " + node[0].valeur + " \"];\n")
        f.write(node[1].get_id() + "   [ label=\" " + str(node[1].valeur) + " \"];\n")
        f.write(node[2].get_id() + "   [ label=\" " + str(node[2].valeur) + " \"];\n")
        f.write(node[0].get_id() + " -> " + str(node[1].get_id()) + "   [ style=dashed  ];\n")
        f.write(node[0].get_id() + " -> " + str(node[2].get_id()) + "   [ style=solid  ];\n")
    f.write("}")

    f.close()


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
    print(root.valeur)

    # Process left child
    print2DUtil(root.gauche, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


# Question 4.15
'''
def size(tree):
    if not tree:
        return 0
    return 1 + size(tree.get_gauche()) + size(tree.get_droit())

def experimentation(nbVariable):
    resultDic = {}
    tailleTable = pow(2,nbVariable)
    maxValeur = pow(2,tailleTable)-1
    for value in range(0,maxValeur):
        tree = cons_abr(echauffement.table(value, tailleTable))
        tree_robdd = robdd(tree) #transformer l'arbre en ROBDD
        nbNoeud = size(tree_robdd)
        if resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud]+1
        else:
            resultDic[nbNoeud] = 1
    return resultDic



##### Exprimentale #####
'''
#dicRes = experimentation(1)

#sorted (dicRes)

plt.plot([1,2,3,4], [1,4,9,16],'b-o')
# 指定 x 轴显示区域为 0-6，y 轴为 0-20
plt.axis([0,3.2,0,2.4])
plt.show()




######partie pour tester###########
abd = cons_abr([False, True, True, False, False, True, False, False])
abd.display()
# arbre_luka = luka(abd)
listNoeud(abd)
print(listN)
dot(abd)

# arbre_luka.display()
# print2D(arbre_luka)
######fin des tests###########

