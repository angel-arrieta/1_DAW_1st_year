var imagenes = ["Imagenes/solar.png", "Imagenes/nebulosa.png", "Imagenes/vortice.png", "Imagenes/stardust.png"];
var marcos = [ 5, 5, 5, 5];
var intervaloRuleta = [ null, null, null, null ];
var corriendo = 0;
var intervaloSombras;
var posicionSombras = [[2,2], [-2,2], [-2,-2], [2,-2]];
var posicionActualSombra = 0;
var vida = 520;
var moonlord = 145000;
var sol = 0;
var nebules = 0;
var vortex = 0;
var star = 0;
var dano = 0;

function DamageCalculator(){    
    marcos.forEach(solar)
    marcos.forEach(nebula)
    marcos.forEach(vortice)
    marcos.forEach(stardust)
    if (sol == 2){
        dano += 6500
    }
    else if (sol == 3){
        dano += 7000
    }
    else if (sol == 4){
        dano += 7500
    }
    if (nebules == 2){
        dano += 6000
    }
    else if (nebules == 3){
        dano += 6500
    }
    else if (nebules == 4){
        dano += 7000
    }
    if (vortex == 2){
        dano += 5500
    }
    else if (vortex == 3){
        dano += 6000
    }
    else if (vortex == 4){
        dano += 6500
    }
    if (star == 2){
        dano += 5000
    }
    else if (star == 3){
        dano += 5500
    }
    else if (star == 4){
        dano += 6000
    }
    if (star == 1 && sol == 1 && nebules == 1 && vortex == 1 ){
        dano += 6500
    }
    console.log(sol, nebules, vortex, star)
    return dano
}

function solar(image){
    if (image == 0){
        sol += 1
    }
}
function nebula(image){
    if (image == 1){
        nebules += 1
    }
}
function vortice(image){
    if (image == 2){
        vortex += 1
    }
}
function stardust(image){
    if (image == 3){
        star += 1
    }
}

function ruleta() {
    if (corriendo <= 0) {
        if (vida <= 0){
            document.getElementById("publico").innerHTML = "Desacansa En Paz..."
            document.getElementById("dano").innerHTML = NaN
            document.getElementById("advertencia").innerHTML = "Has Muerto..."
            document.getElementById("estadojefe").innerHTML = "El Moon Lord <br> Acabo Con Tu Vida"
            corriendo = 0
            vida = -5
        } else {
            clearInterval(intervaloSombras);
            dano = DamageCalculator();
            moonlord -= dano;
            vida -= 20
            document.getElementById("dano").innerHTML = "*Has hecho " + dano + " de daño*"

            for(i in marcos)
                marcos[i] = Math.floor(Math.random() * 4);
            
                intervaloRuleta[0] = setInterval(function() { cambiaImagen(0);}, 150);
                intervaloRuleta[1] = setInterval(function() { cambiaImagen(1);}, 150);
                intervaloRuleta[2] = setInterval(function() { cambiaImagen(2);}, 150);
                intervaloRuleta[3] = setInterval(function() { cambiaImagen(3);}, 150);

                console.log("daño "+dano)
                corriendo = 4;
                dano = 0;
                sol = 0;
                nebules = 0;
                vortex = 0;
                star = 0;
        }
    }
    console.log("vida "+vida)
    console.log("boss "+moonlord)
    document.getElementById("lord").innerHTML = moonlord
    document.getElementById("mivida").innerHTML = vida
    
}

function cambiaImagen(x) {
    if (marcos[x]>=3) marcos[x]=0
    else marcos[x] = marcos[x]+1
    document.getElementById("imag"+x).src = imagenes[marcos[x]]
}
            
function paraRuleta() {
    if (corriendo > 0) {
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        
        if (corriendo == 0 || corriendo < 0) {cambiaSombras()} 
    }
    console.log("corriendo "+corriendo)
}

function paraRuleta2() {
    if (corriendo > 0) {
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        
        if (corriendo == 0 || corriendo < 0) {cambiaSombras()} 
    }
    console.log("corriendo "+corriendo)
}

function pararTodo() {
    if (corriendo > 0) {
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        corriendo = corriendo - 1;
        clearInterval(intervaloRuleta[corriendo]);
        
        if (corriendo <= 0) {cambiaSombras()} 
    }
    console.log("corriendo "+corriendo)
}
            
function cambiaSombras() {
    intervaloSombras=setInterval(circulaSombras, 100);
}
            
            
function circulaSombras() {
    if(posicionActualSombra>=3) posicionActualSombra=0;
        else posicionActualSombra=posicionActualSombra+1;
    
    var estilo = posicionSombras[posicionActualSombra][0]+"px "+posicionSombras[posicionActualSombra][1]+"px 5px #FF5050";
    document.getElementById("imag0").style['boxShadow']=estilo;
    document.getElementById("imag1").style['boxShadow']=estilo;
    document.getElementById("imag2").style['boxShadow']=estilo;
    document.getElementById("imag3").style['boxShadow']=estilo;
}