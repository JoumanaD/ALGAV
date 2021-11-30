/* type abr = 
  | Feuille of bool
  | Noeud of int *  abr *  abr
;;
*/
package arbrebinairededecision;

public class ABR {
    private int valeur;

    private ABR gauche, droit;

    public ABR(int valeur) {
        this.valeur = valeur;
    }

    public ABR(int valeur, ABR gauche, ABR droit) {
        this.valeur = valeur;
        setGauche(gauche);
        setDroit(droit);
    }

    public int getValeur() {
        return valeur;
    }

    public ABR getGauche() {
        return gauche;
    }

    public ABR getDroit() {
        return droit;
    }

    public boolean aGauche() {
        return gauche != null;
    }

    public boolean aDroit() {
        return gauche != null;
    }

    //representer l'abre binaire dans la console
    public String toString(){
        int h = height(this);
        int i;
        String result = "";
        for (i=1; i<=h; i++) {
            result += printGivenLevel(this, i);
        }
        return result;
    }

    //returns the number of nodes in the BinaryTree
    public int size(){
        return size(this);
    }

    public static int size(ABR tree){
        if(tree == null) return 0;
        return 1 + size(tree.getGauche()) + size(tree.getDroit());
    }

    public int height(){ return height(this);}

    public static int height(ABR tree){
        if(tree == null) return 0;
        int left = height(tree.getGauche());
        int right = height(tree.getDroit());
        return Math.max(left, right) + 1;
    }

    public String printGivenLevel (ABR root ,int level) {
        if (root == null) return "";
        String result = "";
        if (level == 1) {
            result += root.getValeur() + " ";
            return result;
        }else if (level > 1) {
            String left = printGivenLevel(root.gauche, level-1);
            String right = printGivenLevel(root.droit, level-1);
            return left + right;
        }else{
            return "";
        }
    }

 
    public void setGauche(ABR gauche) {
        this.gauche = gauche;
    }


    public void setDroit(ABR droit) {
        this.droit = droit;
    }
}
