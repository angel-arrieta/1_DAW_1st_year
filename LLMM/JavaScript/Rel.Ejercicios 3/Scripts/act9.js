function rectangle(width, height){
    let div = document.getElementById("mostrar")
    var ancho = Number(width.value)
    var alto = Number(height.value)
    console.log(typeof(ancho))
    console.log(typeof(alto))
    var tapas = "# ​ ​"
    var relleno = "# ​ ​"
    var iter = 1
    while (iter != ancho){
        if (iter == (ancho - 1)){
            var tapas = tapas + "#"
            var relleno = relleno + "#"
        }else{
            var tapas = tapas + "# ​ ​"
            var relleno = relleno + "​ ​ ​ ​ ​"
        }
        iter += 1
    }
    var relleno = relleno + "<br>"
    var respuesta = tapas + "<br>"
    console.log(tapas)
    console.log(relleno)
    var iter = 1
    while (iter != alto){
        if (iter == (alto - 1)){
            var respuesta = respuesta + tapas
        }else{
            var respuesta = respuesta + relleno
        }
        iter += 1
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}