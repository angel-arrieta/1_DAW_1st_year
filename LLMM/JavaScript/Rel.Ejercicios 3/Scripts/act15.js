function potenciado (base, power){
    let div = document.getElementById("mostrar")
    var base = Number(base.value)
    var power = Number(power.value)
    var potenciadores = Array.from({length: power}, (_, i) => i + 1)
    var suelo = 1
    var resultado = 0
    for (x in potenciadores){
        var resultado = suelo * base
        var suelo = resultado
    }
    console.log(resultado)
    div.innerHTML = resultado
    }