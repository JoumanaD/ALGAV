package partie2;

public class Feuille implements ABD {
    public Feuille (boolean valeur) {
        this.valeur = valeur;
    }

    private Boolean valeur;
    
    public Boolean getValeur() {
        return this.valeur;
    }

    public void setValeur(Boolean valeur) {
        this.valeur = valeur;
    }

    public String toString(){
        if (valeur = true) return "True";
        else return "False";
    }
}
