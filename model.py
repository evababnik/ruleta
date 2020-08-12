import random
import json

GESLO_NI_PRAVILNO = 'Nepravilno geslo.'

class Igralec:
    def __init__(self, stanje_na_racunu=None, username, geslo)
        self.username = username
        if self.stanje_na_racunu is None:
            self.stanje_na_racunu = 2500.0
        else:
            self.stanje_na_racunu = float(stanje_na_racunu) 
        self.geslo = geslo
    
    def ali_se_gesli_ujemata(self, geslo):
        if self.geslo != geslo:
            return GESLO_NI_PRAVILNO
    
    def shrani_uporabnikove_podatke(self, datoteka):
        stanje = {'username': self.username, 'geslo': self.geslo, 'podatek': self.shrani_stanje_na_racunu.podatek}
        with open(datoteka, 'w', encoding='utf-8') as dat:
            json.dump(stanje, dat, ensure_ascii=Fase, indent=4)
   
    def odpri_uporabnikove_podatke(datoteka):
        with open(datoteka, encoding='utf-8') as dat:
            stanje = json-load(dat)
        username = stanje['username']
        geslo = stanje['geslo']
        stanje_na_racunu = Stanje_racuna(stanje['podatek'])
        return Igralec(stanje_na_racunu, username, geslo)
    
class Stanje_racuna:


class Igra:
    zelena = {0}
    crna = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    rdeca = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34}

    def __init__(self, barva, vrednost, zgodovina=None, zgodovina_barv=None, vrsta_stave=None, stanje_na_racunu=None):
        self.barva = barva
        self.vrednost = int(vrednost)
        if zgodovina is None:
            self.zgodovina = []
        else:
            self.zgodovina = zgodovina
        if vrsta_stave is None:
            self.vrsta_stave = 'stava_na_eno_številko'
        else:
            self.vrsta_stave = vrsta_stave
        if stanje_na_racunu is None:
            self.stanje_na_racunu = 2500.0
        else:
            self.stanje_na_racunu = float(stanje_na_racunu)
        if zgodovina_barv is None:
            self.zgodovina_barv = []
        else:
            self.zgodovina_barv = zgodovina_barv
        
    def __str__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)
    
    def belezi_barve(self, dobljena_stevilka):
        if dobljena_stevilka in self.rdeca:
            self.zgodovina_barv.append('rdeca')
        elif dobljena_stevilka in self.crna:
            self.zgodovina_barv.append('crna')
        else:
            self.zgodovina_barv.append('zelena')
    
    def vrzi_kroglico(self):
        dobljena_stevilka = random.randint(0, 36)
        self.zgodovina.append(dobljena_stevilka)
        return dobljena_stevilka

    
    def belezi_statistiko(self, dobljena_stevilka):
        pass
    
    
    def je_liha_soda(self, dobljena_stevilka):
        if int(dobljena_stevilka) % 2 == 0:
            return ('soda')
        elif int(dobljena_stevilka) % 2 != 0:
            return ('liha')
        else:
            return False

        
    def stava_na_eno_številko(self, stavljena_stevilka=None, znesek_stave=None):
        if int(stavljena_stevilka) <= 36 and int(stavljena_stevilka) >= 0:
            dobljena_stevilka = self.vrzi_kroglico()
            if dobljena_stevilka == int(stavljena_stevilka):
                self.stanje_na_racunu += 36 * float(znesek_stave)
                return self.stanje_na_racunu
            else:
                self.stanje_na_racunu -= float(znesek_stave)
                return self.stanje_na_racunu
        return False
        
    def stava_na_barvo(self, stavljena_stevilka=None, znesek_stave=None):
        if stavljena_stevilka in self.rdeca or stavljena_stevilka in self.crna:
            self.vrzi_kroglico()
            if self.zgodovina_barv[-1] == stavljena_stevilka:
                self.stanje_na_racunu += 2 * float(znesek_stave)
                return self.stanje_na_racunu
            else:
                self.stanje_na_racunu -= float(znesek_stave)
                return self.stanje_na_racunu 
        return False

    def stava_na_sodo_liho(self, stavljena_stevilka, znesek_stave=None):
        if stavljena_stevilka == 'soda' or stavljena_stevilka == 'liha':
            dobljena_stevilka = self.vrzi_kroglico()
            liha_soda = self.je_liha_soda(dobljena_stevilka)
            if liha_soda == stavljena_stevilka:
                self.stanje_na_racunu += 2 * float(znesek_stave)
                return self.stanje_na_racunu
            else:
                self.stanje_na_racunu -= float(znesek_stave)
                return self.stanje_na_racunu
        return False



def preveri_zacetni_odgovor(odgovor):
    if odgovor == '1':
        return 'prvi'
    elif odgovor == '2':
        return 'drugi'
    return False 
    
def je_dovolj_denarja(igralec, znesek_stave):
    return (igralec.stanje_na_racunu - znesek_stave) >= 0


def preveri_vrsto_stave(vrsta_stave):
    if vrsta_stave == '1':
        return 'cifra'
    elif vrsta_stave == '2':
        return 'barva'
    elif vrsta_stave == '3':
        return 'sodost'
    return False

def preveri_stavljeno_barvo(stavljena_barva):
    if stavljena_barva == '1':
        return 'rdeca'
    elif stavljena_barva == '2':
        return 'crna'
    return False

def preveri_dodatno_stavo(dodatna_stava):
    if dodatna_stava == '1':
        return 'dodaj'
    elif dodatna_stava == '2':
        return 'zacni'
    else:
        return False

def preveri_stavljeno_sodost(stavljena_sodost):
    if stavljena_sodost == '1':
        return 'soda'
    elif stavljena_sodost == '2':
        return 'liha'
    else:
        return False

            
                
            


   
           
    


