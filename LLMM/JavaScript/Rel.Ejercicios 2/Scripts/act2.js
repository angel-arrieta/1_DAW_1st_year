function calcular(input){
    var numero = input.value
    console.log(numero)
    let div = document.getElementById("mostrar")
    div.innerHTML = (numero%2 == 0) ? "Es par" : "Es impar"
}