import numpy as np
from collections import Counter


def iguales(diccionario_1, diccionario_2):
    return diccionario_1.__eq__(diccionario_2)


def comprobar_barcos(oceano, cuenta_barcos):
    barcos_oceano = {}
    tamano = 0
    for fila in range(oceano.shape[0]):
        for casilla in oceano[fila, :]:
            if casilla == 0:
                if tamano > 1:
                    if tamano in barcos_oceano:
                        barcos_oceano[tamano] += 1
                    else:
                        barcos_oceano[tamano] = 1
                tamano = 0
            else:
                tamano += 1
    for columna in range(oceano.shape[1]):
        for casilla in oceano[:, columna]:
            if casilla == 0:
                if tamano > 1:
                    if tamano in barcos_oceano:
                        barcos_oceano[tamano] += 1
                    else:
                        barcos_oceano[tamano] = 1
                tamano = 0
            else:
                tamano += 1

    return iguales(barcos_oceano, cuenta_barcos)


if __name__ == '__main__':
    respuestas = []
    numero_barcos = int(input("numero de barcos:"))
    while numero_barcos > 0:
        lista_barcos = [int(x) for x in input().split()]
        cuenta_barcos = Counter(lista_barcos)
        tamano_oceano = int(input("tamaño(lado) del oceano:"))
        oceano = []
        for fila in range(tamano_oceano):
            oceano.append([int(x) for x in input().split()])
        oceano = np.array(oceano)
        if comprobar_barcos(oceano, cuenta_barcos):
            respuestas.append('SI')
        else:
            respuestas.append('NO')
        numero_barcos = int(input())
    for respuesta in respuestas:
        print(respuesta)
