function calcular(input){
    var nota = input.value
    console.log(nota)
    let div = document.getElementById("mostrar")
    if (nota < 0){
        var literal = " "
    } else if (nota < 5){
        var literal = "Suspenso"
    } else if (nota == 5){
        var literal = "Aprobado"
    } else if (nota == 6){
        var literal = "Bien"
    } else if (nota == 7 || nota == 8){
        var literal = "Notable"
    } else if (nota == 9 || nota == 10){
        var literal = "Sobresaliente"
    } else if (nota > 10){
        var literal = " "
    }
    div.innerHTML = literal
}