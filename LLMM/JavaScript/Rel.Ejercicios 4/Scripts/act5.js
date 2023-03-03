function days(){
    let div = document.getElementById("mostrar")
    var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    var resultado = (
        "Los días de la semana: " + dias.join(", ") + "<br>" +
        "Los días de la semana al reves: " + dias.reverse() + "<br>" +
        "Los días de la semana ordenados alfabeticamente: " + dias.sort() + "<br>" +
        "La posición del Lunes en su array es la número: " + dias.findIndex(Lunes)
    )
    div.innerHTML = resultado
    }
function Lunes(dias){
    return dias == "Lunes"
}