package arbrebinairededecision;

public class Node {
    int value;
    Node left;
    Node right;

    Node(int value) {
        this.value = value;
        right = null;
        left = null;
    }

    Node(int value,Node leftNode, Node rightNode){
        this.value = value;
        this.left = leftNode;
        this.right = rightNode;
    }
}