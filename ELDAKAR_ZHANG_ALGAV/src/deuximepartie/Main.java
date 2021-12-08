package deuximepartie;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<Boolean> tableV = new ArrayList<Boolean>();
        ArrayList<Integer> tableI = new ArrayList<Integer>();
        List list = Arrays.asList(false,true,true,false,false,true,false,false);
        tableV.addAll(list);
        Node abdTest = new Node();
        Node test = abdTest.cons_arbre(tableV);
        System.out.println(tableV);
        abdTest.output(test);
        //abdTest.preOrderTraverse1(test);
        abdTest.affiche((Node)test.getLeft());
        //tableI = abdTest.transformLbooltoLint(tableV);

        //abdTest.cons_arbre();
        //System.out.println(abdTest.cons_arbre().toString());
    }
}
