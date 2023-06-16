function nombrar(nombre){
    console.log(nombre.value)
    if (nombre.value.length >= 3){
        if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(nombre.value) == true || /\d/g.test(nombre.value) == true ){
            var respuesta = "No se permiten caracteres especiales ni digitos"
        }else if(nombre.value == ""){
            var respuesta = "Rellene el cuadro"
        }else{ var respuesta = "Correcto" }
    } else {  var respuesta = "Nombre demasiado corto (mínimo 3 char.)" }
    console.log(respuesta)
    document.getElementById("nomcomp").innerHTML = respuesta
}
function apellidar(apellido){
    console.log(apellido.value)
    if (apellido.value.length >= 4){
        if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(apellido.value) == true || /\d/g.test(apellido.value) == true ){
            var respuesta = "No se permiten caracteres especiales ni digitos"
        }else if(apellido.value == ""){
            var respuesta = "Rellene el cuadro"
        }else{ var respuesta = "Correcto" }
    } else {  var respuesta = "Apellido demasiado corto (mínimo 4 char.)" }
    console.log(respuesta)
    document.getElementById("apecomp").innerHTML = respuesta
}
function telefono(numero){
    console.log(numero.value)
    if (/\D/g.test(numero.value) == true){
        var telefono = "Caracteres no númericos detectados"
    } else { if (/^[6789]/g.test(numero.value) == true){
            var telefono = "Correcto"
        }else{ var telefono = "Extension telefónica no reconocida" } }
    console.log(telefono)
    document.getElementById("telfcomp").innerHTML = telefono
}
function correo(mail){
    console.log(mail.value)
    if(/.@/g.test(mail.value) == true){
        if (/\..+$/g.test(mail.value) == true){ var email = "Correcto" }
        else{ var email = "Dominio no detectado" }}
    else{ var email = "No se detecta ningun correo" }
    console.log(email)
    document.getElementById("mailcomp").innerHTML = email
}
function comprobar(){
    var nomco = (document.getElementById("nomcomp").innerHTML)
    var apeco = (document.getElementById("apecomp").innerHTML)
    var numco = (document.getElementById("telfcomp").innerHTML)
    var mailco = (document.getElementById("mailcomp").innerHTML)
    mirar = [nomco, apeco, numco, mailco]
    console.log(mirar)
    respuesta = "Datos Correctos"
    for (x in mirar){
        if (mirar[x] != "Correcto"){
            respuesta = "Datos Mal introducidos"
            break }
    } console.log(respuesta)
    document.getElementById("finalcomp").innerHTML = respuesta
}
function anadir(nombrado, apellidado, numerado, mailed){
    var comprobacion = (document.getElementById("finalcomp").innerHTML)
    nombrado = (nombrado.value).toLocaleUpperCase()
    apellidado = (apellidado.value).toLocaleUpperCase()
    console.log(comprobacion)
    if(comprobacion != "Datos Correctos"){}else if(comprobacion == "Datos Correctos"){
        var colocar = '<tr class="filas">'+
                            '<td>'+ nombrado +'</td>'+
                            '<td>'+ apellidado +'</td>'+
                            '<td>'+ numerado.value +'</td>'+
                            '<td>'+ mailed.value +'</td>'+
                            '</tr>'
        var actual = document.getElementById("agenda").innerHTML
        anadido = actual + colocar
        console.log(anadido)
        document.getElementById("finalcomp").innerHTML = "Datos Ya Añadidos"
    } else {
        document.getElementById("finalcomp").innerHTML = "Datos Mal Introducidos"
    }
}
function listar(){
    var puesto = (document.getElementById("finalcomp").innerHTML)
    console.log(puesto)
    console.log(anadido)
    if(puesto != "Datos Ya Añadidos"){}else if(puesto == "Datos Ya Añadidos"){
        document.getElementById("agenda").innerHTML = anadido
    }
}
function Limp_Pant(){
    document.getElementById("agenda").innerHTML = '<tr class="primerafila">' +
    '<td>Nombre</td>' + '<td>Apellido</td>' + '<td>Número</td>' + '<td>Email</td>' + '</tr>'
}