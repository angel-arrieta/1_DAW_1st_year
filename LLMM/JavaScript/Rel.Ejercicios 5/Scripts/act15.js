var dni = "12345678A";
function Separa(){
dni = dni.split("").reverse().join()
dni = dni.match(/\d/gi).join().replace(/,/gi, "")
document.getElementById("mostrar").innerHTML = dni.slice(0,4)
}