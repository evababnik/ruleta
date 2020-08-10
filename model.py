import random

class Igra:
    stevilke = {0: 'Zelena', 1: 'Rdeča', 2: 'Črna', 3: 'Rdeča', 4: 'Črna', 5: 'Rdeča', 6: 'Črna', 7: 'Rdeča', 8:'Črna', 9: 'Rdeča', 10: 'Črna', 11: 'Črna', 12: 'Rdeča', 13: 'Črna', 14: 'Rdeča', 15: 'Črna', 16: 'Rdeča', 17: 'Črna', 18: 'Rdeča', 19:'Rdeča', 20: 'Črna', 21: 'Rdeča', 22: 'Črna', 23: 'Rdeča', 24: 'Črna', 25: 'Rdeča', 26: 'Črna', 27: 'Rdeča', 28: 'Črna', 29: 'Črna', 30: 'Rdeča', 31: 'Črna', 32: 'Rdeča', 33: 'Črna', 34: 'Rdeča', 35: 'Črna'} 
    def __init__(self, barva, vrednost, zgodovina=None, vrsta_stave=None, stanje_na_racunu=None):
        self.barva = barva
        self.vrednost = vrednost
        if zgodovina is None:
            self.zgodovina = []
        else:
            self.zgodovina = zgodovina
        if vrsta_stave is None:
            self.vrsta_stave = 'Stava na eno številko'
        else:
            self.vrsta_stave = vrsta_stave
        if stanje_na_racunu is None:
            self.stanje_na_racunu = 2500.0
        else:
            self.stanje_na_racunu = float(stanje_na_racunu)
        
    def __str__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)
    
    def vrzi_kroglico(self):
        dobljena_stevilka = random.randint(0, 36)
        self.zgodovina.append(dobljena_stevilka)
        return dobljena_stevilka

