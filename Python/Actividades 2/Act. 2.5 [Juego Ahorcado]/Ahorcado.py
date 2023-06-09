from guardado import dame, revisor, muneco
"""
Documentación:

"""

if __name__ == "__main__":
    #  VARIABLES NECESARIAS
    secreta = dame()
    adivinar = []
    no_esta = []
    ya_probado = []
    intentos = 5
    for i in range(len(secreta)):
        adivinar.append("_")
    # vv PROCESO DE JUEGO vv
    while True:
        # PRINT INTERFAZ
        print(f"TESTING PURPOSE: '{secreta}'")  # TESTEO
        print(muneco(intentos))
        print(f"\tLongitud: {len(secreta)}")
        print(f"\tIntentos: {intentos}")
        print("\t"+(",".join(adivinar)))
        print(f"\tNo se encuentra:\n"
              f"\t{'  '.join(no_esta)}")
        intento = input("Introduzca una letra (ó 0 para intentar la palabra)\n> ")
        lugares = []
        # vv CONTROL DE ERRORES AL INPUT PRINCIPAL vv
        if revisor(ya_probado, intento) is True:
            print("Ya introduciste anteriormente esa letra")
            continue
        else:
            pass
        if len(intento) != 1:  # Hay más de un carácter
            print("Introduce solo UN carácter")
            continue
        try:
            if int(intento) is not ValueError and int(intento) != 0:  # No es letra ni el número 0
                print("Introduzca una letra (ó el numero 0)")
                continue
        except ValueError:  # Es una letra o 0
            pass
        # ^^ CONTROL DE ERRORES AL INPUT PRINCIPAL ^^
        # vv SUB-INPUT /PALABRAS/ vv
        if intento == "0":
            compara = str(input("Intente adivinar la palabra (0 para salir)\n> "))
            if compara == "0":
                print("Saliendo del intento de adivinar...")
                continue
            if revisor(ya_probado, compara) is True:
                print("Ya introduciste anteriormente esa palabra (saliendo...)")
                continue
            else:
                pass
            non = 0
            for letras in compara:
                try:
                    if int(letras) is not ValueError:
                        non = 1
                        break
                except ValueError:
                    continue
            if non == 1:
                print("Introduzca letras, no números (saliendo...)")
                continue
            # ^^ SUB-INPUT /PALABRAS/ ^^
            # vv COMPARADOR DE PALABRAS vv
            ya_probado.append(compara)
            if compara != secreta:
                no_esta.append(compara)
                intentos -= 1
            elif compara == secreta:
                adivinar = []
                for letra in compara:
                    adivinar.append(letra)
                break
            # ^^ COMPARADOR DE PALABRAS ^^##
        # vv BUSCADOR DE LETRAS vv
        elif intento != "0":
            ya_probado.append(intento)
            veces = secreta.count(intento)
            if veces == 0:
                no_esta.append(intento)
                intentos -= 1
            else:
                x = 0
                alter = list(secreta)
                for i in range(veces):
                    pos = alter.index(intento)
                    lugares.append(pos+x)
                    alter.remove(intento)
                    x += 1
                for positions in lugares:
                    adivinar[positions] = intento
        # ^^ BUSCADOR DE LETRAS ^^
        #  PASO AL DESENLACE
        if intentos == 0 or adivinar.count("_") == 0:
            break
    # ^^ PROCESO DE JUEGO ^^
    # PRINTS DESENLACE JUEGO
    if "".join(adivinar) == secreta:
        intentos = "win"
        print(muneco(intentos))
        print("\t¡Has Ganado!")
        print("\t" + ("".join(adivinar)))
    if "".join(adivinar) != secreta:
        print("\tHas Perdido")
        print(muneco(intentos))
        print(f"\tLa palabra secreta era {secreta}")
