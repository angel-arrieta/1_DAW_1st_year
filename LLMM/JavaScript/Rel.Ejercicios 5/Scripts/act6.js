function Nombrar(name, ape1, ape2){
var comprueba = [name.value, ape1.value, ape2.value]
for (i in comprueba){
    if (/[\W\d]/g.test(comprueba[i]) == true){
        if (/[ÁÄÉËÍÏÓÖÚÜÑáäéëíïóöúüñ]/g.test(comprueba[i]) == true){
            comprueba[i] = comprueba[i].replace(/(Á|Ä)/g, "A")
            comprueba[i] = comprueba[i].replace(/(É|Ë)/g, "E")
            comprueba[i] = comprueba[i].replace(/(í|Ï)/g, "I")
            comprueba[i] = comprueba[i].replace(/(Ó|Ö)/g, "O")
            comprueba[i] = comprueba[i].replace(/(Ú|Ü)/g, "U")
            comprueba[i] = comprueba[i].replace(/(á|ä)/g, "a")
            comprueba[i] = comprueba[i].replace(/(é|ë)/g, "e")
            comprueba[i] = comprueba[i].replace(/(í|ï)/g, "i")
            comprueba[i] = comprueba[i].replace(/(ó|ö)/g, "o")
            comprueba[i] = comprueba[i].replace(/(ú|ü)/g, "u")
        } else {
            resultado = "Carácteres no permitidos encontrados"
            break
        }
    }
    comprueba[i] = comprueba[i].replace(/Ñ/g, "N")
    comprueba[i] = comprueba[i].replace(/ñ/g, "n")
    resultado = comprueba[1] + " " + comprueba[2] + ", " + comprueba[0]
}
document.getElementById("mostrar").innerHTML = resultado
}