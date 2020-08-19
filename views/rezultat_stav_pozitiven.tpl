%rebase('baza.tpl')


<h1>Padla je številka <img src="../img/{{dobljena_stevilka}}.jpg" alt"dobljena_stevilka" width="60" height="60"></h1>
<h1>Čestitam! Zaslužili ste {{dobicek}} €. </h1>
<h1>Na vašem računu je še {{stanje_na_racunu}} €. </h1>

<form action="/igra/" method="GET">
    <button type="submit" class="btn btn-secondary btn-lg">Nadaljuj.</button>
</form>