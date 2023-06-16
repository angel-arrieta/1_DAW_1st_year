function evaluar(){
    var recuperar = []
    var suma_fol = parseInt(document.getElementById("fol1").value) + parseInt(document.getElementById("fol2").value) + parseInt(document.getElementById("fol3").value)
    var suma_sist = parseInt(document.getElementById("ssii1").value) + parseInt(document.getElementById("ssii2").value) + parseInt(document.getElementById("ssii3").value)
    var suma_edes = parseInt(document.getElementById("edes1").value) + parseInt(document.getElementById("edes2").value) + parseInt(document.getElementById("edes3").value)
    var suma_prog = parseInt(document.getElementById("prog1").value) + parseInt(document.getElementById("prog2").value) + parseInt(document.getElementById("prog3").value)
    var suma_lmar = parseInt(document.getElementById("llmm1").value) + parseInt(document.getElementById("llmm2").value) + parseInt(document.getElementById("llmm3").value)
    var suma_bdat = parseInt(document.getElementById("bbdd1").value) + parseInt(document.getElementById("bbdd2").value) + parseInt(document.getElementById("bbdd3").value)
    media_fol = Math.floor(suma_fol/3)
    document.getElementById("Fol").innerHTML = media_fol
    media_sist = Math.floor(suma_sist/3)
    document.getElementById("Ssii").innerHTML = media_sist
    media_edes = Math.floor(suma_edes/3)
    document.getElementById("Edes").innerHTML = media_edes
    media_prog = Math.floor(suma_prog/3)
    document.getElementById("Prog").innerHTML = media_prog
    media_lmar = Math.floor(suma_lmar/3)
    document.getElementById("Llmm").innerHTML = media_lmar
    media_bdat = Math.floor(suma_bdat/3)
    document.getElementById("Bbdd").innerHTML = media_bdat
    if (media_fol < 5){
        recuperar.push("Fol")
    } if (media_sist < 5){
        recuperar.push("Sistemas Informáticos")
    } if (media_edes < 5){
        recuperar.push("Entornos de Desarrollo")
    } if (media_prog < 5){
        recuperar.push("Programación")
    } if (media_lmar < 5){
        recuperar.push("Lenguaje de Marca")
    } if (media_bdat < 5){
        recuperar.push("Base de Datos")
    } if (recuperar.length > 0){
        var respuesta = "Tienes que recuperar: "
        recuperar.forEach(asignatura => respuesta += (asignatura +", "))
    } else {
        var respuesta = "¡Has aprobado todo!"
    } document.getElementById("response").innerHTML = respuesta
    
}
