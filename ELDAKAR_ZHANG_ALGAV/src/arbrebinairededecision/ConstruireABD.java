package arbrebinairededecision;

import java.util.*;

public class ConstruireABD {
    public ArrayList<Boolean> T;
    public ConstruireABD (ArrayList<Boolean> T){
        this.T = T;
    }
    
    /*
    public ArrayList<Integer> transformLbooltoLint(ArrayList<Boolean> T){
        ArrayList<Integer> Tint = new ArrayList<Integer>();
        for(int i =0; i< T.size(); i++){
            if (T.get(i) == true) Tint.add(1);
            else Tint.add(0);
        }
        return Tint;

    }
    */

    public ABR<Integer> cons_arbre0 () {
        ABR<Integer> X3 = new ABR<Integer>(3);
        ABR<Integer> X2 = new ABR<Integer>(2);
        ABR<Integer> X1 = new ABR<Integer>(1);
        
        X2.setGauche(X1);
        X2.setDroit(X1);
        X3.setGauche(X2);
        X3.setDroit(X2);
    }

    public ABR cons_arbre(){
        double i = 2;
        double j = this.T.size();
        ArrayList<ABR> feuilleList = new ArrayList<>();
        ArrayList<ABR> tempNode = new ArrayList<>();
        ABR nodeRacine = null;

        int puissanceRacine = (int)(Math.log(j)/Math.log(i)) ;
        
        
        for(int index = 0; index<j;index++){
            if(this.T.get(index)==true){
                ABR feuille = new ABR(1);
                feuilleList.add(feuille);
            }else{
                ABR feuille = new ABR(0);
                feuilleList.add(feuille);
            }
        }

        int start;
        int feuilleIndex;
        for(int first = puissanceRacine-1; i >= 0; i++){
            start = 0;
            feuilleIndex = 0;
            for(int second = 0; second < Math.pow(2,first); second++){
                ABR nodeIntern = new ABR(puissanceRacine-first,feuilleList.get(start),feuilleList.get(start+1));
                feuilleList.set(feuilleIndex,nodeIntern);
                feuilleIndex = feuilleIndex + 1;
                start = start + 2;
                nodeRacine = nodeIntern;
               
            }
        }
        return nodeRacine;

    }

        
}
