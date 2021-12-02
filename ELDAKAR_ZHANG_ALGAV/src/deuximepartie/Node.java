package deuximepartie;

import java.util.ArrayList;

public class Node implements Component{
    private int etiquette;
    private Component leftChild;
    private Component rightChild;
    private ArrayList<Component> nodes = new ArrayList<Component>();

    Node(){

    }

    Node(int s, Component left, Component right){
        this.etiquette = s;
        this.leftChild = left;
        this.rightChild = right;
    }


    @Override
    public Component getLeft() {
        return this.leftChild;
    }

    @Override
    public void setLeft(Component left) {
        this.leftChild = left;
    }

    @Override
    public Component getRight() {
        return this.rightChild;
    }

    @Override
    public void setRight(Component right) {
        this.rightChild = right;
    }
/*
    public Component cons_arbre(ArrayList<Boolean> list){
        Component tree;

        int size = list.size();
        if(size < 3){
            tree = new Node("x",new Leaf(list.get(0)),new Leaf(list.get(1)));
            return tree;

        }else{
            ArrayList<Boolean> subList1 = new ArrayList<>(list.subList(0,size/2));
            ArrayList<Boolean> subList2 = new ArrayList<>(list.subList(size/2,size));
            tree = new Node("x",cons_arbre(subList1),cons_arbre(subList2));
        }
            return tree;
    }*/
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

    public String toString() {
        if (this.leftChild == null && this.rightChild == null) {
            return String.format("[ %d ]", this.etiquette);
        }
        return String.format("[ %d : %s, %s]", this.etiquette, this.leftChild, this.rightChild);
    }


}
