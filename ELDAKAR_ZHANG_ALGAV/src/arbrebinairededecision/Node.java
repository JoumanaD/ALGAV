package arbrebinairededecision;

public class Node {
    int valeur;
    boolean estFeuille;

    Node gauche, droit;
 
    public Node(int valeur, boolean estFeuille)
    {
        this.valeur = valeur;
        this.estFeuille = estFeuille;
        gauche = droit = null;
    }
    
}
