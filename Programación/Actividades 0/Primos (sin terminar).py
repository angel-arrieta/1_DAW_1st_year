print("Escribe un número para saber si es primo o no")
x = int(input("Introduce un número\t"))
cont = int
if x == 1:
    print(f"{x} es primo")
else:
    cont = x - 1

    while x % cont == 1 and cont > 1:
        print(f"{x} no es primo")
        cont = cont - 1
    else:
        print(f"{x} es primo")