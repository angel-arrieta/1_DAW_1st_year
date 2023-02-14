function media(nota1, nota2, nota3){
    var nota1 = Number(nota1.value)
    var nota2 = Number(nota2.value)
    var nota3 = Number(nota3.value)
    let div = document.getElementById("mostrar")
    const notas = [nota1, nota2, nota3]
    const literal = ["primera", "segunda", "tercera"]
    var media = ((nota1 + nota2 + nota3) / 3)
    var y = Number(0)
    var recuperar = []
    var resultado = ""
    for (x in notas){
        if (notas[x] < 5) {
            recuperar.push(literal[x])
        }
    }
    if (recuperar.length > 0){
        var resultado = ""
        for (lit in recuperar){
            var resultado = resultado.concat("Debe recuperar la ", recuperar[lit], " evaluación. <br> ")
        }
    }else{
        var resultado = "Tienes una nota media de " + media
    }
    div.innerHTML = resultado
}