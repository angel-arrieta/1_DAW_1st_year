def number(numero):
    suma = list(str(numero))
    total = 0
    for i in suma:
        dig = int(i)
        total += dig
    return total


def coparer(numero):
    if numero % 2 == 0:
        div = 0  # par
        return div
    if numero % 2 != 0:
        div = 1  # impar
        return div


if __name__ == "__main__":
    print("Sumador individual de los dígitos de un número entero positivo y contador de números pares e impares")
    print("Introduce -1 para salir")
    try:
        num = int(input(">"))
        sumlist = []
        divlist = []
        if type(num) == int and num >= -1:
            while not num == -1:
                sumlist.append(number(num))
                divlist.append(coparer(num))
                num = int(input(">"))
            print(*sumlist, sep=' ')
            print(f"Has ingresado {divlist.count(0)} números pares y {divlist.count(1)} números impares")
        else:
            print("Introduzca adecuadamente un número entero positivo")
    except ValueError:
        print("Ingrese un número positivo")
