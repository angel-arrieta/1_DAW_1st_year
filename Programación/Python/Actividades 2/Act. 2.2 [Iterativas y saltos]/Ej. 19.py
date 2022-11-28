def acumulador(valor):
    valor += 1
    return valor


def impresion(element):
    text = element
    return text


def imprimir(text, times):
    press = []
    while times != 0:
        press.append(text)
        times -= 1
    imprime = "\n".join(press)
    return imprime


if __name__ == "__main__":
    veces = 0
    texto = "vacio, añade un listado"
    while True:
        veces = veces
        texto = texto
        while True:
            try:

                print(f"""
                        Impresor listado
                        1-Aumentar impresiones
                        2-Cambiar listado
                        3-Imprimir ({veces}veces)
                        0-finalizar
                        """)
                ini = int(input(">"))

                if ini == 1:
                    veces = acumulador(veces)
                    break
                if ini == 2:
                    put = input("Introduce el listado:\n")
                    texto = impresion(put)
                    break
                if ini == 3:
                    print(imprimir(texto, veces))
                    veces = 0
                    break
                if ini == 0:
                    print("Hasta la próxima ;)")
                    exit()
                else:
                    print("Opción no recogida, elija otra")
                    continue

            except ValueError:
                print("Opción inexistente, elija otra")
                continue
