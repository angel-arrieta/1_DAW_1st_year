from CommonFuncs import leer, casting, calculador


def ordenador(lista):
    lista = sorted(lista, key=ordena_entradayduracion)
    ordered = []
    ordered.append(lista.pop(0))
    while True:
        if len(lista) == 0:
            break
        paralelo = []
        wiper = []
        x = len(ordered)-1
        for tarea in lista:
            if x == 0:
                comienzo = 1
                ultimo = ordered[x][1] + ordered[x][2]
            else:
                for n in range(comienzo, len(ordered)):
                    ultimo += ordered[n][2]
                    if n == (len(ordered)-1) and comienzo < len(ordered):
                        comienzo = ultimo
            if tarea[2] <= ultimo:
                paralelo.append(tarea)
                wiper.append(tarea)
            elif tarea[2] > ultimo:
                if len(lista) == 1:
                    paralelo.append(tarea)
                    wiper.append(tarea)
                break
        paralelo.sort(key=ordena_duracion)
        for tarea in paralelo:
            ordered.append(tarea)
        for hecho in wiper:
            lista.remove(hecho)
    return ordered


def ordena_entradayduracion(lista):
    return lista[2], lista[1]


def ordena_duracion(lista):
    return lista[1]


if __name__ == "__main__":
    leibles = casting(leer("Process.FIFO.txt"))
    ordenado = ordenador(leibles)
    ejecutable = calculador(ordenado)
    for ciclos in ejecutable:
        print(f"Proceso {ciclos[0]}: entra en el ciclo {ciclos[1]} y sale en el ciclo {ciclos[2]}")
