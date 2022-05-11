
/*
 * tj.exe Prva.java . .
 */

import java.util.*;

public class Prva {

    public static void main(String[] args) {
        // dopolnite ...
		Scanner sc = new Scanner(System.in);
		
		int solataNaBranjevko = sc.nextInt();
		int kupci = sc.nextInt();
		
		int trenutniIndeks = 1;
		int stevec = solataNaBranjevko;
		for (int i = 0; i < kupci; i++) {
			int zahteva = sc.nextInt();
			if (stevec - zahteva < 0) {
				trenutniIndeks++;
				stevec = solataNaBranjevko;
			}
			if (stevec - zahteva >= 0) {
				stevec -= zahteva;
			}
			
		}
		
		System.out.println(trenutniIndeks);
    }
}
