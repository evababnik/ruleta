%rebase('baza.tpl')
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;
  padding:10px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-o3f9{background-color:#fffe65;border-color:inherit;font-family:Verdana, Geneva, sans-serif !important;;font-size:14px;
  text-align:left;vertical-align:middle}
.tg .tg-rfce{background-color:#013300;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-f4zg{background-color:#009901;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-o799{background-color:#fffe65;border-color:inherit;font-size:14px;text-align:left;vertical-align:top}
.tg .tg-706m{background-color:#009901;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-rx1r{background-color:#34ff34;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-tkh2{background-color:#fe0000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-y2p1{background-color:#000000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-ovck{background-color:#fe0000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-roz7{background-color:#000000;border-color:#ffffff;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;;
  font-size:22px;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 656px">
<colgroup>
<col style="width: 48px">
<col style="width: 48px">
<col style="width: 48px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 47px">
<col style="width: 21px">
<col style="width: 21px">
</colgroup>
<thead>
  <tr>
    <th class="tg-o799" colspan="6">STANJE NA RAČUNU: {{trenutno_stanje_na_racunu}}</th>
    <th class="tg-706m"></th>
    <th class="tg-o3f9" colspan="6">VREDNOST DOBIČKA</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
   <form submit action="/preveri_stave/" method="POST">
  <tr>
    <td class="tg-rx1r" rowspan="3">0<input type="checkbox" name="stavljena_stevilka" value="0"></td>
    <td class="tg-tkh2">3<input type="checkbox" name="stavljena_stevilka" value="3"></td>
    <td class="tg-y2p1">6<input type="checkbox" name="stavljena_stevilka" value="6"></td>
    <td class="tg-tkh2">9<input type="checkbox" name="stavljena_stevilka" value="9"></td>
    <td class="tg-tkh2">12<input type="checkbox" name="stavljena_stevilka" value="12"></td>
    <td class="tg-y2p1">15<input type="checkbox" name="stavljena_stevilka" value="15"></td>
    <td class="tg-tkh2">18<input type="checkbox" name="stavljena_stevilka" value="18"></td>
    <td class="tg-tkh2">21<input type="checkbox" name="stavljena_stevilka" value="21"></td>
    <td class="tg-y2p1">24<input type="checkbox" name="stavljena_stevilka" value="24"></td>
    <td class="tg-tkh2">27<input type="checkbox" name="stavljena_stevilka" value="27"></td>
    <td class="tg-tkh2">30<input type="checkbox" name="stavljena_stevilka" value="30"></td>
    <td class="tg-y2p1">33<input type="checkbox" name="stavljena_stevilka" value="33"></td>
    <td class="tg-tkh2">36<input type="checkbox" name="stavljena_stevilka" value="36"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-y2p1">2<input type="checkbox" name="stavljena_stevilka" value="2"></td>
    <td class="tg-tkh2">5<input type="checkbox" name="stavljena_stevilka" value="5"></td>
    <td class="tg-y2p1">8<input type="checkbox" name="stavljena_stevilka" value="8"></td>
    <td class="tg-y2p1">11<input type="checkbox" name="stavljena_stevilka" value="11"></td>
    <td class="tg-tkh2">14<input type="checkbox" name="stavljena_stevilka" value="14"></td>
    <td class="tg-y2p1">17<input type="checkbox" name="stavljena_stevilka" value="17"></td>
    <td class="tg-y2p1">20<input type="checkbox" name="stavljena_stevilka" value="20"></td>
    <td class="tg-tkh2">23<input type="checkbox" name="stavljena_stevilka" value="23"></td>
    <td class="tg-y2p1">26<input type="checkbox" name="stavljena_stevilka" value="26"</td>
    <td class="tg-y2p1">29<input type="checkbox" name="stavljena_stevilka" value="29"></td>
    <td class="tg-tkh2">32<input type="checkbox" name="stavljena_stevilka" value="32"></td>
    <td class="tg-y2p1">35<input type="checkbox" name="stavljena_stevilka" value="35"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-tkh2">1<input type="checkbox" name="stavljena_stevilka" value="1"></td>
    <td class="tg-y2p1">4<input type="checkbox" name="stavljena_stevilka" value="4"></td>
    <td class="tg-tkh2">7<input type="checkbox" name="stavljena_stevilka" value="7"></td>
    <td class="tg-y2p1">10<input type="checkbox" name="stavljena_stevilka" value="10"></td>
    <td class="tg-y2p1">13<input type="checkbox" name="stavljena_stevilka" value="13"></td>
    <td class="tg-tkh2">16<input type="checkbox" name="stavljena_stevilka" value="16"></td>
    <td class="tg-tkh2">19<input type="checkbox" name="stavljena_stevilka" value="19"></td>
    <td class="tg-y2p1">22<input type="checkbox" name="stavljena_stevilka" value="22"></td>
    <td class="tg-tkh2">25<input type="checkbox" name="stavljena_stevilka" value="25"></td>
    <td class="tg-y2p1">28<input type="checkbox" name="stavljena_stevilka" value="28"></td>
    <td class="tg-y2p1">31<input type="checkbox" name="stavljena_stevilka" value="31"></td>
    <td class="tg-tkh2">34<input type="checkbox" name="stavljena_stevilka" value="34"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-f4zg" colspan="13"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-rfce" colspan="2">LIHA<input type="checkbox" name="stavljena_stevilka" value="60"></td>
    <td class="tg-f4zg"></td>
    <td class="tg-ovck" colspan="3">RDEČA<input type="checkbox" name="stavljena_stevilka" value="70"></td>
    <td class="tg-f4zg"></td>
    <td class="tg-roz7" colspan="3">ČRNA<input type="checkbox" name="stavljena_stevilka" value="50"></td>
    <td class="tg-f4zg"></td>
    <td class="tg-rfce" colspan="2">SODA<input type="checkbox" name="stavljena_stevilka" value="40"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>
<input class="button" type="submit" name="zacni" value="Vrži kroglico"> 

</form>