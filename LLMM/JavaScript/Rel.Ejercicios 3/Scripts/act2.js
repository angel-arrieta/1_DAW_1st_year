let input = String(document.getElementById("mayuminu"))
function leer(input){
    console.log(input.value);
    let div = document.getElementById("show");
    var mayu = input.toUpperCase();
    var minu = input.toLowerCase();
    switch (input) {
        case input == mayu:
            div.innerHTML = "Todo esta en mayúsculas" 
            break
        case input == minu:
            div.innerHTML = "Todo esta en minúsculas"
            break
        case input != mayu && input != minu:
            div.innerHTML = "Hay tanto mayúsculas como minúsculas"
            break
    }; 
}