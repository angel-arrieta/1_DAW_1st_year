var pruebas = "Hola y adios";
function Busca(){
respuesta = "Lugar de la primera a: " + pruebas.indexOf("a") + " <br> Lugar de la última a: " + pruebas.lastIndexOf("a")
document.getElementById("mostrar").innerHTML = respuesta
}