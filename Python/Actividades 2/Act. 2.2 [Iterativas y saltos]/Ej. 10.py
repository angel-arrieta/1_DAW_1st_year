print("Introduzca un número entero para saber si es primo o no.")

numero = int(input(">"))
comparador = 0
if numero == 1:
    print(f"{numero} no es primo")
else:
    comparador = numero-1
    while comparador > 1:
        resto = numero % comparador
        if resto > 0 and resto != 0:
            comparador -= 1
        elif resto == 0:
            print(f"{numero} no es primo")
            exit()
    print(f"{numero} es primo")
