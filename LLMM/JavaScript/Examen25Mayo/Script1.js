function Cual_Calculo(evento){
    var calc_type = typeof evento.value
    console.log(calc_type)
    calculo = evento.value
}
var segu = 0;
var decsegu = 0;
var minu = 2;
function PaTras() { 'setInterval(tictac, 1000)' }
function tictac(){
    /*if (segu == 0 && decsegu == 0 && minu == 0) { window.close() }
    if(segu>0) { segu -= 1 }
    else { if(decsegu>0) { decsegu -= 1 }
                else { if(minu>0) { minu -= 1 }
                            else { minu =  1} decsegu = 5} segu = 9}
    document.getElementById("min").src = "Contador/" + minu + ".png";
	document.getElementById("segu2").src = "Contador/" + decsegu + ".png";
	document.getElementById("segu").src = "Contador/" + segu + ".png";*/
}
function Calcular(){
    console.log(typeof calculo)
    console.log(calculo)
}
