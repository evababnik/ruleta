%rebase('baza.tpl')
 
<h1>Padla je številka <img src="../img/{{dobljena_stevilka}}.jpg" alt="zgodovina">.</h1>
<h1>Zgubili ste {{dobicek}} €. </h1>
<h1>Na računu nimate več denarja.</h1>
<br>
<form action="/izplacaj/" method="GET">
          <button type="submit" class="btn btn-secondary btn-lg">Končaj.</button>
        </form>
</br>
<br>
<form action="/polog/" method="GET">
          <button type="submit" class="btn btn-secondary btn-lg">Ponovno naloži denar.</button>
        </form>
</br>  
    