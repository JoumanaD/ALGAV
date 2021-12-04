package partie2;

public class Noeud implements ABD {
    private int valeur;
    private Noeud gauche;
    private Noeud droit;

    public Noeud(int valeur, Noeud gauche, Noeud droit){
        this.valeur = valeur;
        this.droit = droit;
        this.gauche = gauche;
    }

    public int getValeur() {
        return this.valeur;
    }

    public void setValeur(int valeur) {
        this.valeur = valeur;
    }

    public Noeud getGauche() {
        return this.gauche;
    }

    public void setGauche(Noeud gauche) {
        this.gauche = gauche;
    }

    public Noeud getDroit() {
        return this.droit;
    }

    public void setDroit(Noeud droit) {
        this.droit = droit;
    }

}
