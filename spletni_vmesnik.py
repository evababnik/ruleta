import bottle
import model
import random
from model import Igra, Igralec
igra = Igra(0)

stanja = {}

def stanje_igralca():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    if st_uporabnika is None:
        st_uporabnika = str(random.randint(0, 2 ** 45))
        stanja[st_uporabnika] = Igralec(0)
        bottle.response.set_cookie('st_uporabnika', st_uporabnika, path='/')
    return stanja[st_uporabnika]

@bottle.get('/')
def osnovna():
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/polog/')
def zacni():
    return bottle.template('polog_denarja.tpl')

@bottle.get('/pokazi_navodila/')
def pokazi_navodila():
    return bottle.template('pravila_rulete.tpl')

@bottle.post('/polog/')
def polog0():
    print(stanja)
    igralec = stanje_igralca()
    znesek_pologa = bottle.request.forms['znesek_pologa']
    if model.preveri_ce_je_stevilka(znesek_pologa) == True:
        if float(znesek_pologa) == 0:
            return bottle.template('nicelna_stava.tpl')
        else:
            igralec.stanje_na_racunu = float(znesek_pologa)
            bottle.redirect('/igra/')
    else:
        return bottle.template('napaka_pri_vnosu.tpl')

@bottle.get('/igra/')
def polog():   
    igralec = stanje_igralca()
    return bottle.template('igralno_polje.tpl', trenutno_stanje_na_racunu = igralec.stanje_na_racunu, zgodovina = igra.zgodovina)
    

@bottle.post('/igra1/')
def igra1():
    igralec = stanje_igralca()
    igra.znesek_stave = float(bottle.request.forms['znesek_stave'])
    stavljene_stevilke = bottle.request.forms.getall('stavljena_stevilka')
    if int(igra.pridobi_vrednost_trenutnih_stav(stavljene_stevilke)) > igralec.stanje_na_racunu:
        return bottle.template('neveljavna_igra.tpl')
    else:
        dobicek = igra.poslji_stave(stavljene_stevilke)
        dobljena_stevilka = igra.zgodovina[-1]
        igralec.dodaj(dobicek)
        igralec.znesek_stave = 0
        if igralec.stanje_na_racunu == 0:
            return bottle.template('nic_denarja.tpl', dobljena_stevilka = dobljena_stevilka, dobicek = (-1)*dobicek)
        else:
            if dobicek < 0:
                dobicek *= (-1)
                return bottle.template('rezultat_stav_negativen.tpl',  dobljena_stevilka = dobljena_stevilka, dobicek = dobicek, stanje_na_racunu = igralec.stanje_na_racunu)
            elif dobicek == 0:
                return bottle.template('rezultat_stav_nic.tpl',  dobljena_stevilka = dobljena_stevilka, dobicek = dobicek, stanje_na_racunu = igralec.stanje_na_racunu)
            else:
                return bottle.template('rezultat_stav_pozitiven.tpl', dobljena_stevilka = dobljena_stevilka, dobicek = dobicek, stanje_na_racunu = igralec.stanje_na_racunu)


@bottle.get('/img/<picture>')
def serve_pictures(picture, root='img'):
    return bottle.static_file(picture, root='img')

@bottle.get('/izplacaj/')
def izplacaj():
    igralec = stanje_igralca()
    return bottle.template('izplacilo.tpl', denar = igralec.stanje_na_racunu)



    

bottle.run(debug=True, reloader=True)

