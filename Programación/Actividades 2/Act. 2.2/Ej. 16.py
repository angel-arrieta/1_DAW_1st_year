print("Buscador de número mayor")
print("Introduzca 0 para terminar el programa")
num = int(input(">"))
line = []
while num != 0:
    line.append(num)
    num = int(input(">"))
line.sort()
line.reverse()
print(f"El número mas grande es {line[0]}")
