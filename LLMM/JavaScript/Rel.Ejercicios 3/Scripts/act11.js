function paridad(numero){
    let div = document.getElementById("mostrar")
    var number = Number(numero.value)
    if (number % 2 == 0){
        var respuesta = 1
    } else {
        var respuesta = 0
    } 
    console.log(respuesta)
    div.innerHTML = respuesta
}