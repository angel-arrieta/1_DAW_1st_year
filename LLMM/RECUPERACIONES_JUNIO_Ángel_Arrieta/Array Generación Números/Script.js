function twentyRandoms(){
    var veinte_numeros = []
    var cantidad = 0
    while (cantidad < 20){
        veinte_numeros.push(Math.floor(Math.random() * 1000))
        cantidad ++
    }
    document.getElementById("response").innerHTML = veinte_numeros
}
function randomNumbers(pedido){
    var lista_numeros = []
    var cant = 0
    while (cant < pedido.value){
        lista_numeros.push(Math.floor(Math.random() * 1000))
        cant ++
    }
    console.log(cantidad)
    console.log(lista_numeros.length)
    console.log(lista_numeros)
    document.getElementById("response").innerHTML = lista_numeros
}