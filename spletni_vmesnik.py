import bottle
import model
from model import Igra

igra = Igra(0)

@bottle.get('/')
def osnovna():
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/zacni/')
def zacni():
    return bottle.template('polog_denarja.tpl')

@bottle.get('/pokazi_navodila/')
def pokazi_navodila():
    return bottle.template('pravila_rulete.tpl')

@bottle.post('/polog/')
def polog():
    znesek_pologa = bottle.request.forms['znesek_pologa']
    if int(znesek_pologa) == 0:
        return bottle.template('nicelna_stava.tpl')
    else:
        igra.stanje_na_racunu = znesek_pologa
        return bottle.template('znesek_stave')
   #else:
        #return bottle.template('napaka_pri_vnosu.tpl')

@bottle.post('/znesek_stave/')
def znesek_stave():
    igra.znesek_stave = bottle.request.forms['znesek_stave']
    trenutno_stanje_na_racunu = igra.stanje_na_racunu
    return bottle.template('igralno_polje.tpl', trenutno_stanje_na_racunu = trenutno_stanje_na_racunu)



@bottle.post('/preveri_stave/')
def preveri_stave():
    stavljene_stevilke = bottle.request.forms.getall('stavljena_stevilka')
    dobljena_stevilka = igra.vrzi_kroglico()
    denar = igra.rezultat_stav(stavljene_stevilke)
    return bottle.template('rezultat_stav.tpl', dobljena_stevilka = dobljena_stevilka, denar = denar)



    

bottle.run(debug=True, reloader=True)