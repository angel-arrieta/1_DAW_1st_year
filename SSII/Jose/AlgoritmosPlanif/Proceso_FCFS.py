from CommonFuncs import leer, casting, calculador


def ordenador(lista):
    return lista[2]


if __name__ == "__main__":
    leibles = casting(leer("Process.FIFO.txt"))
    ordenados = sorted(leibles, key=ordenador)
    ejecutables = calculador(ordenados)
    for ciclos in ejecutables:
        print(f"Proceso {ciclos[0]}: empieza en el ciclo {ciclos[1]} y sale en el ciclo {ciclos[2]}")
