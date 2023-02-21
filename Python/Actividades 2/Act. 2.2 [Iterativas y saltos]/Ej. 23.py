import re


def contador(linea):
    digi = 0
    for char in linea:
        es = re.match("[0-9]", char)
        if es is not None:
            digi += 1
    return digi


if __name__ == "__main__":
    print("Ingrese títulos de libro")
    digitos = 0
    lineas = 0
    while True:
        titulo = input(">")
        if titulo == "/":
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            lineas += 1
            digitos = 0
        if titulo == "*":
            break
        digitos += contador(titulo)
    print(f"Fin. Se leyeron {lineas} líneas completas.")
