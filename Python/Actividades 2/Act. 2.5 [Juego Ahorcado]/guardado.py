import random


def dame():
    diccionario = ["oklahoma", "ontario", "massachusetts", "misisipi", "madrid", "barcelona", "andalucia", "paisano",
                   "paisvasco", "euskalerria", "torremolinos", "honduras", "animado", "roma", "venecia", "cormoran",
                   "luxemburgo", "londres", "mesilla", "comoda", "armario", "escalera", "tejado", "cimientos",
                   "sillones", "frigorifico", "batidora", "cazuela", "sartenes", "espumadera", "pinzas", "harina",
                   "huevos", "rallador", "cuchillo", "instituto", "universidad", "carrera", "trabajo", "examenes",
                   "cuaderno", "libreria", "biblioteca", "panaderia", "industria", "chrome", "busqueda", "videojuego",
                   "perspectiva", "clasificacion", "memoria", "almacenamiento", "proceso", "altavoz", "cargador",
                   "deficit", "trastorno", "psicologo", "psiquiatra", "hospital", "emergencia", "doctor", "medico",
                   "celador", "enfermera", "intravenosa", "aguja", "sangre", "donacion", "altruismo", "solidaridad",
                   "amistad", "cercania", "trenes", "tranvia", "transporte", "alado", "sufrimiento", "rechazo",
                   "calefaccion", "television", "radiofonia", "alargadera", "regleta", "iluminacion", "estadio",
                   "ambulancia", "portatil", "tableta", "graficos", "mochila", "teclado", "suelo", "granja", "amarillo",
                   "rosado", "magenta", "verdoso", "dorado", "caoba", "olivar", "maizal", "trigal", "tigre", "elefante",
                   "hipopotamo", "ascensor", "banquero", "pescador", "ejecutivo", "militar", "programador", "rehacer",
                   "ahorcado", "linchamiento", "juicio", "juzgado", "juzgado", "almeria", "policia", "malaga", "cadiz",
                   "jurisdiccion", "huelva", "gaditano", "onuvense", "neoyorquino", "losangeles", "mexico", "mexicano",
                   "deportivo", "villareal", "futbol", "clubes", "baloncesto", "aguado", "llovizna", "geiser", "anillo",
                   "nubarron", "volcan", "torrente", "pelicula", "trescientos", "señor", "opera", "cineasta", "teclas",
                   "anfiteatro", "quesadilla", "gastronomia", "gastronomico", "empezamos", "almuerzo", "desayuno",
                   "alados", "doloridos", "pajaro", "gaviota", "cuervo", "ohio", "labrador", "calico", "gatito","viena",
                   "locura", "esceptico", "escepticismo", "cinico", "cinismo", "hipocrita", "pablo", "sara", "erick",
                   "maurice", "angel", "juan", "ignacio", "programar", "bases", "datacion", "datos", "dormir", "negar",
                   "aburrimiento", "cartas", "ajedrez", "dragones", "mazmorras", "enfermedad", "cabecita", "rodilla",
                   "brazo", "brazada", "natacion", "nadar", "bucear", "barcos", "yates", "puerto", "crucero", "polar",
                   "atlantico", "transatlantico", "igualdad", "feminismo", "diversidad", "cantar", "agujero", "salado",
                   "roedor", "bailando", "danzas", "namibia", "japoneses", "norte", "europa", "externo", "interno",
                   "nobleza", "caballerosidad", "torreon", "alacena", "guardarropa", "acondicionado", "fechado",
                   "optica", "graduacion", "mansion", "tejido", "banderin", "supermercado", "luminiscente",
                   "temporal", "esqueleto", "ornamenta", "expresion", "reaccion", "andamiaje", "convento", "cataratas",
                   "fluidos", "humareda", "humedal", "bosquejo", "desertico", "abandonado", "dioses", "griegos",
                   "romanos", "nordicos", "segunda", "avenida", "carretera", "caminante", "direccion"]
    return random.choice(diccionario)


def revisor(puesto, intento):
    if len(puesto) == 0:
        return None
    else:
        for vez in puesto:
            if vez != intento:
                pass
            else:
                return True
    revisor.__doc__ = "Llega a True si el input(intento) se encuentre en la lista(puesto)"

def muneco(intentos):
    if intentos == 5:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦═══════════░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╩╬╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫─╜░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
            """"")
    elif intentos == 4:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦════╤══════░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╩╬╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫─╜░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
            """"")
    elif intentos == 3:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦════╤══════░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚╤╝░░░░░░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╩╬╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫─╜░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
            """"")
    elif intentos == 2:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦════╤══════░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚╤╝░░░░░░░░
    ░░░║║░░┌╔╧╗┐░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ░░░║║░░░░░░░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╩╬╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫─╜░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
            """"")
    elif intentos == 1:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦════╤══════░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚╤╝░░░░░░░░
    ░░░║║░░┌╔╧╗┐░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ░░░║║░░░│░│░░░░░░░░
    ░░░║║░░░│░│░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╩╬╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫─╜░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
             """"")
    elif intentos == 0:
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦════╤══════░░░
    ░░░║║░░░░│░░░░░░░░░
    ░░░║║░░░░│░░░░░░░░░
    ░░░║║░░░╔╧╗░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚╤╝░░░░░░░░
    ░░░║║░░┌╔╧╗┐░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ╥╥╥╫╫╥░░│░│░░╥╥╥╥╥╥
    ╚╬╬╩╬░░░│░│░░░╬╩╬╬╝
    ░╟╫─╫░░░░░░░░░╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░─╜░╥╥░░╥░╙─░║║░
            """"")
    elif intentos == "win":
        muneco = ("""
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░═╦╦═══════════░░░
    ░░░║║░░░╔═╗░░░░░░░░
    ░░░║║░░│║░║│░░░░░░░
    ░░░║║░░│╚╤╝│░░░░░░░
    ░░░║║░░└╔╧╗┘░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░║░║░░░░░░░░
    ░░░║║░░░╚═╝░░░░░░░░
    ░░░║║░░░│░│░░░░░░░░
    ░░░║║░░░│░│░░░░░░░░
    ╥╥╥╫╫╥╥╥╥╥╥╥╥╥╥╥╥╥╥
    ╚╬╬╩╬╬╩╩╩╩╩╩╬╩╬╩╬╬╝
    ░╟╫─╫╜░░░░░░╙─╫─╫╢░
    ░╟╫─╜░░░░░░░░░╙─╫╢░
    ░║║░░░░░░░░░░░░░║║░
            """"")
    return muneco


