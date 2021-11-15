package echauffement;

import java.util.ArrayList;

public class Completion {

    //ArrayList result = new ArrayList();

    public ArrayList completion(ArrayList list, int n){
        ArrayList temp = new ArrayList();

        if(list.size() <= n){
            int index = list.size();
            temp.addAll(list);

            while(index < n){
                temp.add(false);
                index++;
            }
            return temp;
        }else{
            for(int index = 0; index < n; index++){
                temp.add(list.get(index));
            }
            return temp;
        }
    }


}
