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
    znesek_stave = bottle.request.forms['stanje_racuna']
    if isinstance(float(znesek_stave), int) == True:
        znesek_stave = float(znesek_stave)
        if znesek_stave == 0:
            return bottle.template('nicelna_stava.tpl')
        else:
            igralec.stanje_na_racunu = znesek_stave
            return bottle.redirect('/zacni_s_stavami/')
    else:
        return bottle.template('napaka_pri_vnosu.tpl', link='/polog/')

@bottle.get

bottle.run(debug=True, reloader=True)