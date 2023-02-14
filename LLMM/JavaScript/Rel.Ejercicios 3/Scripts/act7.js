function imprimir(input, fill){
    console.log(input.value)
    console.log(fill.value)
    var relleno = fill.value
    var numero = input.value
    let div = document.getElementById("mostrar")
    input.value
    var numero = numero - 1
    var filas = 0
    var respuesta = relleno
    console.log(respuesta)
    while (filas != numero){
    var added = " " + relleno 
    var respuesta = respuesta + added 
    filas += 1
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}