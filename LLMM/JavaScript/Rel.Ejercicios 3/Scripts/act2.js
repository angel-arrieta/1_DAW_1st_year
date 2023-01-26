function leer(input){
    console.log(input.value)
    let div = document.getElementById("show")
    let chain = input.value
    let mayu = chain.toUpperCase()
    let minu = chain.toLowerCase()
    switch (chain) {
        case mayu:
            var response = "Todo esta en mayúsculas"
            break
        case minu:
            var response = "Todo esta en minúsculas"
            break
        default:
            var response = "Hay tanto mayúsculas como minúsculas"
            break
    };
    div.innerHTML = response
}