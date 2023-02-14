function prime_range (input){
    let div = document.getElementById("mostrar")
    var strnums = String(input.value)
    var numarray = strnums.split(",")
    console.log(numarray)
    var respuesta = ""
    for (n in numarray){
        var number = Number(numarray[n])
        var lilength = number - 2
        var lista = Array.from({length: lilength}, (_, i) => i + 2)
        // console.log(lista)
        var response =""
        for(dig in lista){
            // console.log(dig)
            // console.log(lista[dig])
            if (number % lista[dig] == 0){
                // console.log(number % lista[dig])
                var response = number + " no es un número primo"
                break
        } }
        // console.log(respuesta)
        if (response.match("primo") == null){
            var response = number + " es un número primo" }
        var respuesta = respuesta.concat(response, "<br>")
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}