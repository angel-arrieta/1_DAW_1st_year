function espacio(char){
    return char == " "
}
function leer(input){
    var texto = input.value
    console.log(texto)
    let div = document.getElementById("mostrar")
    var chain = texto.split("")
    console.log(chain)
    var response = chain.find(espacio)
    console.log(response)
    div.innerHTML = (response == " ") ? "Tiene espacios" : "No tiene espacios"
}