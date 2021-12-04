package deuximepartie;

public class Leaf implements Component{
    private Boolean value;


    Leaf(Boolean v){
        this.value = v;
    }

    public boolean getSelf(){
        return this.value;
    }

    @Override
    public Component getLeft() {
        return null;
    }

    @Override
    public void setLeft(Component left) {

    }

    @Override
    public Component getRight() {
        return null;
    }

    @Override
    public void setRight(Component right) {

    }

    public boolean output(){
        return this.value;
    }
}
