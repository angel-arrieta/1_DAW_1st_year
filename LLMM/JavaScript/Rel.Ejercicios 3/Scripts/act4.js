function escalera(){
    let div = document.getElementById("mostrar")
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
    div.innerHTML = respuesta
}
