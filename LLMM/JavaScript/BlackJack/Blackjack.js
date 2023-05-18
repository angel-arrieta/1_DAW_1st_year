var baraja = ["AC", "AD", "AH", "AS", "2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S", "5C", "5D", "5H", "5S",
"6C", "6D", "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S",
"10C", "10D", "10H", "10S", "JC", "JD", "JH", "JS", "QC", "QD", "QH", "QS", "KC", "KD", "KH", "KS"]
var dinero = 490
var apostado = 10
var tu_mano = []
var show_mano = []
var mano_2 = []
var show_segundo = []
var crupier = []
var show_crupier = []
var jugando = 0
var funcionar = 0
var explica = "Para ganar has de acercarte a 21, la J,Q y K valen 10, y los As pueden valer 1 u 11, " +
                "dependidendo de cual te convenga, si con 2 cartas sumas 21, haces Blackjack y ganas. " +
                "<br> Si te pasas de 21 pierdes, pero si sacas mas que el crupier sin pasarte de 21, ganas."
function show(mano){
    visible = []
    for (carta in mano){
        visible.push( "<img class='cartas' src='Cartas/"+mano[carta]+".png'>")
    }
    return visible
}
function hide(mano){
    escondido = []
    for (carta in mano){
        if (carta == 0){
            escondido.push( "<img class='cartas' src='Cartas/"+mano[carta]+".png'>")
        } else {
        escondido.push( "<img class='cartas' src='Cartas/reverso.png'>")
        }
    }
    return escondido
}
function mas(){
    if (jugando == 0){
        dinero -= 10
        apostado += 10
        document.getElementById("apostado").innerHTML = apostado
        document.getElementById("dinero").innerHTML = dinero
    } else if (jugando == 1){
        
    }
}
function inicia(){
    document.getElementById("explica").innerHTML = explica + " <br> Primero haz tu apuesta, luego incia el juego."
    document.getElementById("terminado").innerHTML = '<div class="boton" type="button" id="repetir" onclick="inicio()">Empezar<br>Partida</div>'
    document.getElementById("apostado").innerHTML = apostado
    document.getElementById("dinero").innerHTML = dinero
}
function devolver(mano){
    for (carta in mano){
        baraja = baraja.concat(mano[carta])
    }
    return []
}
function dar_car(mano){
    posicion = Math.floor(Math.random() * (baraja.length-1))
    mano.push(baraja.splice((posicion), 1))
}
function inicio (){
    if (apostado == 0){ } else {
        jugando = 1
        funcionar = 1
        document.getElementById("terminado").innerHTML = ""
        dar_car(tu_mano)
        dar_car(tu_mano)
        show_mano = show(tu_mano)
        dar_car(crupier)
        dar_car(crupier)
        show_crupier = hide(crupier)
        console.log(tu_mano)
        console.log(crupier)
        document.getElementById("jugador").innerHTML = show_mano
        document.getElementById("crupier").innerHTML = show_crupier
        document.getElementById("explica").innerHTML = explica
        if (tu_mano.length == 2 && calcular(tu_mano) == 21) {
            ganaste()
            final = explica + "<br> ¡BLACKJACK! (Has Ganado)"
            document.getElementById("terminado").innerHTML = '<div class="boton" type="button" id="repetir" onclick="otra_partida()">Seguir<br>Jugando</div>'
            document.getElementById("explica").innerHTML = final
            document.getElementById("apostado").innerHTML = apostado
            document.getElementById("dinero").innerHTML = dinero
            document.getElementById("crupier").innerHTML = show_crupier
        }
    }
}
function otra_partida(){
    show_mano = []
    show_crupier = []
    show_segundo = []
    mano_2 = devolver(mano_2)
    tu_mano = devolver(tu_mano)
    crupier = devolver(crupier)
    document.getElementById("jugador").innerHTML = show_mano
    document.getElementById("crupier").innerHTML = show_crupier
    document.getElementById("doblado").innerHTML = ""
    jugando = 0
    inicia()
}
function pedir(){
    if (funcionar == 0){ } else if (funcionar == 1){
        dar_car(tu_mano)
        show_mano = show(tu_mano)
        document.getElementById("jugador").innerHTML = show_mano
        if (calcular(tu_mano) > 21){
            pasar(mano)
        }
        
    }
}
function pedir2(){
    if (funcionar == 0){ } else if (funcionar == 1){
        dar_car(mano_2)
        show_segundo = show(mano_2)
        document.getElementById("jugador").innerHTML = show_mano
        if (calcular(mano_2) > 21){
            pasar(mano)
        }
        
    }
}
function rendirse(){
    if (funcionar == 0){ } else if (funcionar == 1){
        final = explica + "<br> Te has rendido"
        funcionar = 0
        dinero += (apostado/2)
        apostado = 0
        show_crupier = show(crupier)
        document.getElementById("explica").innerHTML = final
        document.getElementById("apostado").innerHTML = apostado
        document.getElementById("dinero").innerHTML = dinero
        document.getElementById("crupier").innerHTML = show_crupier
        document.getElementById("terminado").innerHTML = '<div class="boton" type="button" id="repetir" onclick="otra_partida()">Jugar<br>Otra</div>'
    }
}
function calcular(mano) {
    cantidades = []
    sumando = 0
    adaptar = []
    for (carta in mano){
        card = mano[carta].toString()
        cantidades.push(card.substring(0, card.length-1))
    }
    for (nume in cantidades){
        if (cantidades[nume] == "J" || cantidades[nume] == "Q" || cantidades[nume] == "K"){
                sumando += 10
        } else if (cantidades[nume] == "A") {
            adaptar.push(cantidades[nume])
        } else {
            sumando += parseInt(cantidades[nume])
        }
    }
    if (adaptar.length > 0){
        if (adaptar.length == 1){   
            if (sumando <= 10){
                sumando += 11
            } else {
                sumando += 1
            }
        } else if (adaptar.length > 1){
            for (carta in adaptar){
                sumando += 1
            }
        }
    }
    return sumando
}
function doblar(){
    if (funcionar == 0){ } else if (funcionar == 1){
        if (tu_mano.length == 2 && (calcular(tu_mano) == 9 || calcular(tu_mano) == 10 || calcular(tu_mano) == 11)){
            dar_car(tu_mano)
            show_mano = show(tu_mano)
            dinero -= apostado
            apostado = (apostado*2)
            document.getElementById("jugador").innerHTML = show_mano
            if (calcular(tu_mano) > 21){
                pasar()
            }
        } else { }
    }
}
function seguro(){
    if (funcionar == 0){ } else if (funcionar == 1){
        if (crupier[0].toString()[0] == "A" ){
            dinero -= (apostado/2)
            apostado += (apostado/2)
            if (calcular(crupier) == 21){
                final = explica + "<br> !Has ganado¡"
                ganaste()
            }else{
                final = explica + "<br> Perdiste"
                apostado = 0  
            }
            funcionar = 0
            funcionar = 0
            show_crupier = show(crupier)
            document.getElementById("explica").innerHTML = final
            document.getElementById("crupier").innerHTML = show_crupier
            document.getElementById("terminado").innerHTML = '<div class="boton" type="button" id="repetir" onclick="otra_partida()">Jugar<br>Otra</div>'
        }
        document.getElementById("apostado").innerHTML = apostado
        document.getElementById("dinero").innerHTML = dinero
    }
}
function dividir(){
if (funcionar == 0){ } else if (funcionar == 1){
if (tu_mano.length == 2){
compara = []
for (carta in tu_mano){
    card = mano[carta].toString()
    compara.push(card.substring(0, card.length-1))
}
if (compara[0].substring(0, card.length-1) == compara[1].substring(0, card.length-1)){
    document.getElementById("doblado").innerHTML = 'Segunda mano <div id="segundo"></div>'
    document.getElementById("extra").innerHTML = '<div class="boton" type="button" id="pedir2" onclick="pedir2()">Pedir Carta</div>'+
                                                    '<div> Dividido: <div id="dividido"> </div> </div>'
    document.getElementById("apostado").innerHTML = (apostado/2)
    document.getElementById("dividido").innerHTML = (apostado/2)
} else{ }  
} else { }
}
}
function escoger(cantidad){
    if (cantidad <= 10){
        coger = "si"
    } else if (10 < cantidad < 15){
        azar = Math.round(Math.random())
        if (azar == 0){
            coger = "no"
        } else if (azar == 1){
            coger = "si"
        }
    } else if (cantidad >= 16){
        coger = "no"
    }
    console.log(coger)
    return coger
}
function pasar(){
    crupi = calcular(crupier)
    robar = escoger(crupi)
    if (robar == "si"){
        dar_car(crupier)
        show_crupier = hide(crupier)
    } else if (robar == "no"){

    }
    document.getElementById("crupier").innerHTML = show_crupier
}
function ganaste(){
    dinero += (apostado*2)
    apostado = 0
}
function plantarse(){
    if (funcionar == 0){ } else if (funcionar == 1){
            jugador = calcular(tu_mano)
            rival = calcular(crupier)
            if (mano_2.length != 0){
                jugada_2 = calcular(mano_2)
            }
        if (jugador > 21 ){
            final = explica + "<br> Perdiste"
            apostado = 0
        } else if (jugador == 21) {
            if (jugador == rival) {
                final = explica + "<br> Has empatado, juega de nuevo"
                dinero += apostado
                apostado = 0
            } else {
                final = explica + "<br> !Has ganado¡"
                ganaste()
            }
        } else if (jugador < 21){
            if (rival < 21){
                if (jugador == rival) {
                    final = explica + "<br> Has empatado, juega de nuevo"
                    dinero += apostado
                    apostado = 0
                } else if (jugador > rival){
                    final = explica + "<br> !Has ganado¡"
                    ganaste()
                } else if (jugador < rival){
                    final = explica + "<br> Perdiste"
                    apostado = 0
                }
            } else if (rival > 21){
                final = explica + "<br> !Has ganado¡"
                ganaste()
            } 
        }
        funcionar = 0
        show_crupier = show(crupier)
        document.getElementById("explica").innerHTML = final
        document.getElementById("apostado").innerHTML = apostado
        document.getElementById("dinero").innerHTML = dinero
        document.getElementById("crupier").innerHTML = show_crupier
        document.getElementById("terminado").innerHTML = '<div class="boton" type="button" id="repetir" onclick="otra_partida()">Jugar<br>Otra</div>'
    }
}