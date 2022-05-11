
/*
 * tj.exe
 */

import java.util.*;

public class Druga {

    public static int stolpecZNajvecPrevladujoceZelenimi(int[][][] slika) {
        // popravite / dopolnite ...
		int indeksNajStolpca = 0;
		int stNajZel = 0;
		
		int[] podatki = new int[slika[0].length];
		
		int indeksTrenutni = 0;
		for (int[][] stolpec : slika) {
			indeksTrenutni = 0;
			for (int[] piksel : stolpec) {
				if (pikselPrevladujoceZelen(piksel)) {
					podatki[indeksTrenutni]++;
				}
				indeksTrenutni++;
			}
		}
		
		int st = 0;
		for (int i : podatki) {
			if (stNajZel < i) {
				indeksNajStolpca = st;
				stNajZel = podatki[st];
			}
			st++;
		}
		//System.out.println(Arrays.toString(podatki));
        return indeksNajStolpca;
    }
	
	public static boolean pikselPrevladujoceZelen(int[] piksel) {
		if (piksel[0] < piksel[1] && piksel[2] < piksel[1]) {
			return true;
		}
		return false;
	}

    public static void main(String[] args) {
        // koda za ro"cno testiranje (po potrebi)
    }
}
