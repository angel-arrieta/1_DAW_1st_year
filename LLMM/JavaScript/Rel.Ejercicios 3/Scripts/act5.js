function escalera(input){
    console.log(input.value)
    var max = input.value
    console.log(max)
    var max = max - 1
    console.log(max)
    let div = document.getElementById("mostrar")
    input.value
    var filas = 0
    var respuesta = "* <br>"
    var anterior = "*"
    while (filas != max){
    var nivel = "*" + anterior + "*" 
    var anterior = nivel
    filas += 1
    console.log(nivel)
    var respuesta = respuesta + nivel + "<br>"
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}