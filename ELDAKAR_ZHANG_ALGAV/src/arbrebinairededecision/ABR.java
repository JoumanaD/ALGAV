package arbrebinairededecision;
/* type abr =
  | Feuille of bool
  | Noeud of int *  abr *  abr
;;
*/

public class ABR<T> {
    private T valeur;
    private boolean isFeuille;
    private ABR<T> gauche, droit;

    public ABR(T valeur) {
        this.valeur = valeur;
    }

    public ABR(T valeur, ABR<T> gauche, ABR<T> droit) {
        this.valeur = valeur;
        setGauche(gauche);
        setDroit(droit);
    }

    public T getValeur() {
        return valeur;
    }

    public ABR<T> getGauche() {
        return gauche;
    }

    public ABR<T> getDroit() {
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
    public int size(ABR<T> tree){
        if(tree == null) return 0;
        return 1 + size(tree.getGauche()) + size(tree.getDroit());
    }

    public int height(ABR<T> tree){
        if(tree == null) return 0;
        int left = height(tree.getGauche());
        int right = height(tree.getDroit());
        return Math.max(left, right) + 1;
    }

    public String printGivenLevel (ABR<T> root ,int level) {
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


    public void setGauche(ABR<T> gauche) {
        this.gauche = gauche;
    }


    public void setDroit(ABR<T> droit) {
        this.droit = droit;
    }
}