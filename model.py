import random
import json

class Igra:
    

    def __init__(self, znesek_stave):
        self.zgodovina = []
        self.znesek_stave = float(znesek_stave)


    def poslji_stave(self, stavljene_stevilke):
        dobljena_stevilka = random.randint(0, 36)
        self.zgodovina.append(dobljena_stevilka)
        return self.rezultat_stav(stavljene_stevilke)
        
        
    def stava_na_eno_številko(self, stavljene_stevilke):
        dobicek = 0
        znesek_stave = self.znesek_stave
        for stava in stavljene_stevilke:
            if int(stava) <= 36 and int(stava) >= 0:
                if int(self.zgodovina[-1]) == int(stava):
                    dobicek += 36 * float(znesek_stave)
                else:
                    dobicek += (-1) * float(znesek_stave)
        return dobicek
    
    def stava_na_polovicko(self, stavljene_stevilke):
        znesek_stave = self.znesek_stave
        dobicek = 0
        for stava in stavljene_stevilke:
            if int(stava) == 41 or int(stava) == 42:
                if int(stava) == 41:
                    if int(self.zgodovina[-1]) in range(1, 19):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                else:
                    if int(self.zgodovina[-1]) in range(19, 37):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)

        return dobicek

        
    def stava_na_barvo(self, stavljene_stevilke):
        znesek_stave = self.znesek_stave
        dobicek = 0
        for stava in stavljene_stevilke:
            if int(stava) == 70 or int(stava) == 50:
                if int(stava) == 70:
                    if int(self.zgodovina[-1]) in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34}:
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                else:
                    if self.zgodovina[-1] in {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}:
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)               
        return dobicek

    def stava_na_sodo_liho(self, stavljene_stevilke):
        znesek_stave = self.znesek_stave
        dobicek = 0
        for stava in stavljene_stevilke:
            if int(stava) == 40 or int(stava) == 60:
                if int(stava) == 40:
                    if int(self.zgodovina[-1]) % 2 == 0:
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                else:
                    if int(self.zgodovina[-1]) % 2 != 0:
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
        return dobicek

    def stava_na_ducat(self, stavljene_stevilke):
        znesek_stave = self.znesek_stave
        dobicek = 0
        for stava in stavljene_stevilke:
            if int(stava) == 43 or int(stava) == 44 or int(stava) == 45:
                if int(stava) == 43:
                    if int(self.zgodovina[-1]) in range(1, 13):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                elif int(stava) == 44:
                    if int(self.zgodovina[-1]) in range(13, 25):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                else:
                    if int(self.zgodovina[-1]) in range(25, 37):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
        return dobicek

    def stava_na_vrstico(self, stavljene_stevilke):
        znesek_stave = self.znesek_stave
        dobicek = 0
        for stava in stavljene_stevilke:
            if int(stava) == 46 or int(stava) == 47 or int(stava) == 48:
                if int(stava) == 46:
                    if int(self.zgodovina[-1]) in range(1, 35, 3):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                elif int(stava) == 47:
                    if int(self.zgodovina[-1]) in range(2, 36, 3):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
                else:
                    if int(self.zgodovina[-1]) in range(3, 37, 3):
                        dobicek += 2 * float(znesek_stave)
                    else:
                        dobicek += (-1) * float(znesek_stave)
        return dobicek    
    
    def pridobi_stevilo_stav(self, stavljene_stevilke):
        stevilo_trenutnih_stav = 0
        for stava in stavljene_stevilke:
            stevilo_trenutnih_stav += 1
        return stevilo_trenutnih_stav
        
   
    def pridobi_vrednost_trenutnih_stav(self, stavljene_stevilke):
        return float(self.znesek_stave * self.pridobi_stevilo_stav(stavljene_stevilke))

    def rezultat_stav(self, stavljene_stevilke):
        dobicek = self.stava_na_barvo(stavljene_stevilke) + self.stava_na_ducat(stavljene_stevilke) + self.stava_na_polovicko(stavljene_stevilke) + self.stava_na_vrstico(stavljene_stevilke) + self.stava_na_eno_številko(stavljene_stevilke) + self.stava_na_sodo_liho(stavljene_stevilke)
        return dobicek
    

    
def je_dovolj_denarja(igralec, znesek_stave):
    return (igralec.stanje_na_racunu - znesek_stave) >= 0

def preveri_ce_je_stevilka(cifra):
    x = cifra
    if x.isnumeric() == True:
            return True
    else:
        return False


class Igralec:
    def __init__(self, znesek_pologa):
        self.stanje_na_racunu = int(znesek_pologa)
        self.znesek_stave = 0
        self.igra = Igra(self.znesek_stave)
   
    def dodaj(self, dobicek):
        self.stanje_na_racunu += float(dobicek)
        
       

 
    
