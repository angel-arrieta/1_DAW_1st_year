function leer(input){
    var derecho = input.value
    var derecho = derecho.toLowerCase()
    var derecho = derecho.replaceAll(",","")
    var derecho = derecho.replaceAll(" ","")
    console.log(derecho)
    let div = document.getElementById("mostrar")

    var chain = derecho.split("")
    var chain = chain.reverse()
    var chain = chain.toString()
    var reversed = chain.replaceAll(",","")
    console.log(reversed)

    div.innerHTML = (derecho == reversed) ? "Es un palindromo" : "No es un palindromo"
}
    
