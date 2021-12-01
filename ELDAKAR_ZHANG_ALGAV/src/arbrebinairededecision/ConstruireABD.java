package arbrebinairededecision;

import java.util.*;

public class ConstruireABD {
    public ArrayList<Boolean> T;
    public ConstruireABD (ArrayList<Boolean> T){
        this.T = T;
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
