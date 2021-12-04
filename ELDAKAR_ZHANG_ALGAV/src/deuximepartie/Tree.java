package deuximepartie;

import java.util.ArrayList;

public class Tree {

    public Component cons_arbre(ArrayList<Boolean> list){
        int size = list.size();
        return cons_arbre_sub(size,list);
    }

    private Component cons_arbre_sub(int tag,ArrayList<Boolean> list){
        int size = list.size();
        if(size < 3){

            return new Node(tag,new Leaf(list.get(0)),new Leaf(list.get(1)));

        }else{
            ArrayList<Boolean> subList1 = new ArrayList<>(list.subList(0,size/2));
            ArrayList<Boolean> subList2 = new ArrayList<>(list.subList(size/2,size));
            return new Node(tag,cons_arbre_sub(tag-1,subList1),cons_arbre_sub(tag-1,subList2));
        }

    }

    public void output(){
        if(this.leftChild == null && this.rightChild == null){
            System.out.println(this.);
        }else{
            System.out.println(this.etiquette);
            this.leftChild.output();
            this.rightChild.output();
        }
    }
}
