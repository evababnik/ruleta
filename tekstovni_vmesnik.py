import model
from model import Igra
import time

def uvod():
    print ('Pozdravljeni! Danes je vaš srečen dan.')
    zacetek()
    igralec = stava_na_igro()
    if igralec.je_dovolj_denarja():
        zmanjkalo_je_denarja()
        return False
    else:
        pass
    return igralec



def zmanjkalo_je_denarja():
    pass

def stava_na_igro():
    print('Kakšno stavo želite?')
    print ('1) Stava na številko.')
    print ('2) Stava na barvo')
    print ('3) Stava na liho ali sodo število')
    vrsta_stave = input('>')
    vrsta_stave = model.preveri_vrsto_stave(vrsta_stave)
    if vrsta_stave == 'cifra':
        stevilcna_stava()
    elif vrsta_stave == 'barva':
        barvna_stava()
    elif vrsta_stave == 'sodost':
        soda_stava()
    else:
        print('Prišlo je do napake: lahko izbirate med števili 1, 2 ali 3.')

def stevilcna_stava():
    print ('Vpišite število od 0 do 36 na katerega želite staviti.')
    stavljena_stevilka = input('>')
    koliko_denarja_zelite_staviti(igralec)

def barvna_stava():
    print('Na katero barvo želite staviti?')
    print('1) Rdeča')
    print('2')
    stavljena_barva = input ('>')
    stavljena_barva = model.preveri_stavljeno_barvo(stavljena_barva)
    if stavljena_barva == 'rdeca':
        stavljena_stevilka = 'rdeca'
        koliko_denarja_zelite_staviti(igralec)
    elif stavljena_barva == 'crna':
        stavljena_stevilka = 'crna'
        koliko_denarja_zelite_staviti(igralec)
    else:
        print('Prišlo je do napake: prosim vpišite 1 ali 2.')
        barvna_stava()
    

def soda_stava():
    print('Ali želite staviti na vsa liha ali vsa soda števila?')
    print ('1) soda')
    print ('2) liha')
    stavljena_sodost = input('>')
    stavljena_sodost = model.preveri_stavljeno_sodost(stavljena_sodost)
    if stavljena_sodost == 'soda':
        stavljena_stevilka = 'soda'
        koliko_denarja_zelite_staviti(igralec)
    elif stavljena_sodost == 'liha':
        stavljena_stevilka = 'soda'
        koliko_denarja_zelite_staviti(igralec)
    else:
        print('Prišlo je do napake: prosim vpišite 1 ali 2.')
        soda_stava()

def koliko_denarja_zelite_staviti(igralec):
    print('Koliko denarja želite staviti?')
    znesek_stave = input('>')
    if isinstance(float(znesek_stave), int) == True:
        znesek_stave = float(znesek_stave)
        if znesek_stave == 0:
            print('Stavili niste nič.')
            return koliko_denarja_zelite_staviti(igralec)
        elif model.je_dovolj_denarja(igralec, znesek_stave):
            igralec.koliko_denarja_zelite_staviti = znesek_stave
            igralec.vzemi()
            return ali_zelite_staviti_se_kaj()
        else:
            print('Za željeno stavo nimate dovolj denarja.')
            return koliko_denarja_zelite_staviti(igralec)
    else:
        print('Neveljavna stava.')
        return koliko_denarja_zelite_staviti(igralec)


def ali_zelite_staviti_se_kaj():
    print('Ali želite staviti še kaj?')
    print ('1) Dodaj stavo')
    print ('2) Zavrti kolo!')
    dodatna_stava = input ('>')
    dodatna_stava = model.preveri_dodatno_stavo(dodatna_stava)
    if dodatna_stava == 'dodaj'
        stava_na_igro()
    elif dodatna_stava == 'zacni'
        zacni_igro()
    else:
        print('Prišlo je do napake: prosim vpišite 1 ali 2.')

def zacni_igro():
    pass

def izpis_zmage(igra):
    pass


def zacetek():
print('Kaj želite storiti?')
print ('1) Zanimajo me pravila igre.')
print ('2) Naj se igra začne!')
odgovor = input ('>')
odgovor = model.preveri_zacetni_odgovor(odgovor)
if odgovor == 'prvi':
    pokazi_pravila()
    time.sleep(10)
    zacetek()
elif odgovor == 'drugi':
    pass
else:
    print('Prišlo je do napake: prosim vpišite 1 ali 2.')
    zacetek()


def izpis_zmage(igra):
    pass


def pokazi_pravila():
    with open('pravila_rulete.txt', 'r', encoding='utf-8') as pravila:
        for vrstica in pravila:
            print(vrstica[0:])
