package echauffement;

import java.util.ArrayList;

public class Table {
    public ArrayList table(int x, int n){
        ArrayList result = new ArrayList();

        Decomposition decom = new Decomposition();
        Completion com = new Completion();

        result = decom.decomposition(x);
        result = com.completion(result,n);

        return result;
    }

}
