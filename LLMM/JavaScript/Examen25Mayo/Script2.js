var segu = 0;
var decsegu = 0;
var minu = 2;
function PaTras() { setInterval(tictac, 1000) }
function tictac(){
    if (segu == 0 && decsegu == 0 && minu == 0) { window.close() }
    if(segu>0) { segu -= 1 }
    else { if(decsegu>0) { decsegu -= 1 }
                else { if(minu>0) { minu -= 1 }
                            else { minu =  1} decsegu = 5} segu = 9}
    document.getElementById("min").src = "Contador/" + minu + ".png";
	document.getElementById("segu2").src = "Contador/" + decsegu + ".png";
	document.getElementById("segu").src = "Contador/" + segu + ".png";
}
function correo(mail){
    if(/.@/g.test(mail.value) == true){
        if (/\..+$/g.test(mail.value) == true){ var email = "Correcto" }
        else{ var email = "Dominio no detectado" }}
    else{ var email = "No se detecta ningun correo" }
    document.getElementById("mailcomp").innerHTML = email
}
function identificar(nie){
    console.log(nie.value.substring(0, 8))
    console.log(typeof nie.value.substring(0, 8))
    var no_es = "Formato DNI no reconocido"
    if (nie.value.length == 9){
        if (/[A-Z]/.test(nie.value[8]) == true) {
            if(/[\D]/g.test(nie.value.substring(0, 8)) == true ){
                var respuesta = no_es
            }else{ var respuesta = "Correcto" }
        }else{ var respuesta = no_es }
    }else{ var respuesta = no_es }
    document.getElementById("idcomp").innerHTML = respuesta
}
function texto(escrito){
    console.log(escrito.value.length)
    if (escrito.value.length >= 3){
        if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(escrito.value) == true || /\d/g.test(escrito.value) == true ){
            var respuesta = "No se permiten caracteres especiales ni digitos"
        }else if(escrito.value == ""){
            var respuesta = "Rellene el cuadro"
        }else{ var respuesta = "Correcto" }
    } else {  var respuesta = "Nombre demasiado corto (mínimo 3 char.)" }
    document.getElementById("textcomp").innerHTML = respuesta
}
function borra2(){
    document.getElementById("resultados").innerHTML = '<tr class="primerafila">'+
                                                            '<td>Nombre</td>'+
                                                            '<td>DNI</td>'+
                                                           '<td>Email</td>'+
                                                        '</tr>'
}
function comprobar2(){
    var nomco = (document.getElementById("textcomp").innerHTML)
    var idco = (document.getElementById("idcomp").innerHTML)
    var mailco = (document.getElementById("mailcomp").innerHTML)
    var mirar = [nomco, idco, mailco]
    respuesta = "Datos Guardados"
    for (x in mirar){
        if (mirar[x] != "Correcto"){
            respuesta = "Datos Mal introducidos"
            break }
    } document.getElementById("finalcomp").innerHTML = respuesta
}
function listar2(nombre, dni, correo){
    comprobar2()
    var proceder = document.getElementById("finalcomp").innerHTML
    console.log(proceder)
    if (proceder == "Datos Guardados"){
        var colocar = '<tr class="filas">'+
                            '<td>'+ (nombre.value).toLocaleUpperCase() +'</td>'+
                            '<td>'+ dni.value +'</td>'+
                            '<td>'+ correo.value +'</td>'+
                            '</tr>'
        var ya_hay = document.getElementById("resultados").innerHTML
        var anadido = ya_hay + colocar
        document.getElementById("resultados").innerHTML = anadido
    } else if (proceder == "Datos Mal introducidos" || proceder == null) {
        document.getElementById("finalcomp").innerHTML = "Datos Mal introducidos"
    }
}