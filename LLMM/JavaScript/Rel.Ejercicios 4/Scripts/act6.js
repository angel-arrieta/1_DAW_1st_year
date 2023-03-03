function days(){
    let div = document.getElementById("mostrar")
    var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    var resultado = (
        "Cantidad de elementos en el array: " + dias.length + "<br>" +
        "Extraemos el primer elemento: " + dias.shift() + "<br>" +
        "Cantidad actual de elementos en el array: " + dias.length + "<br>"
        )
        dias = dias.concat("Sunday")
    var extra = (
        "Añadimos 'Sunday' al final: " + dias + "<br>" +
        "Cantidad actual de elementos en el array: " + dias.length + "<br>" +
        "El array en sí (los días de la semana): " + dias
        )
        resultado = resultado + extra
    div.innerHTML = resultado
    }
function Lunes(dias){
    return dias == "Lunes"
}