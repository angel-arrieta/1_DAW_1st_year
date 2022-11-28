def guardar(element):
    add = element
    return add


if __name__ == "__main__":
    listado = "vacio, introduzca texto"
    while True:
        while True:
            try:
                print(f"""
                        Impresor de lista
                        "1"-Alterar listado
                        "2"-Imprimir listado
                        "3"-finalizar
                        """)
                ini = int(input(">"))
                if ini == 1:
                    put = input("Escribe el listado:\n")
                    listado = guardar(put)
                    break
                if ini == 2:
                    print(listado)
                    break
                if ini == 3:
                    print("Hasta la próxima ;)")
                    exit()
                else:
                    print("Opción no recogida, elija otra")
                    continue

            except ValueError:
                print("Opción inexistente, elija otra")
                continue
