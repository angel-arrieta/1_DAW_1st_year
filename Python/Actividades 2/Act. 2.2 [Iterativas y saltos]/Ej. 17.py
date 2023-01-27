def number(num):
    suma = list(str(num))
    total = 0
    for i in suma:
        dig = int(i)
        total += dig
    return total


if __name__ == "__main__":
    print("Suma de los dígitos de un número entero positivo")
    try:
        num = int(input(">"))
        if type(num) == int and num > 0:
            print(f"La suma total de los dígitos es {number(num)}")
        else:
            print("Introduzca adecuadamente un número entero positivo")
    except ValueError:
        print("Introduce al menos un número")
