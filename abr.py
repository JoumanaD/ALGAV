import math 

class ArbreBinaire:
   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_droit = None

   def insert_gauche(self, valeur):
      if self.enfant_gauche == None:
         self.enfant_gauche = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

   def insert_droit(self, valeur):
      if self.enfant_droit == None:
         self.enfant_droit = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

   def get_valeur(self):
      return self.valeur

   def get_gauche(self):
      return self.enfant_gauche

   def get_droit(self):
      return self.enfant_droit

#######fin de la classe########

######début de la construction de l'arbre binaire###########

def cons_abr(liste):
    size = len(liste)
    tag = int(math.log(size)/math.log(2))
    return cons_arbre_sub(tag, liste)

def cons_arbre_sub(tag, liste):
    size = len(liste)
    abd = ArbreBinaire(tag)
    if size < 3:
        #Node(tag,new Feuille(list.get(0)),new Feuille(list.get(1)));
        abd.insert_gauche(liste[0])
        abd.insert_droit(liste[1])
    #ArrayList<Boolean> subList1 = new ArrayList<>(list.subList(0,size/2));
    #ArrayList<Boolean> subList2 = new ArrayList<>(list.subList(size/2,size));
    #return new Node(tag,cons_arbre_sub(tag-1,subList1),cons_arbre_sub(tag-1,subList2));
    else :
        milieu = size//2
        sousListe1 = liste[:milieu]
        sousListe2 = liste[milieu:]
        abd.insert_gauche(cons_arbre_sub(tag-1, sousListe1))
        abd.insert_droit(cons_arbre_sub(tag-1, sousListe2))
    return abd

######fin de la construction de l'arbre binaire###########

def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))

abd = cons_abr([False, True, True, False, False, True, False, False])
print(affiche(abd))

racine = ArbreBinaire(3)
racine.insert_gauche(2)
racine.insert_droit(2)

un_node2g = racine.get_gauche()
un_node2g.insert_gauche(1)
un_node2g.insert_droit(1)

un_node2d = racine.get_droit()
un_node2d.insert_gauche(1)
un_node2d.insert_droit(1)

c_node = un_node2g.get_gauche()
c_node.insert_gauche(False)
c_node.insert_droit(True)

d_node = un_node2g.get_droit()
d_node.insert_gauche(True)
d_node.insert_droit(False)

e_node = un_node2d.get_gauche()
e_node.insert_gauche(False)
e_node.insert_droit(True)

f_node = un_node2d.get_droit()
f_node.insert_gauche(False)
f_node.insert_droit(False)

print(affiche(racine))