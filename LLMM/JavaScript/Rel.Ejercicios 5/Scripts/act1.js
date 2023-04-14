function numerico(input){
    numer = (isNaN(input.value) == true) ? "No es un número" : "Es un número"
    if (isNaN(input.value) == true){
        pari = ""
    } else {
        pari = (input.value % 2 == 0) ? ", y es par" : ", y no es par"
    }
    document.getElementById("mostrar").innerHTML = numer + pari
}