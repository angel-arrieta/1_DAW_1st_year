function texto(escrito){
    if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(escrito.value) == true || /\d/g.test(escrito.value) == true ){
        var respuesta = "No se permiten caracteres especiales ni digitos"
    }else if(escrito.value == ""){
        var respuesta = "Rellene el cuadro"
    }else{ var respuesta = null }
    document.getElementById("textcomp").innerHTML = respuesta
}
function numeros(numb){
    if(numb.value == "") { var respuesta = "Introduzca un número"}
    else{ var respuesta = null} 
    document.getElementById("numcomp").innerHTML = respuesta
}
function codigo(serie){
    iden = parseInt(serie.value)
    var validos = [11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11100, 11110, 11120, 11130,
    11138, 11139, 11140, 11149, 11150, 11158, 11159, 11160, 11170, 11178, 11179, 11180, 11190, 11201, 11202, 11203, 11204, 11205,
    11206, 11207, 11300, 11310, 11311, 11312, 11313, 11314, 11315, 11316, 11320, 11330, 11339, 11340, 11349, 11350, 11351, 11360,
    11368, 11369, 11370, 11379, 11380, 11390, 11391, 11392, 11393, 11400, 11401, 11402, 11403, 11404, 11405, 11406, 11407, 11408,
    11500, 11510, 11518, 11519, 11520, 11530, 11540, 11549, 11550, 11560, 11570, 11579, 11580, 11590, 11591, 11592, 11593, 11594,
    11595, 11596, 11600, 11610, 11611, 11612, 11620, 11630, 11638, 11639, 11640, 11648, 11649, 11650, 11659, 11660, 11670, 11679,
    11680, 11687, 11688, 11689, 11690, 11691, 11692, 11693]
    if (iden == ""){ respuesta = "Rellene el cuadro"}
    else { if (validos.includes(iden) == false){
            respuesta = "Código Postal invalido"}
            else { respuesta = null} }
    document.getElementById("ubicomp").innerHTML = respuesta
}
function identificar(nie){
    console.log(nie.value)
    console.log(nie.value[0]-[7])
    var no_es = "Formato no reconocido"
    if (nie.value.length == 9){
        console.log(nie.value[8])
        if (/A-Z/.test(nie.value[8]) == true) {

        }
    }else{ var respuesta = no_es }
    document.getElementById("idcomp").innerHTML = respuesta
}
function correo(mail){
    if(/.@/g.test(mail.value) == true){
        if (/\..+$/g.test(mail.value) == true){ var email = null }
        else{ var email = "Dominio no detectado" }}
    else{ var email = "No se detecta ningun correo" }
    document.getElementById("mailcomp").innerHTML = email
}
function comprobacion(){
    var solo_texto = document.getElementById("textcomp").innerHTML
    var numeros = document.getElementById("numcomp").innerHTML
    var ubica = document.getElementById("ubicomp").innerHTML
    var dni = document.getElementById("idcomp").innerHTML
    var email = document.getElementById("mailcomp").innerHTML
    var correcto = [solo_texto, numeros, ubica, dni, email]
    console.log(correcto)
    for (comp in correcto){
        if (correcto[comp] != ""){
            response = "Arregle los campos inadecuados (siga las instrucciones en rojo)"
            break
        } else { response = "<div class='good'>Formulario enviado correctamente</div>" }
    } document.getElementById("completo").innerHTML = response }