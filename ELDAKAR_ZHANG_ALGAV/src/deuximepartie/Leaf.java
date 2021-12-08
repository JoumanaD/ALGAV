package deuximepartie;

public class Leaf implements Component{
    private Boolean value;
    private String luka;



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

    @Override
    public String getLuka() {
        this.luka = Boolean.toString(this.getSelf());
        return this.luka;
    }


    @Override
    public void setLuka(String str) {
        this.luka = str;
    }

    public boolean output(){
        return this.value;
    }
}
