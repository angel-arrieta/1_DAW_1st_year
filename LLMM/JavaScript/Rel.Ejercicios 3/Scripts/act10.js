function ordena_limites(ini, fin){
    let div = document.getElementById("mostrar")
    var start = Number(ini.value)
    var end = Number(fin.value)
    if(start < end){
        var respuesta = "Límites ya ordenados: " + start + " < " + end
    }else{
        var nstart = end
        var nend = start
        var respuesta = "Límites reordenados: " + nstart + " < " + nend
    }
    console.log(respuesta)
    div.innerHTML = respuesta
}