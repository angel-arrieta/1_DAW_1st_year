function calcular(input){
    console.log(input.value)
    let div = document.getElementById("mostrar")
    div.innerHTML = (input.value % 2 == 0) ? "El número es par" : "El número es impar"
}