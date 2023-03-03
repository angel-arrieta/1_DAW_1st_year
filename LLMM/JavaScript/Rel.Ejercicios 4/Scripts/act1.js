function days(){
    let div = document.getElementById("mostrar")
    var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    var resultado = dias[0] + " " + dias[dias.length-1]
    console.log(resultado)
    div.innerHTML = resultado
    }