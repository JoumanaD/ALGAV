package echauffement;

import java.util.ArrayList;

public class Test {
    public static void main(String[] args) {
        ArrayList testDecom = new ArrayList();
        ArrayList testCom = new ArrayList();
        ArrayList testTab = new ArrayList();

        Decomposition decom = new Decomposition();
        testDecom = decom.decomposition(38);

        Completion com = new Completion();
        testCom = com.completion(testDecom,8);

        Table t = new Table();
        testTab = t.table(58, 10);

        System.out.println(decom.toString(testDecom));
        System.out.println(decom.toString(testCom));
        System.out.println(decom.toString(testTab));


    }
}
