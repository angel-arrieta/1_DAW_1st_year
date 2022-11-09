num = int(input("Introduzca un número entero y positivo:\t"))
catras = []
while num >= 0:
    catras. append(num)
    num = num - 1
print(catras, sep=", ")
