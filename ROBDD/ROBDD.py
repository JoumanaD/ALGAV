import math
import random

COUNT = [50]


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

###### debut fonction compression #########

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

   if not isinstance(Noeud.lukaval, bool) and not exist_struc(tab, Noeud.lukaval): 
      ng = rech_val(tab,Noeud.gauche.lukaval)
      nd = rech_val(tab,Noeud.droit.lukaval)
      tab.append([Noeud.lukaval, ng, nd, len(tab)])
      tabn.append([Noeud, len(tabn)])
      Noeud.gauche = rech_noeud(tabn, ng)
      Noeud.droit = rech_noeud(tabn, nd)
      
   else :
      if not exist_struc(tab, Noeud.valeur):
         tab.append([Noeud.lukaval, len(tab)])
         tabn.append([Noeud, len(tabn)])
 
   return Noeud 
####### fin fonction compression #########

def compression_bdd(Noeud):
    if Noeud==None:
      return

    if Noeud.gauche!=None :
        compression_bdd(Noeud.gauche) 
    if  Noeud.droit!=None:
        compression_bdd(Noeud.droit)

    if not isinstance(Noeud.lukaval, bool) and not exist_struc(tab, Noeud.lukaval): 
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
        
    else :
        if not exist_struc(tab, Noeud.valeur):
            tab.append([Noeud.lukaval, len(tab)])
            tabn.append([Noeud, len(tabn)])
    
    return Noeud
##### Question 2.9 #######
listN = []

def listNoeud(Noeud):
    if Noeud.get_gauche() != None and [Noeud, Noeud.gauche, Noeud.droit] not in listN:
            listN.append([Noeud, Noeud.gauche, Noeud.droit])
            listNoeud(Noeud.get_gauche())
            listNoeud(Noeud.get_droit())


def dot(Noeud):
    listNoeud(Noeud)
    f = open('/home/joumana/STL/ALGAV/arbre_décision_compression/dot_arbre.dot', "a")
    f.write("digraph test {\n")

    for node in listN:
        f.write(node[0].get_id() + "   [ label=\" " + node[0].valeur + " \"];\n")
        f.write(node[1].get_id() + "   [ label=\" " + str(node[1].valeur) + " \"];\n")
        f.write(node[2].get_id() + "   [ label=\" " + str(node[2].valeur) + " \"];\n")
        f.write(node[0].get_id() + " -> " + str(node[1].get_id()) + "   [ style=dashed  ];\n")
        f.write(node[0].get_id() + " -> " + str(node[2].get_id()) + "   [ style=solid  ];\n")
    f.write("}")

    f.close()


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
def print2D(root):
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
abd = cons_abr([False, True, True, False, False, True, False, False])

# arbre_luka = luka(abd)
#print2D(abd)
luka(abd)
'''
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print2D(abd)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
printluka2D(abd)
'''
compression_bdd(abd)
'''
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print2D(abd)
'''
dot(abd)
######fin des tests###########
