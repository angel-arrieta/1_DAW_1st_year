function paridad(numero){
    let div = document.getElementById("mostrar")
    var number = Number(numero.value)
    if (number % 2 == 0){
        var respuesta = "False"
    } else {
        var respuesta = "True"
    } 
    console.log(respuesta)
    div.innerHTML = respuesta
}