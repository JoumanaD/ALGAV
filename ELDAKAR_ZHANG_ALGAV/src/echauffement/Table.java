package echauffement;

import java.util.ArrayList;
import java.util.List;

public class Table {
	public Table(int x, int n) {
		Decomposition xb = new Decomposition(x);
		List<Boolean> lb = xb.getL();
		Completion tb = new Completion(lb,n);
		this.l = tb.getLC();
	}
	
	private List<Boolean> l = new ArrayList<Boolean>();

	public List<Boolean> getTableVerite(){
		return l;
	}
	
	public static void main(String[] args) {
		Table TableVerite = new Table(38, 8);
		System.out.println(TableVerite.getTableVerite());
	  }
	
}
