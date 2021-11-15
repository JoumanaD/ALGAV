package echauffement;

import java.util.ArrayList;
import java.util.List;

public class Completion {
	public Completion(List<Boolean> l, int n) {
		int size = l.size();
		if(size>n) {
			for(int i = 0; i<n; i++) {
				this.l.add(l.get(i));
			}
		} else if(size<n) {
			this.l = l;
			for(int i = size; i<n; i++) {
				this.l.add(false);
			}
		} else {
			this.l = l; 
		} 
		
	}
	
	private List<Boolean> l = new ArrayList<Boolean>();

	public List<Boolean> getLC(){
		return l;
	}
	
	public static void main(String[] args) {
		List<Boolean> l = new ArrayList<Boolean>();
		l.add(false);
		l.add(true);
		l.add(true);
		l.add(false);
		l.add(false);
		l.add(true);
		Completion comp1 = new Completion(l,4);
		System.out.println(comp1.getLC());
		Completion comp2 = new Completion(l,8);
		System.out.println(comp2.getLC());
	  }
	
}
