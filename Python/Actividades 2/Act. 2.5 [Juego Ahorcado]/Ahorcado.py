from guardado import dame


if __name__ == "__main__":
    secreta = dame()
    adivinar = []
    intentado = []
    puesto = []
    print(secreta)
    intentos = 5
    for i in range(len(secreta)):
        adivinar.append("_")
    while True:
        print(f"Longitud: {len(secreta)}")
        print(f"Intentos restantes: {intentos}")
        print(",".join(adivinar))
        print(f"No se encuentra: {'  '.join(intentado)}")
        intento = input("Introduzca una letra (ó 0 para intentar la palabra)\n> ")
        if int(intento) == 0:
            compara = str(input("Intente adivinar la palabra\n> "))
            puesto.append(compara)
            if compara != secreta:
                intentado.append(compara)
                intentos -= 1
            if compara == secreta:
                adivinar = []
                for letra in compara:
                    adivinar.append(letra)
                break
        elif isinstance(intento, str) is True and len(intento) == 1:
            lugares = []
            puesto.append(intento)
            veces = secreta.count(intento)
            if veces == 0:
                intentado.append(intento)
                intentos -= 1
            elif veces == 1:
                lugares.append(secreta.find(intento))
            elif veces > 1:
                x = 0
                for i in range(veces):
                    alter = secreta
                    pos = alter.find(intento)
                    lugares.append(alter[pos]+x)
                    alter.pop(alter[pos]+x)
                    x += 1
            for positions in lugares:
                adivinar[positions] = intento
        if int(intento) != 0 or isinstance(intento, str) is False:
            print("Introduzca una letra (ó el numero 0)")
        elif isinstance(intento, str) is True and len(intento) != 1:
            print("Introduce solo UNA letra porfavor")
        if intentos == 0:
            break
    if "".join(adivinar) == secreta: #GANA
        "ra"
    if "".join(adivinar) != secreta: #PIERDE
        "ra"
