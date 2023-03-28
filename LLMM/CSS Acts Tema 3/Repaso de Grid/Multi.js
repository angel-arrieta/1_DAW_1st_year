function Multiplicaciones(numero) {
numero = Number(numero.value)
if (Number.isSafeInteger(numero) == true){
    var sol = ( "<div> Número </div><div> ------------- </div><div> Multiplicador </div><div> ------------- </div><div> Resultado </div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 1 +"</div><div>=</div><div>"+ (numero*1) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 2 +"</div><div>=</div><div>"+ (numero*2) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 3 +"</div><div>=</div><div>"+ (numero*3) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 4 +"</div><div>=</div><div>"+ (numero*4) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 5 +"</div><div>=</div><div>"+ (numero*5) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 6 +"</div><div>=</div><div>"+ (numero*6) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 7 +"</div><div>=</div><div>"+ (numero*7) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 8 +"</div><div>=</div><div>"+ (numero*8) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 9 +"</div><div>=</div><div>"+ (numero*9) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 10 +"</div><div>=</div><div>"+ (numero*10) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 11 +"</div><div>=</div><div>"+ (numero*11) +"</div>"+
    "<div>"+ numero +"</div><div>x</div><div>"+ 12 +"</div><div>=</div><div>"+ (numero*12) +"</div>")
    
} else {
    var sol = "<div class='mal'>No es un número Entero</div>"
}
document.getElementById("table").innerHTML = sol
}
