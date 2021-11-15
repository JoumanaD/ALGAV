package echauffement;

import java.util.ArrayList;

public class Decomposition {
    ArrayList result = new ArrayList();

    public ArrayList decomposition (int a){
        String bi = Integer.toBinaryString(a);

        for(int index = bi.length()-1; index >= 0; index--){
            if(bi.charAt(index) ==  '1'){
                result.add(true);
            }else{
                result.add(false);
            }
        }
        System.out.println(bi);
        return result;
    }


    public String toString (ArrayList result){
        String print = "(";
        for(int index = 0; index < result.size(); index++){
            if(index == result.size()-1){
                if(result.get(index).equals(true)){
                    String a = "True";
                    print = print.concat(a);
                }else{
                    String a = "False";
                    print = print.concat(a);
                }
            }else{
                if(result.get(index).equals(true)){
                    String a = "True,";
                    print = print.concat(a);
                }else{
                    String a = "False,";
                    print = print.concat(a);
                }
            }
        }
        print = print +")";
        return print;
    }

}
