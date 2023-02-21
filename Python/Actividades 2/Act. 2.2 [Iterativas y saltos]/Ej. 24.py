def primador(numero):
    if numero == 1:
        return 0
    else:
        cont = numero - 1
        while cont > 1:
            res = numero % cont
            if res > 0 and res != 0:
                cont -= 1
            elif res == 0:
                return 0
        return 1


if __name__ == "__main__":
    print("Introduzca números mayores de 1")
    primos = 0
    while True:
        x = int(input("Introduce un número. (Introduzca 0 para terminar)\t"))
        if x == 0:
            break
        elif x < 0 or x == 1:
            print("Introduzca números mayores de 1")
        elif x > 1:
            primos += primador(x)
    print(f"Has ingresados {primos} números primos")
