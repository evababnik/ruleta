%rebase('baza.tpl')
%import model

<h1>Padla je številka <img src="../img/{{dobljena_stevilka}}.jpg" alt="zgodovina"width="60" height="60" ></h1>
<h1> Nič niste zaslužili niti zgubili. </h1>
<h1> Na vašem računu je še {{stanje_na_racunu}} €. </h1>

<form action="/igra/" method="GET">
          <button type="submit" class="btn btn-secondary btn-lg">Nadaljuj.</button>
        </form>