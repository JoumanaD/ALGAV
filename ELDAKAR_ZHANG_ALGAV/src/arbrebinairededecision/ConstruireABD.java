package arbrebinairededecision;

import java.util.*;

public class ConstruireABD {
    public ArrayList<Boolean> T;
    public ConstruireABD (ArrayList<Boolean> T){
        this.T = T;
    }

    public ArrayList<Integer> transformLbooltoLint(ArrayList<Boolean> T){
        ArrayList<Integer> Tint = new ArrayList<Integer>();
        for(int i =0; i< T.size(); i++){
            if (T.get(i) == true) Tint.add(1);
            else Tint.add(0);
        }
        return Tint;

    }
    public ABR<Integer> cons_arbre(){
        double i = 2;
        double j = this.T.size();
        ArrayList<ABR<Integer>> feuilleList = new ArrayList<>();
        ArrayList<ABR<Integer>> tempNode = new ArrayList<>();
        ABR<Integer> nodeRacine = new ABR<Integer>(1);

        int puissanceRacine = (int)(Math.log(j)/Math.log(i)) ;


        for(int index = 0; index<j;index++){
            if(this.T.get(index)==true){
                ABR<Integer> feuille = new ABR<Integer>(1);
                feuilleList.add(feuille);
            }else{
                ABR<Integer> feuille = new ABR<Integer>(0);
                feuilleList.add(feuille);
            }
        }

        int start;
        int feuilleIndex;
        for(int first = puissanceRacine-1; i >= 0; i++){
            start = 0;
            feuilleIndex = 0;
            for(int second = 0; second < Math.pow(2,first); second++){
                ABR<Integer> nodeIntern = new ABR<Integer>(puissanceRacine-first,feuilleList.get(start),feuilleList.get(start+1));
                feuilleList.set(feuilleIndex,nodeIntern);
                feuilleIndex = feuilleIndex + 1;
                start = start + 2;
                nodeRacine = nodeIntern;
            }
        }

        return nodeRacine;

    }

}
