import random
import json

GESLO_NI_PRAVILNO = 'Nepravilno geslo.'


class Igra:
    ZELENA = {0}
    CRNA = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    RDECA = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34}

    def __init__(self, dobljena_stevilka=None):
        if dobljena_stevilka is None:
            dobljena_stevilka = 0
        else:
            self.dobljena_stevilka = int(dobljena_stevilka)
        self.zgodovina = []
        self.stanje_na_racunu = 0
        self.zgodovina_barv = []
        self.znesek_stave = 0
        
    
    def belezi_barve(self, dobljena_stevilka):
        if dobljena_stevilka in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34}:
            self.zgodovina_barv.append('RDECA')
        elif dobljena_stevilka in {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}:
            self.zgodovina_barv.append("CRNA")
        else:
            self.zgodovina_barv.append("ZELENA")

    
    def vrzi_kroglico(self):
        dobljena_stevilka = random.randint(0, 36)
        self.zgodovina.append(dobljena_stevilka)
        self.zgodovina_barv.append(dobljena_stevilka)
        return dobljena_stevilka

        
    def stava_na_eno_številko(self, stavljene_stevilke):
        for stava in stavljene_stevilke:
            if int(stava) <= 36 and int(stava) >= 0:
                if self.dobljena_stevilka == int(stava):
                    return 36 * float(self.znesek_stave)
                else:
                    return (-1) * float(self.znesek_stave)
        return 0
        
    def stava_na_barvo(self, stavljene_stevilke):
        for stava in stavljene_stevilke:
            if int(stava) == 70 or int(stava) == 50:
                if int(stava) == 70:
                    if int(stava) == self.dobljena_stevilka:
                        return 2 * float(self.znesek_stave)
                    else:
                        return (-1) * float(self.znesek_stave)
                else:
                    if int(stava) == self.dobljena_stevilka:
                        return 2 * float(self.znesek_stave)
                    else:
                        return (-1) * float(self.znesek_stave)               
        return 0

    def stava_na_sodo_liho(self, stavljene_stevilke):
        for stava in stavljene_stevilke:
            if int(stava) == 40 or int(stava) == 60:
                if int(stava) == 40:
                    if self.dobljena_stevilka % 2 == 0:
                        return 2 * float(self.znesek_stave)
                    else:
                        return (-1) * float(self.znesek_stave)
                else:
                    if self.dobljena_stevilka % 2 != 0:
                        return 2 * float(self.znesek_stave)
                    else:
                        return (-1) * float(self.znesek_stave)
        return 0

    def pridobi_stevilo_stav(self, stavljene_stevilke):
        stevilo_trenutnih_stav = 0
        for stava in stavljene_stevilke:
            if stava < 37 or stava >= 0 or stava == 40 or stava == 50 or stava == 60 or stava == 70:
                stevilo_trenutnih_stav += 1
                return stevilo_trenutnih_stav
        return 0
   
    def pridobi_vrednost_trenutnih_stav(self, stavljene_stevilke):
        return self.znesek_stave * self.pridobi_stevilo_stav(stavljene_stevilke)

    def rezultat_stav(self, stavljene_stevilke):
        self.vrzi_kroglico()
        return int(self.stava_na_barvo(stavljene_stevilke)) + int(self.stava_na_eno_številko(stavljene_stevilke)) + int(self.stava_na_sodo_liho(stavljene_stevilke))
        
    
    def novo_stanje(self, stavljene_stevilke):
        novo = self.rezultat_stav(stavljene_stevilke)
        self.stanje_na_racunu += novo
        return self.stanje_na_racunu
    
    def zacetno_stanje_na_racunu(self):
        return self.stanje_na_racunu
        



    
def je_dovolj_denarja(igralec, znesek_stave):
    return (igralec.stanje_na_racunu - znesek_stave) >= 0




            
                
            


   
           
    


