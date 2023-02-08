def oddeven(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"


if __name__ == "__main__":
    print("Contador de paridad de digitos")
    print("Introduzca cualquier número")
    try:
        granlista = []
        while True:
            print("Para salir introduzca 0")
            entrada = int(input(">\t"))
            if entrada != 0:
                entry = str(entrada)
                lista = []
                lista[:] = entry
                for numb in entry:
                    numb = int(numb)
                    lista.append(oddeven(numb))
                par = lista.count("par")
                impar = lista.count("impar")
                print(f"{par} dígitos pares / {impar} dígitos impares")
                for digitos in lista:
                    granlista.append(digitos)
            if entrada == 0:
                break
        granpar = granlista.count("par")
        granimpar = granlista.count("impar")
        print(f"En total, has introducido:\n {granpar} dígitos pares\n {granimpar} dígitos impares")

    except ValueError:
        print("Introduzca un valor numérico")
