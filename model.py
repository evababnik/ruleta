import random
import json

GESLO_NI_PRAVILNO = 'Nepravilno geslo.'


class Igra:
    ZELENA = {0}
    CRNA = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    RDECA = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34}

    def __init__(self, dobljena_stevilka=None, zgodovina=None, zgodovina_barv=None, vrsta_stave=None, stanje_na_racunu=None):
        self.dobljena_stevilka = int(dobljena_stevilka)
        if zgodovina is None:
            self.zgodovina = []
        else:
            self.zgodovina = zgodovina
        if vrsta_stave is None:
            self.vrsta_stave = 'stava_na_eno_številko'
        else:
            self.vrsta_stave = vrsta_stave
        self.stanje_na_racunu = float(stanje_na_racunu)
        if zgodovina_barv is None:
            self.zgodovina_barv = []
        else:
            self.zgodovina_barv = zgodovina_barv
        
    def __str__(self):
        return '{0}'.format(self.dobljena_stevilka)
    
    def belezi_barve(self, dobljena_stevilka):
        if dobljena_stevilka in self.RDECA:
            self.zgodovina_barv.append('RDECA')
        elif dobljena_stevilka in self.CRNA:
            self.zgodovina_barv.append('CRNA')
        else:
            self.zgodovina_barv.append('ZELENA')
    
    def vrzi_kroglico(self):
        dobljena_stevilka = random.randint(0, 36)
        self.zgodovina.append(dobljena_stevilka)
        self.zgodovina_barv(dobljena_stevilka)
        return dobljena_stevilka

    
    
    
    
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
        else:
            return 0
        
    def stava_na_barvo(self, stavljena_stevilka=None, znesek_stave=None):
        if stavljena_stevilka == 'RDECA' or stavljena_stevilka == 'CRNA':
            self.vrzi_kroglico()
            if self.zgodovina_barv[-1] == stavljena_stevilka:
                self.stanje_na_racunu += 2 * float(znesek_stave)
                return self.stanje_na_racunu
            else:
                self.stanje_na_racunu -= float(znesek_stave)
                return self.stanje_na_racunu 
        else:
            return 0

    def stava_na_sodo_liho(self, stavljena_stevilka=None, znesek_stave=None):
        if stavljena_stevilka == 'SODA' or stavljena_stevilka == 'LIHA':
            dobljena_stevilka = self.vrzi_kroglico()
            liha_soda = self.je_liha_soda(dobljena_stevilka)
            if liha_soda == stavljena_stevilka:
                self.stanje_na_racunu += 2 * float(znesek_stave)
                return self.stanje_na_racunu
            else:
                self.stanje_na_racunu -= float(znesek_stave)
                return self.stanje_na_racunu
        else:
            return 0

    def koncen_rezultat(self):
        stava_na_barvo = self.stava_na_barvo()
        stava_na_eno_številko = self.stava_na_eno_številko()
        stava_na_sodo_liho = self.stava_na_sodo_liho()
        return int(stava_na_sodo_liho) + int(stava_na_eno_številko) + int(stava_na_barvo)
    
    def novo_stanje(self, stavljena_stevilka):
        novo = self.koncen_rezultat()
        self.stanje_na_racunu += novo
        return self.stanje_na_racunu
        




    
def je_dovolj_denarja(igralec, znesek_stave):
    return (igralec.stanje_na_racunu - znesek_stave) >= 0




            
                
            


   
           
    


