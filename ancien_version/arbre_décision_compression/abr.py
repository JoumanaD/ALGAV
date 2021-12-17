import math 
import random

COUNT = [50]
ID = [1]
class ArbreBinaire:
   def __init__(self, valeur, gauche=None, droit=None):
      self.valeur= valeur
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
   if Noeud==None:
      return
  
   if Noeud.gauche!=None:
      luka(Noeud.gauche) 
  
   if Noeud.droit!=None:
      luka(Noeud.droit)
   
   if not isinstance(Noeud.valeur, bool):
      Noeud.valeur = str(Noeud.valeur)+"("+str(Noeud.gauche.get_valeur())+")"+"("+str(Noeud.droit.get_valeur())+")"
      #print(str(Noeud.valeur)+"("+str(Noeud.gauche.get_valeur())+")"+"("+str(Noeud.droit.get_valeur())+")")      
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

######partie pour tester###########
abd = cons_abr([False, True, True, False, False, True, False, False])
#abd.display()
#print2D(abd)
#print("\n\n\n\n\n")
arbre_luka = luka(abd)
print2D(abd)
#arbre_luka.display()
#print2D(arbre_luka)

compression(abd)
######fin des tests###########

print(tab)
print2D(abd)
