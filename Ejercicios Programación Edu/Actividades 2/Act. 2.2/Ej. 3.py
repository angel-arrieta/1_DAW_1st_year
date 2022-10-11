num = int(input("Introduzca un número entero y positivo:\t"))
comp = 1
imp = []
while comp <= num:
    if comp % 2 == 0:
        comp = comp + 1
        continue
    elif comp % 2 != 0:
        imp. append(comp)
        comp = comp + 1
        continue
print(imp, sep=", ")
