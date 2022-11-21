def imprimir_tablero():
    columnas = "ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    print()
    for orden, fila in enumerate(tablero()):
        print(orden+1, end=" ")
        if orden+1 < 10:
            print(" ", end="")
        for celda in fila:
            print(celda, end=" ")
        print()


def tablero(filas=10, columnas=10):
    return [["V" for _ in range(columnas)] for _ in range(filas)]


imprimir_tablero()
