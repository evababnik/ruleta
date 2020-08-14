import bottle
import model

@bottle.get('/')
def osnovna():
    return bottle.template('osnovna_stran.tpl')

@bottle.post('/zacni/')
def prva_izbira():
    answer = bottle.request.forms['odgovor1']
    if answer == 'Zanimajo me pravila igre.':
        return bottle.template('pravila_rulete.tpl')
    else:
        return bottle.redirect('/polog/')

@bottle.get('/polog/')
def polog():
    return bottle.template('polog_denarja.tpl')

@bottle.post('/stanje_racuna/')
def polog():
    znesek_pologa = bottle.request.forms['stanje_racuna']
    if isinstance(float(znesek_pologa), int) == True:
        znesek_pologa = float(znesek_pologa)
        if znesek_pologa == 0:
            return bottle.template('nicelna_stava.tpl')
        else:
            igralec.stanje_na_racunu = znesek_pologa
            return bottle.redirect('/zetoni/')
    else:
        return bottle.template('napaka_pri_vnosu.tpl')

@bottle.get('/zetoni/')
def zetoni():
    return bottle.template('znesek_stave.tpl')

@bottle.post('/znesek_stave/')
def znesek_stave():
    znesek_stave = bottle.request.forms['znesek_stave']
    return bottle.template('igralno_polje.tpl')

@bottle.post('/preveri_stave/')
def preveri_stave():
    stavljena_stevilka = bottle.request.forms['stavljena_stevilka']
    znesek_stave = bottle.request.forms['znesek_stave']

    

        



bottle.run(debug=True, reloader=True)