def coincidir(cadena, caracter):
    return cadena.find(caracter)


if __name__ == "__main__":
    frase = input("Introduzca una frase\n").lower()
    while True:
        letra = input("Introduce una letra a buscar\t").lower()
        if 0 < len(letra) >= 2:
            print("Introduzca UN carácter")
        if len(letra) == 1:
            break
    posicion = coincidir(frase, letra)
    if posicion == int(-1):
        print(f"en {frase} no hay ningún/a {letra}")
    elif posicion >= int(1):
        print(f"hay al menos un/a {letra} en la posición {posicion}")
