import math 
import random

from matplotlib import pyplot as plt

from arbre_décision_compression import echauffement

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

decomposition(5895)

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
    
table(38,8)

COUNT = [50]
ID = [1]
class ArbreBinaire:
    def __init__(self, valeur, gauche=None, droit=None, lukaval=None):
        self.valeur = valeur
        self.lukaval = lukaval
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

    def get_luka(self):
        return self.lukaval
#######fin de la classe########


######début de la construction de l'arbre binaire###########
def cons_abr(liste):
   taille = len(liste)
   if taille == 1:
      return ArbreBinaire(liste[0])
   mid = taille//2
   return ArbreBinaire("x"+ str(int(math.log2(taille))), cons_abr(liste[:mid]), cons_abr(liste[mid:]))
######fin de la construction de l'arbre binaire###########


###### le mot de Lukasiewicz ###########
#on utilise un parcours postfixe pour créer l'arbre luka
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

tab=[]
tabn=[]
def rech_val(tab, val):
   for i in range(len(tab)):
      if not isinstance(val, bool):
         if tab[i][0] == val :
            return tab[i][3]
      else : 
         if tab[i][0] == val:
            return tab[i][1]

def exist_struc(tab, struc):
   for i in range(len(tab)):
      if tab[i][0] == struc :
         return True
   return False

def rech_noeud(tab, val):
   for i in range(len(tab)):
      if tab[i][1] == val :
         return tab[i][0]

def compression(Noeud):
   if Noeud==None:
      return

   if Noeud.gauche!=None :
      compression(Noeud.gauche) 
   if  Noeud.droit!=None:
      compression(Noeud.droit)

   if not isinstance(Noeud.valeur, bool) and not exist_struc(tab, Noeud.valeur): 
      ng = rech_val(tab,Noeud.gauche.valeur)
      nd = rech_val(tab,Noeud.droit.valeur)
      tab.append([Noeud.valeur, ng, nd, len(tab)])
      tabn.append([Noeud, len(tabn)])
      Noeud.gauche = rech_noeud(tabn, ng)
      Noeud.droit = rech_noeud(tabn, nd)
      
   else :
      if not exist_struc(tab, Noeud.valeur):
         tab.append([Noeud.valeur, len(tab)])
         tabn.append([Noeud, len(tabn)])
 
   return Noeud 
 

def compression_bdd(Noeud):
    if Noeud==None:
      return

    if Noeud.gauche!=None :
        compression_bdd(Noeud.gauche) 
    if  Noeud.droit!=None:
        compression_bdd(Noeud.droit)

    if not isinstance(Noeud.lukaval, bool) and not exist_struc(tab, Noeud.lukaval) and Noeud.gauche!=None and Noeud.droit!=None: 
        if Noeud.gauche.gauche != None and Noeud.gauche.gauche == Noeud.gauche.droit :
            Noeud.gauche = Noeud.gauche.gauche
        elif Noeud.droit.droit != None and Noeud.droit.gauche == Noeud.droit.droit :
            Noeud.droit = Noeud.droit.droit
        
        ng = rech_val(tab,Noeud.gauche.lukaval)
        nd = rech_val(tab,Noeud.droit.lukaval)
        tab.append([Noeud.lukaval, ng, nd, len(tab)])
        tabn.append([Noeud, len(tabn)])
        Noeud.gauche = rech_noeud(tabn, ng)
        Noeud.droit = rech_noeud(tabn, nd)
        if Noeud.gauche == Noeud.droit:
            return ArbreBinaire(Noeud.gauche.valeur, Noeud.gauche.gauche, Noeud.droit.gauche, Noeud.gauche.lukaval)
        
    else :
        if not exist_struc(tab, Noeud.valeur):
            tab.append([Noeud.lukaval, len(tab)])
            tabn.append([Noeud, len(tabn)])
    
    return Noeud

a = cons_abr([False, False])
luka(a)
compression_bdd(a)
 
##### Question 2.9 #######
listN = []

def listNoeud(Noeud):
    if Noeud.get_gauche() != None and [Noeud, Noeud.gauche, Noeud.droit] not in listN:
            listN.append([Noeud, Noeud.gauche, Noeud.droit])
            listNoeud(Noeud.get_gauche())
            listNoeud(Noeud.get_droit())


def dot(Noeud):
    listNoeud(Noeud)
    f = open('D:\M1-STL\ALGAV\dot_arbre.dot', "a")
    f.write("digraph test {\n")

    for node in listN:
        f.write(node[0].get_id() + "   [ label=\" " + node[0].valeur + " \"];\n")
        f.write(node[1].get_id() + "   [ label=\" " + str(node[1].valeur) + " \"];\n")
        f.write(node[2].get_id() + "   [ label=\" " + str(node[2].valeur) + " \"];\n")
        f.write(node[0].get_id() + " -> " + str(node[1].get_id()) + "   [ style=dashed  ];\n")
        f.write(node[0].get_id() + " -> " + str(node[2].get_id()) + "   [ style=solid  ];\n")
    f.write("}")

    f.close()
####### fin Question 2.9 #########

def print2DUtil(root, space) :
 
      # Base case
      if (root == None) :
         return

      # Increase distance between levels
      space += COUNT[0]

      # Process right child first
      print2DUtil(root.droit, space)

      # Print current node after space
      # count
      print()
      for i in range(COUNT[0], space):
         print(end = " ")
      print(root.get_id() +": " +str(root.valeur))
 
    # Process left child
      print2DUtil(root.gauche, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
   # space=[0]
   # Pass initial space count as 0
   print2DUtil(root, 0)


def printluka2DUtil(root, space) :
 
      # Base case
      if (root == None) :
         return

      # Increase distance between levels
      space += COUNT[0]

      # Process right child first
      printluka2DUtil(root.droit, space)

      # Print current node after space
      # count
      print()
      for i in range(COUNT[0], space):
         print(end = " ")
      print(root.get_id() +": " +str(root.lukaval))
 
    # Process left child
      printluka2DUtil(root.gauche, space)


# Wrapper over print2DUtil()
def printluka2D(root):
    # space=[0]
    # Pass initial space count as 0
    printluka2DUtil(root, 0)



######partie pour tester###########
#abd = cons_abr([True, True, False, True, False, True, False, False, True, False, True, False, False, True, True, False])

# arbre_luka = luka(abd)
#print2D(abd)
#luka(abd)

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

######fin des tests###########

##### Exprimentale #####


def experimentation(nbVariable):
    resultDic = {}
    tailleTable = pow(2,nbVariable)
    maxValeur = pow(2,tailleTable)-1
    for value in range(0,maxValeur+1):
        tree = cons_abr(table(value, tailleTable))
        tree_robdd = compression_bdd(tree) #transformer l'arbre en ROBDD
        nbNoeud = dot(tree_robdd)
        if nbNoeud in resultDic:#resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud]+1
        else:
            resultDic[nbNoeud] = 1
    return resultDic

def graphy_test_1(nbVariable):
    dicRes = experimentation(nbVariable)
    sorted(dicRes)
    print(dicRes)
    all_keys = dicRes.keys()
    all_values = dicRes.values()

    plt.plot(all_keys, all_values, 'b-o')
    plt.axis([0, 3.2, 0, 2.4])
    plt.show()

def graphy_test_2(nbVariable):
    dicRes = experimentation(nbVariable)
    sorted(dicRes)
    all_keys = dicRes.keys()
    all_values = dicRes.values()

    plt.plot(all_keys, all_values, 'b-o')

    plt.axis([0, 6, 0, 10])
    plt.show()



graphy_test_1(1)
graphy_test_2(2)