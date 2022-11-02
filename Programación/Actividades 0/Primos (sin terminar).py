print("Escribe un número para saber si es primo o no")
x = int(input("Introduce un número\t"))
cont = int
if x == 1:
    print(f"{x} no es primo")
else:
    cont = x - 1
    while cont > 1:
        res = x % cont
        if res > 0 and res != 0:
            cont -= 1
        elif res == 0:
            print(f"{x} no es primo")
            exit()
    print(f"{x} es primo")
