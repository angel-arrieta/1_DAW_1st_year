function texto(name){
    if(/[^ÁÉÍÓÚáéíóú\w\s]/g.test(name.value) == true || /\d/g.test(name.value) == true ){
        var nombrado = "No se permiten caracteres especiales ni digitos"
    }else if(name.value == ""){
        var nombrado = "Rellene el cuadro"
    }else{ var nombrado = null }
    document.getElementById("nomcomp").innerHTML = nombrado
} function numeros(anos){
    if(anos.value == ""){
        var tiempo = "Introduzca su edad"
    }else if(anos.value < 0 || anos.value == 0){
        var tiempo = "Introduzca una edad valida"
    }else{ var tiempo = null} 
    document.getElementById("edadcomp").innerHTML = tiempo
} function correo(mail){
    if(/.@/g.test(mail.value) == true){
        if (/\..+$/g.test(mail.value) == true){ var email = null }
        else{ var email = "Dominio no detectado" }}
    else{ var email = "No se detecta ningun correo" }
    document.getElementById("mailcomp").innerHTML = email
} function fechado(giv_date){
    if(giv_date.value == ""){
        var fechar = "Introduzca una fecha"
    }else{ var fechar = null }
    document.getElementById("fechacomp").innerHTML = fechar
} function opciones(opcion){
    if(opcion.value == "ninguno" || opcion.value == ""){
        var preferencias = "Escoge alguna opcion"
    }else{ var preferencias = null }
    document.getElementById("prefercomp").innerHTML = preferencias
} function radio(){
    var uno = document.getElementById("uno").checked
    var dos = document.getElementById("dos").checked
    var tres = document.getElementById("tres").checked
    var buleano = [uno,dos,tres]
    var verdad = 0
    for (num in buleano) { if (buleano[num] == true){ verdad += 1 } }
    if (verdad == 0){
        var radios = "Escoge alguna opción"
    } else{ var radios = null } 
    document.getElementById("radiocomp").innerHTML = radios
} function comprobacion(){ // (nombre, edad, mail, fecha, prefer)
    var nombrado = document.getElementById("nomcomp").innerHTML
    var tiempo = document.getElementById("edadcomp").innerHTML
    var email = document.getElementById("mailcomp").innerHTML
    var fechar = document.getElementById("fechacomp").innerHTML
    var preferencias = document.getElementById("prefercomp").innerHTML
    var radios = document.getElementById("radiocomp").innerHTML
    var correcto = [nombrado, tiempo, email, fechar, preferencias, radios]
    console.log(correcto)
    for (comp in correcto){
        if (correcto[comp] != ""){
            response = "Arregle los campos inadecuados (siga las instrucciones en rojo)"
            break
        } else { response = "<div class='good'>Suscripción enviada correctamente</div>" }
    } document.getElementById("completo").innerHTML = response }