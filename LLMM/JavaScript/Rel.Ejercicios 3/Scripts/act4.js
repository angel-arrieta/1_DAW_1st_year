let div = document.getElementById("mostrar")
function escalera(){
    var filas = 0
    var respuesta = "* <br>"
    var anterior = "*"
    while (filas != 4){
    var nivel = "*" + anterior + "*" 
    var anterior = nivel
    filas += 1
    console.log(nivel)
    var respuesta = respuesta + nivel + "<br>"
    }
    console.log(respuesta)
    return respuesta
};
div.innerHTML = escalera()