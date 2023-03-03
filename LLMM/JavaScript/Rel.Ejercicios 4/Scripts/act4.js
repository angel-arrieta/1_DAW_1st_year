function calculate(){
    var notas = [5, 7, 9]
    let div = document.getElementById("mostrar")
    var media = 0
    for (x in notas){
        media += notas[x]
    }
    media = media / 3
    var resultado = ("La nota media del alumno es: " + media)
    div.innerHTML = resultado
    }