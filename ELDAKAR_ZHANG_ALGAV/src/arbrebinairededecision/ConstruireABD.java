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
    
    public ABR cons_arbre(){
        ArrayList<Integer> Ta = transformLbooltoLint(this.T);
        for()

    }
}
