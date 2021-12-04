package arbrebinairededecision;

import java.util.*;

import echauffement.Table;

/* type abr = 
  | Feuille of bool
  | Noeud of int *  abr *  abr
;;
*/
public class ABDecision {
    private Node racine;

    public void ajoutNoeud(int valeur, boolean estFeuille) {
      Node nouvelNoeud = new Node(valeur, estFeuille);

    }


    public ABDecision(Node noeud){
        this.racine = noeud;
    }

    private ABDecision cons_arbre(int x, int n) {
      int hauteur = Math.log(n)/Math.log(2); 
      return null;
    }

    public static void main(String[] args) {
      Table TableVerite = new Table(38, 8);
      System.out.println(TableVerite.getTableVerite());
      }
}
