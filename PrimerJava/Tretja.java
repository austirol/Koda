
/*
 * tj.exe
 */

public class Tretja {

    public static abstract class Predavalnica {
        private String oznaka;
        private int stMest;

        protected Predavalnica(String oznaka, int stMest) {
            this.oznaka = oznaka;
            this.stMest = stMest;
        }

        public String vrniOznako() {
            return this.oznaka;
        }

        public int vrniSteviloMest() {
            return this.stMest;
        }
		

        // popravite / dopolnite ...
        public int casCiscenja() {
			
            return stMest * 2;
        }
    }

    public static class Avditorna extends Predavalnica {

        public Avditorna(String oznaka, int stMest) {
            super(oznaka, stMest);
        }
		
		
    }

    public static class Racunalnica extends Predavalnica {
        private int stRacunalnikov;

        public Racunalnica(String oznaka, int stMest, int stRacunalnikov) {
            super(oznaka, stMest);
            this.stRacunalnikov = stRacunalnikov;
        }

        public int vrniSteviloRacunalnikov() {
            return this.stRacunalnikov;
        }
		
		@Override
		public int casCiscenja() {
			return super.casCiscenja() + this.vrniSteviloRacunalnikov() * 3;
		}
    }

    public static class Garaza extends Predavalnica {
        private int povrsina;

        public Garaza(String oznaka, int stMest, int povrsina) {
            super(oznaka, stMest);
            this.povrsina = povrsina;
        }
		
		public int vrniPovrsino() {
			return povrsina;
		}
		
		@Override
		public int casCiscenja() {
			return super.casCiscenja() + this.vrniPovrsino();
		}
    }

    public static class Stavba {
        private Predavalnica[] predavalnice;

        public Stavba(Predavalnica[] predavalnice) {
            this.predavalnice = predavalnice;
        }

        public int casCiscenja() {
            int cas = 0;
            for (Predavalnica predavalnica: this.predavalnice) {
                cas += predavalnica.casCiscenja();
            }
            return cas;
        }

        public int[] razporedi(int stStudentov, int[] ostanek) {
            // popravite / dopolnite ...
			int[] razporedi = new int[predavalnice.length];
			int stevec = 0;
			for (Predavalnica i : predavalnice) {
				if (stStudentov > 0 && stevec < predavalnice.length) {
					if (i instanceof Avditorna) {
						if (i.vrniSteviloMest() <= stStudentov) {
							razporedi[stevec] = i.vrniSteviloMest();
							stStudentov -= i.vrniSteviloMest();
						} else if (i.vrniSteviloMest() > stStudentov) {
							razporedi[stevec] = stStudentov;
							stStudentov -= stStudentov;	
						}
					}
				}
				stevec++;
			}
			
			stevec = 0;
			for (Predavalnica i : predavalnice) {
				if (stStudentov > 0 && stevec < predavalnice.length) {
					if (i instanceof Racunalnica) {
						if (i.vrniSteviloMest() <= stStudentov) {
							razporedi[stevec] = i.vrniSteviloMest();
							stStudentov -= i.vrniSteviloMest();
						} else if (i.vrniSteviloMest() > stStudentov) {
							razporedi[stevec] = stStudentov;
							stStudentov -= stStudentov;	
						}
					}
				}
				stevec++;
			}
			
			stevec=0;
			for (Predavalnica i : predavalnice) {
				if (stStudentov > 0 && stevec < predavalnice.length) {
					if (i instanceof Garaza) {
						if (i.vrniSteviloMest() <= stStudentov) {
							razporedi[stevec] = i.vrniSteviloMest();
							stStudentov -= i.vrniSteviloMest();
						} else if (i.vrniSteviloMest() > stStudentov) {
							razporedi[stevec] = stStudentov;
							stStudentov -= stStudentov;	
						}
					}
				}
				stevec++;
			}
			
			/*else if (i instanceof Racunalnica) {
						razporedi[stevec] = i.vrniSteviloMest();
						stStudentov -=  i.vrniSteviloMest();
					}else if (i instanceof Garaza) {
						razporedi[stevec] =  i.vrniSteviloMest();
						stStudentov -=  i.vrniSteviloMest();
					}*/
			
			ostanek[0] = stStudentov;
			
            return razporedi;
        }
    }

    public static void main(String[] args) {
        // koda za ro"cno testiranje (po potrebi)
    }
}
