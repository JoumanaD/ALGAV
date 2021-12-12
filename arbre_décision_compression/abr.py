import math 
COUNT = [50]

class ArbreBinaire:
   def __init__(self, valeur, gauche=None, droit=None):
      self.valeur= valeur
      self.gauche = gauche
      self.droit = droit

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


##### Question 2.9 #######
listN=[]
listLuka=[]
def listNoeud(Noeud):

   if Noeud.get_gauche() != None :
      listInternV = [Noeud.valeur,Noeud.gauche.get_valeur(),Noeud.droit.get_valeur()]
      listN.append(listInternV)
      listNoeud(Noeud.get_gauche())
      listNoeud(Noeud.get_droit())

def listNoeudLuka(Noeud):
   if Noeud.get_gauche() != None:
      listInternL = [Noeud.valeur, Noeud.gauche.get_valeur(), Noeud.droit.get_valeur()]
      listLuka.append(listInternL)
      listNoeudLuka(Noeud.get_gauche())
      listNoeudLuka(Noeud.get_droit())

def dot(Noeud):
   listNoeud(abd)
   arbre_luka = luka(abd)
   listNoeudLuka(arbre_luka)
   index = 0
   f = open('/Users/yvo/Desktop/graph.txt', "a")
   f.write("digraph test {\n")


   for lukaV in listLuka:
      if not isinstance(lukaV[1],bool):
         f.write(lukaV[0] + "   [ label=\" " + listN[index][0] + " \"];\n")
         f.write(lukaV[1] + "   [ label=\" " + listN[index][1] + " \"];\n")
         f.write(lukaV[2] + "   [ label=\" " + listN[index][2] + " \"];\n")
         index = index +1
      else:
         f.write(lukaV[0] + "   [ label=\" " + listN[index][0] + " \"];\n")
         f.write(str(lukaV[1]) + "   [ label=\" " + str(listN[index][1]) + " \"];\n")
         f.write(str(lukaV[2]) + "   [ label=\" " + str(listN[index][2]) + " \"];\n")
         index = index + 1

   for tree in listLuka:
      if not isinstance(tree[1],bool):
         f.write(tree[0]+" -> "+tree[1]+"   [ style=dashed ];\n")
         f.write(tree[0]+" -> "+tree[2]+"   [ style=solid    ];\n")
      else:
         f.write(tree[0] + " -> " + str(tree[1]) + "   [ style=dashed  ];\n")
         f.write(tree[0] + " -> " + str(tree[2]) + "   [ style=solid  ];\n")
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
      print(root.valeur)
 
    # Process left child
      print2DUtil(root.gauche, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
   # space=[0]
   # Pass initial space count as 0
   print2DUtil(root, 0)


# Question 2.9




######partie pour tester###########
abd = cons_abr([False, True, True, False, False, True, False, False])
abd.display()
#arbre_luka = luka(abd)

dot(abd)

#arbre_luka.display()
#print2D(arbre_luka)
######fin des tests###########

