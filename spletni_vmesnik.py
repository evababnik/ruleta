import bottle
import model
from model import Igra

igra = Igra()

@bottle.get('/')
def osnovna():
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/zacni/')
def zacni():
    return bottle.template('polog_denarja.tpl')

@bottle.get('/pokazi_navodila/')
def pokazi_navodila():
    return bottle.template('pravila_rulete.tpl')

@bottle.post('/znesek_pologa/')
def polog():
    znesek_pologa = bottle.request.forms['znesek_pologa']
    if int(znesek_pologa) == 0:
        return bottle.template('nicelna_stava.tpl')
    else:
        igra.stanje_na_racunu = znesek_pologa
        return bottle.template('znesek_stave.tpl')
   #else:
        #return bottle.template('napaka_pri_vnosu.tpl')

@bottle.post('/znesek_stave/')
def znesek_stave():
    znesek_stave = bottle.request.forms['znesek_stave']
    return bottle.template('igralno_polje.tpl')

@bottle.post('/preveri_stave/')
def preveri_stave():
    stavljena_stevilka = bottle.request.forms['stavljena_stevilka']
    znesek_stave = bottle.request.forms['znesek_stave']

    

bottle.run(debug=True, reloader=True)