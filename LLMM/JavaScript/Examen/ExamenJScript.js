function valid(nume, numdos){
    nume = String(nume)
    numdos = String(numdos)
    return (nume.includes(".") == true || numdos.includes(".") == true)
}

function suma(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = (prime + seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function resta(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = (prime - seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function multiplica(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = (prime * seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function divide(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = (prime / seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function expone(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = (prime ** seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function porciento(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = ((prime / 100) * seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function raizcua(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = Math.sqrt(prime) + " / " + Math.sqrt(seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}
function expon(prime, seco){
    prime = Number(prime.value)
    seco = Number(seco.value)
    if (valid(prime, seco) == false){
    document.getElementById("res").innerHTML = Math.pow(prime, seco)
    } else if  (valid(prime, seco) == true){
    document.getElementById("res").innerHTML = "Must be Integer"
    }
}

