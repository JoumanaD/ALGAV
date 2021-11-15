package echauffement;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Decomposition {
	
	public Decomposition(int x) {
		bx = Integer.toBinaryString(x);
		for(int i=0; i<bx.length();i++) {
			if (bx.charAt(i) == '1') {
				l.add(true);
			} else { 
				l.add(false);
			}
		}
		 Collections.reverse(l);
	}
	
	private String bx;
	private List<Boolean> l = new ArrayList<Boolean>();
	
	public String getBinaire() {
		return bx;
	}
	
	public ArrayList<Boolean> getL() {
		return (ArrayList<Boolean>) l;
	}
	
	
	public static void main(String[] args) {
		Decomposition deco = new Decomposition(38);
		System.out.println(deco.getBinaire());
		System.out.println(deco.getL());
	  }
}
