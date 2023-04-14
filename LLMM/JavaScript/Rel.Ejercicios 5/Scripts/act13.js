var dni = "12345678A";
function Separa(){
document.getElementById("mostrar").innerHTML = (dni.match(/\D/g)).join("")
}