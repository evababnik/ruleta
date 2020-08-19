%rebase('baza.tpl')
%import model
<h1> Hvala za igro!</h1>
%if denar == 0:
    <h1>Več sreče prihodnjič!</h1>
%else:
 <h1>Izplačalo znaša {{denar}} €.</h1>
 %end 