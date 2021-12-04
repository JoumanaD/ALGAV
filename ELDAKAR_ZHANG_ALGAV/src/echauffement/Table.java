package echauffement;

import java.util.ArrayList;

public class Table {
    public Table() {
    }

    public ArrayList table(int x, int n) {
        new ArrayList();
        Decomposition decom = new Decomposition();
        Completion com = new Completion();
        ArrayList result = decom.decomposition(x);
        result = com.completion(result, n);
        return result;
    }
}
