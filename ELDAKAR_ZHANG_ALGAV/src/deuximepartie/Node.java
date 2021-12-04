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
    public Node cons_arbre(ArrayList<Boolean> list){
        int size = list.size();
        int tag = (int)(Math.log(size)/Math.log(2));
        return cons_arbre_sub(tag,list);
    }

    private Node cons_arbre_sub(int tag,ArrayList<Boolean> list){
        int size = list.size();
        if(size < 3){

            return new Node(tag,new Leaf(list.get(0)),new Leaf(list.get(1)));

        }else{
            ArrayList<Boolean> subList1 = new ArrayList<>(list.subList(0,size/2));
            ArrayList<Boolean> subList2 = new ArrayList<>(list.subList(size/2,size));
            return new Node(tag,cons_arbre_sub(tag-1,subList1),cons_arbre_sub(tag-1,subList2));
        }

    }

    public void output(Node n){
        if(n.leftChild instanceof Node && n.rightChild instanceof Node){
            System.out.println(n.etiquette);
            output((Node)n.leftChild);
            output((Node)n.rightChild);
        }else{
            System.out.println(n.etiquette);
            System.out.println(((Leaf) n.leftChild).output());
            System.out.println(((Leaf) n.rightChild).output());

        }



    }


    /*
    public String toString() {
        if (this.leftChild == null && this.rightChild == null) {
            return String.format("[ %d ]", this.etiquette);
        }
        return String.format("[ %d : %s, %s]", this.etiquette, this.leftChild, this.rightChild);
    }*/
/*
    public int height(Node tree){
        if(tree == null) return 0;
        int left = height(tree.getLeft());
        int right = height(tree.getDroit());
        return Math.max(left, right) + 1;
    }
    public String toString(){
        int h = height(this);
        int i;
        String result = "";
        for (i=1; i<=h; i++) {
            result += printGivenLevel(this, i);
        }
        return result;
    }
*/

}
