package arbrebinairededecision;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<Boolean> tableV = new ArrayList<Boolean>();
        ArrayList<Integer> tableI = new ArrayList<Integer>();
        List list = Arrays.asList(false,true,true,false,false,true,false,false);
        tableV.addAll(list);
        ConstruireABD abdTest = new ConstruireABD(tableV);
        tableI = abdTest.transformLbooltoLint(tableV);

        abdTest.cons_arbre();
        System.out.println(abdTest.cons_arbre().toString());
    }
}
