function factorizado(numero){
    let div = document.getElementById("mostrar")
    var number = Number(numero.value)
    var factores = Array.from({length: number}, (_, i) => i + 1)
    console.log(factores)
    var suelo = 1
    for (x in factores){
        var resultado = suelo * factores[x]
        var suelo = resultado
    }
    console.log(resultado)
    div.innerHTML = resultado
    }