function texto(id, texto){
    if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(texto.value) == true || /\d/g.test(texto.value) == true ){
        document.getElementById(id).innerHTML = "No se permiten caracteres especiales ni digitos"
    }else{
        document.getElementById(id).innerHTML = null
    }
}
function numero(id, numero){
    console.log(numero.value)
    console.log(numero.value.match(/\D/g))
    if(/\D/g.test(numero.value) == true){
        document.getElementById(id).innerHTML = "Solo se permiten números"
    }else{
        document.getElementById(id).innerHTML = null
    }
}
function nacimiento(fecha){
    var rnow = new Date();
    var ahora = [rnow.getFullYear(), rnow.getMonth()+1, rnow.getDate()]
    var fechado = fecha.value.split("-")
    for (dato in ahora){
        ahora[dato] = ahora[dato].toString()
    }
    for (dato in ahora){
        if(ahora[dato].length == 1){
            ahora[dato] = "0".concat(ahora[dato])
        }
    }
    ahora = parseInt(ahora.join(""))
    fechado = parseInt(fechado.join(""))
    if ((ahora - fechado) > 1000000) {
        response = "Edad no reconocida (mayor de 100 años)"
    } else if ((ahora - fechado) < 10000) {
        response = "Edad no reconocida (menor de 1 año)"
    } else {response = null}
    document.getElementById("fnaccomp").innerHTML = response
}