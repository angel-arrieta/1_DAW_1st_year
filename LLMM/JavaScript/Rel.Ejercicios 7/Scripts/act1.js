function comprobar(pri, sec, ter){
    var participantes = [pri.value, sec.value, ter.value]
    var excepciones = []
    console.log(excepciones.length)
    for (jugadores in participantes){
        if(/\W/g.test(participantes[jugadores]) == true){
            excepciones.push(participantes[jugadores] + " Tiene caracteres especiales no validos")
        }
    }
    if (excepciones.length > 0){
        var ocurrencias = ""
        for (ocu in excepciones){
            ocurrencias = ocurrencias.concat(excepciones[ocu])
            ocurrencias = ocurrencias.concat(" <br> ")
        }
    var comp_final = ocurrencias
    } else {
    var comp_final = "Jugadores registrados correctamente"
    }
    document.getElementById("mostrar").innerHTML = comp_final
}