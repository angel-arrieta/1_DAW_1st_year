def leer(fichero):
    lista = []
    with open(fichero) as procesos:
        listado = procesos.readlines()
        for ejecucion in listado:
            stripped = ejecucion.rstrip("\n")
            lista.append(stripped.split(" "))
        procesos.close()
        lista.pop(0)
    return lista


def casting(listado):
    casteado = []
    import re
    for lista in listado:
        unir = []
        for data in lista:
            if re.match("[0-9]", data) is None:
                unir.append(data)
            if re.match("[0-9]", data) is not None:
                cast = int(data)
                unir.append(cast)
        casteado.append(unir)
    return casteado


def calculador(lista):
    listados = []
    iniciara = 0
    for tareas in lista:
        metemos = []
        proceso = tareas[0]
        metemos.append(proceso)
        if iniciara != 0:
            inicio = iniciara
        elif iniciara == 0:
            inicio = iniciara + tareas[2]
        metemos.append(inicio)
        fin = inicio + tareas[1]
        metemos.append(fin)
        listados.append(metemos)
        iniciara = fin + 1
    return listados
