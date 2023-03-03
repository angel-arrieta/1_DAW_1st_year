var valores = [true, 5, false,"hola", "adios", 2]
function text(){
    let div = document.getElementById("textos")
    var textos = []
    for (x in valores){
        if ((typeof valores[x]) == "string"){
            textos = textos.concat(valores[x])
        }
    }
    for (x in textos){
        if (x == 0){
            continue
        }
        if ((textos[x-1]).length > (textos[x]).length){
            var resultado = "La palabra " + textos[x-1] + " es la más larga del array <br>"
        } else if ((textos[x-1]).length < (textos[x]).length){
            var resultado = "La palabra " + textos[x] + " es la más larga del array <br>"
        }
    }
    console.log(textos)
    div.innerHTML = resultado
    }
function math(){
    let div = document.getElementById("mates")
    var numeros = []
    for (x in valores){
        console.log(typeof valores[x])
        if ((typeof valores[x]) == "number"){
            numeros = numeros.concat(valores[x])
        }
    }
    var suma = numeros[0] + numeros[1]
    var resta = numeros[0] - numeros[1]
    var multi = numeros[0] * numeros[1]
    var divi = numeros[0] / numeros[1]
    var respuestas = (
        numeros[0] + " + " + numeros[1] + " = " + suma + "<br>" +
        numeros[0] + " - " + numeros[1] + " = " + resta + "<br>" +
        numeros[0] + " * " + numeros[1] + " = " + multi + "<br>" +
        numeros[0] + " / " + numeros[1] + " = " + divi + "<br>"
    )
    div.innerHTML = respuestas
    }