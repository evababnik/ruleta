%rebase('baza.tpl')
%import model
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-b7tv{border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-frof{background-color:#fe0000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-hv39{background-color:#fffc9e;border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-vywn{background-color:#fffe65;border-color:#ffffff;font-size:18px;text-align:center;vertical-align:middle}
.tg .tg-oe15{background-color:#ffffff;border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-6xes{background-color:#013300;border-color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;font-size:16px;
  text-align:left;vertical-align:top}
.tg .tg-kaak{background-color:#ffffff;border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-rfce{background-color:#013300;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-sflf{background-color:#fffe65;border-color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;font-size:16px;
  text-align:center;vertical-align:top}
.tg .tg-cy1s{background-color:#000000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-eniz{background-color:#013300;border-color:#ffffff;color:#ffffff;font-size:36px;text-align:center;text-decoration:underline;
  vertical-align:top}
.tg .tg-2kkx{background-color:#013300;border-color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;font-size:16px;
  text-align:left;vertical-align:top}
.tg .tg-bgqu{background-color:#fffe65;border-color:#ffffff;font-size:14px;text-align:center;vertical-align:middle}
.tg .tg-b48g{background-color:#013300;border-color:#ffffff;color:#ffffff;font-size:36px;font-weight:bold;text-align:center;
  text-decoration:underline;vertical-align:top}
.tg .tg-rx1r{background-color:#34ff34;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-ovck{background-color:#fe0000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-roz7{background-color:#000000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-2p55{background-color:#013300;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:16px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-g3v6{background-color:#ffffff;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-7zlr{background-color:#013300;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-4tmb{background-color:#ffffff;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 1262px">
<colgroup>
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 54px">
<col style="width: 123px">
<col style="width: 22px">
<col style="width: 400px">
</colgroup>
<thead>
  <tr>
    <th class="tg-vywn" colspan="13"><span style="font-weight:bold">IZBERITE VREDNOST VAŠIH ŽETONOV IN NATO STAVITE</span></th>
    <th class="tg-oe15"></th>
    <th class="tg-zv4m"></th>
    <th class="tg-sflf"><span style="font-weight:bold">ZGODOVINA PADLIH ŠTEVILK</span></th>
  </tr>
</thead>
<tbody>
  <tr>
  <form action="/igra1/" method="post">
    <td class="tg-kaak" rowspan="2"></td>
    <td class="tg-eniz" colspan="2" rowspan="2"><span style="font-weight:bold">2<input type="radio" name="znesek_stave" value="2" checked></span></td>
    <td class="tg-kaak" rowspan="2"></td>
    <td class="tg-b48g" colspan="2" rowspan="2"><span style="font-weight:bold">5<input type="radio" name="znesek_stave" value="5"></span></td>
    <td class="tg-kaak" rowspan="2"></td>
    <td class="tg-b48g" colspan="2" rowspan="2"><span style="font-weight:bold">10<input type="radio" name="znesek_stave" value="10"></span></td>
    <td class="tg-kaak" rowspan="2"></td>
    <td class="tg-b48g" colspan="2" rowspan="2">20<input type="radio" name="znesek_stave" value="20"></td>
    <td class="tg-kaak" rowspan="2"></td>
    <td class="tg-kaak"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-hv39" rowspan="13">
    %for cifra in zgodovina:
 <img src="../img/{{cifra}}.jpg" alt"dobljena_stevilka"width="95" height="95" >
%end
    </td>
  </tr>
  <tr>
    <td class="tg-oe15"></td>
    <td class="tg-zv4m"></td>
  </tr>
  <tr>
    <td class="tg-bgqu" colspan="13"><img src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3e%3cpath fill='%23000000' d='M0 405.3V448c0 35.3 86 64 192 64s192-28.7 192-64v-42.7C342.7 434.4 267.2 448 192 448S41.3 434.4 0 405.3zM320 128c106 0 192-28.7 192-64S426 0 320 0 128 28.7 128 64s86 64 192 64zM0 300.4V352c0 35.3 86 64 192 64s192-28.7 192-64v-51.6c-41.3 34-116.9 51.6-192 51.6S41.3 334.4 0 300.4zm416 11c57.3-11.1 96-31.7 96-55.4v-42.7c-23.2 16.4-57.3 27.6-96 34.5v63.6zM192 160C86 160 0 195.8 0 240s86 80 192 80 192-35.8 192-80-86-80-192-80zm219.3 56.3c60-10.8 100.7-32 100.7-56.3v-42.7c-35.5 25.1-96.5 38.6-160.7 41.8 29.5 14.3 51.2 33.5 60 57.2z'/%3e%3c/svg%3e" alt="Image" width="30" height="30"># <span style="font-weight:700">STANJE NA RAČUNU: {{trenutno_stanje_na_racunu}} €</span></td>
    <td class="tg-kaak"></td>
    <td class="tg-b7tv"></td>
  </tr>
  <tr>
    <td class="tg-rx1r" rowspan="3">0<input type="checkbox" name="stavljena_stevilka" value="0"></td>
    <td class="tg-ovck"><span style="font-weight:bold">3<input type="checkbox" name="stavljena_stevilka" value="3"></span></td>
    <td class="tg-roz7">6<input type="checkbox" name="stavljena_stevilka" value="6"></td>
    <td class="tg-ovck">9<input type="checkbox" name="stavljena_stevilka" value="9"></td>
    <td class="tg-ovck">12<input type="checkbox" name="stavljena_stevilka" value="12"></td>
    <td class="tg-roz7">15<input type="checkbox" name="stavljena_stevilka" value="15"></td>
    <td class="tg-ovck">18<input type="checkbox" name="stavljena_stevilka" value="18"></td>
    <td class="tg-ovck">21<input type="checkbox" name="stavljena_stevilka" value="21"></td>
    <td class="tg-roz7">24<input type="checkbox" name="stavljena_stevilka" value="24"></td>
    <td class="tg-ovck">27<input type="checkbox" name="stavljena_stevilka" value="27"></td>
    <td class="tg-ovck">30<input type="checkbox" name="stavljena_stevilka" value="30"></td>
    <td class="tg-roz7">33<input type="checkbox" name="stavljena_stevilka" value="33"></td>
    <td class="tg-ovck">36<input type="checkbox" name="stavljena_stevilka" value="36"></td>
    <td class="tg-6xes"><span style="font-weight:bold;color:#FFF">TRETJA VRSTICA<input type="checkbox" name="stavljena_stevilka" value="48"></span></td>
    <td class="tg-zv4m"></td>
  </tr>
  <tr>
    <td class="tg-cy1s">2<span style="font-weight:bold"><input type="checkbox" name="stavljena_stevilka" value="2"></span></td>
    <td class="tg-frof">5<input type="checkbox" name="stavljena_stevilka" value="5"></td>
    <td class="tg-cy1s">8<input type="checkbox" name="stavljena_stevilka" value="8"></td>
    <td class="tg-cy1s">11<input type="checkbox" name="stavljena_stevilka" value="11"></td>
    <td class="tg-frof">14<input type="checkbox" name="stavljena_stevilka" value="14"></td>
    <td class="tg-cy1s">17<input type="checkbox" name="stavljena_stevilka" value="17"></td>
    <td class="tg-cy1s">20<input type="checkbox" name="stavljena_stevilka" value="20"></td>
    <td class="tg-frof">23<input type="checkbox" name="stavljena_stevilka" value="23"></td>
    <td class="tg-cy1s">26<input type="checkbox" name="stavljena_stevilka" value="26"></td>
    <td class="tg-cy1s">29<input type="checkbox" name="stavljena_stevilka" value="29"></td>
    <td class="tg-frof">32<input type="checkbox" name="stavljena_stevilka" value="32"></td>
    <td class="tg-cy1s">35<input type="checkbox" name="stavljena_stevilka" value="35"></td>
    <td class="tg-2kkx"><span style="font-weight:bold;color:#FFF">DRUGA VRSTICA<input type="checkbox" name="stavljena_stevilka" value="47"></span></td>
    <td class="tg-b7tv"></td>
  </tr>
  <tr>
    <td class="tg-ovck">1<input type="checkbox" name="stavljena_stevilka" value="1"></td>
    <td class="tg-roz7">4<input type="checkbox" name="stavljena_stevilka" value="4"></td>
    <td class="tg-ovck">7<input type="checkbox" name="stavljena_stevilka" value="7"></td>
    <td class="tg-roz7">10<input type="checkbox" name="stavljena_stevilka" value="10"></td>
    <td class="tg-roz7">13<input type="checkbox" name="stavljena_stevilka" value="13"></td>
    <td class="tg-ovck">16<input type="checkbox" name="stavljena_stevilka" value="16"></td>
    <td class="tg-ovck">19<input type="checkbox" name="stavljena_stevilka" value="19"></td>
    <td class="tg-roz7">22<input type="checkbox" name="stavljena_stevilka" value="22"></td>
    <td class="tg-ovck">25<input type="checkbox" name="stavljena_stevilka" value="25"></td>
    <td class="tg-roz7">28<input type="checkbox" name="stavljena_stevilka" value="28"></td>
    <td class="tg-roz7">31<input type="checkbox" name="stavljena_stevilka" value="31"></td>
    <td class="tg-ovck">34<input type="checkbox" name="stavljena_stevilka" value="34"></td>
    <td class="tg-2p55"><span style="font-weight:bold">PRVA VRSTICA<input type="checkbox" name="stavljena_stevilka" value="46"></span></td>
    <td class="tg-zv4m"></td>
  </tr>
  <tr>
    <td class="tg-g3v6"></td>
    <td class="tg-7zlr" colspan="4">PRVIH 12<input type="checkbox" name="stavljena_stevilka" value="43"></td>
    <td class="tg-7zlr" colspan="4">DRUGIH 12<input type="checkbox" name="stavljena_stevilka" value="44"></td>
    <td class="tg-7zlr" colspan="4">TRETJIH 12<input type="checkbox" name="stavljena_stevilka" value="45"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
  </tr>
  <tr>
    <td class="tg-4tmb"></td>
    <td class="tg-rfce" colspan="2">1-18<input type="checkbox" name="stavljena_stevilka" value="41"></td>
    <td class="tg-rfce" colspan="2">LIHA<input type="checkbox" name="stavljena_stevilka" value="60"></td>
    <td class="tg-ovck" colspan="2">RDEČA<input type="checkbox" name="stavljena_stevilka" value="70"></td>
    <td class="tg-roz7" colspan="2">ČRNA<input type="checkbox" name="stavljena_stevilka" value="50"></td>
    <td class="tg-rfce" colspan="2">SODA<input type="checkbox" name="stavljena_stevilka" value="40"></td>
    <td class="tg-rfce" colspan="2">19-36<input type="checkbox" name="stavljena_stevilka" value="42"></td>
    <td class="tg-zv4m"></td>
    <td class="tg-zv4m"></td>
  </tr>
  <tr>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
    <td class="tg-b7tv"></td>
  </tr>
  <tr>
    <td class="tg-oe15"></td>
    <td class="tg-oe15" colspan="4"><button type="submit" class="btn btn-secondary btn-lg">Vrzi kroglico.</button> 
</form>
</td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15" colspan="4"><form action="/izplacaj/", method="get">
<button type="submit" class="btn btn-secondary btn-lg">Zaključi igro in izplačaj denar.</button></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
  </tr>
  <tr>
    <td class="tg-kaak"></td>
    <td class="tg-kaak" colspan="4"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
  </tr>
  <tr>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
    <td class="tg-oe15"></td>
  </tr>
  <tr>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
    <td class="tg-kaak"></td>
  </tr>
</tbody>
</table>
 