function texto(texto){
    console.log(texto.value)
    if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(texto.value) == true || /\d/g.test(texto.value) == true ){
        document.getElementById("nomcomp").innerHTML = "No se permiten caracteres especiales ni digitos"
    }else{
        document.getElementById("nomcomp").innerHTML = null
    }
}
function numero(numero){
    console.log(numero.value)
    if(/\D/g.test(numero.value) == true){
        document.getElementById("edadcomp").innerHTML = "Solo se permiten digitos"
    }else{
        document.getElementById("edadcomp").innerHTML = null
    }
}
function opciones(opcion){
    console.log(opcion.value)
    if(opcion.value == "ninguno" || opcion.value == ""){
        document.getElementById("intcomp").innerHTML = "Escoge alguna opcion"
    }else{
        document.getElementById("intcomp").innerHTML = null
    }
}
function completo(nombre, edad, interes){
    if (interes.value == "ninguno"){interes.value = ""}
    var compr = [nombre.value, edad.value, interes.value]
    console.log(compr)
    var esta = 0
    for (not in compr) { if (compr[not] == "") {esta += 1} }
    if (esta != 0){
        document.getElementById("completo").innerHTML = "Complete los campos vacíos"
    } else (
        document.getElementById("completo").innerHTML = "<div class='good'> Formulario enviado correctamente <div>"
    ) }