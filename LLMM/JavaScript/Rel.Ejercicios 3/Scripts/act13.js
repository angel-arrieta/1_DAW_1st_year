function prime (input){
    let div = document.getElementById("mostrar")
    var number = Number(input.value)
    var lilength = number - 2
    var lista = Array.from({length: lilength}, (_, i) => i + 2)
    console.log(lista)
    var respuesta =""
    for(dig in lista){
        console.log(dig)
        console.log(lista[dig])
        if (number % lista[dig] == 0){
            console.log(number % lista[dig])
            var respuesta = "No es un número primo"
            break
    } }
    console.log(respuesta)
    if (respuesta.match("primo") == null){
        var respuesta = "Es un número primo" }
    console.log(respuesta)
    div.innerHTML = respuesta
}