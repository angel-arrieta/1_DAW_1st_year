function bic(){
cadena = String(window.prompt("Introduzca una cadena de caracteres:"))
if (cadena.includes("0")|| cadena.includes("1")|| cadena.includes("2")|| cadena.includes("3")||
    cadena.includes("4")|| cadena.includes("5")|| cadena.includes("6")|| cadena.includes("7")||
    cadena.includes("8")|| cadena.includes("9")){
    respuesta = "Ha introducido valores invalidos (números)"
}
else{
    lower = cadena.toLowerCase()
    upper = cadena.toUpperCase()
    respuesta = (String(lower.valueOf()) + "<br>"+ String(upper.valueOf()))    
}
document.getElementById("mostrar").innerHTML = respuesta
}