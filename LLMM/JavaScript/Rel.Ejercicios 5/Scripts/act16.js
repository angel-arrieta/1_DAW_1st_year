function mail(){
var cadena = String(window.prompt("Introduzca su correo electrónico: "))
var usuario = cadena.split(/@/)[0]
var dominio = cadena.split(/@/)[1]
respuesta = "Dirección del usuario: " + usuario + "<br>Dominio de la dirección: " + dominio
document.getElementById("mostrar").innerHTML = respuesta
}