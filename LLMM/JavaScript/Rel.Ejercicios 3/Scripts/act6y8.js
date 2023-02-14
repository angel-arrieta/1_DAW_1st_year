function escalera(input, fill){
    console.log(input.value)
    console.log(fill.value)
    var relleno = fill.value
    var max = input.value
    console.log(max)
    console.log(relleno)
    var max = max - 1
    console.log(max)
    let div = document.getElementById("mostrar")
    input.value
    var filas = 0
    var respuesta = relleno + " <br>"
    var anterior = relleno
    while (filas != max){
    var nivel = relleno + anterior + relleno 
    var anterior = nivel
    filas += 1
    console.log(nivel)
    var respuesta = respuesta + nivel + "<br>"
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}