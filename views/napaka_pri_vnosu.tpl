%rebase('baza.tpl')
    <form action="/polog/" method="post">
    <h1>Prišlo je do napake pri vnosu.</h1>
    <h1>Prosim, vnesite neničeln znesek.</h1>

    <div class="input-group mb-3">
  <input class="input" type="text" placeholder="Polog" aria-label="Polog" aria-describedby="button-addon2" name="znesek_pologa">
  <div class="input-group-append">
    <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Naloži denar.</button>
  </div>
</div>
    </form>
