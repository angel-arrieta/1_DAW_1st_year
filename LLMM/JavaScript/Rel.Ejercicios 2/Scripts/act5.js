function media(nota1, nota2, nota3){
    var nota1 = Number(nota1.value)
    var nota2 = Number(nota2.value)
    var nota3 = Number(nota3.value)
    let div = document.getElementById("mostrar")
    const notas = [nota1, nota2, nota3]
    const literal = ["primera", "segunda", "tercera"]
    var recuperar = []
    var suma = Number(0)
    var y = Number(0)
    for (var x in notas){
        if (Number(x) < 5) {
            recuperar.concat(literal[y])
        }
        console.log(suma)
        suma += x
        console.log(x)
        y += Number(1)
        console.log(suma)
        console.log(y)
    }
    console.log(suma)
    console.log(recuperar)
    if (recuperar == []){
        var resultado = "Su nota media es " + (suma/3)
    } else {
        var resultado = "Debe de recuperar la(s) evaluación(es): <br>"
        for (var lit in recuperar){
            resultado.concat("- ", lit, "<br>")
        }
    }
    console.log(resultado)
    div.innerHTML = resultado
}