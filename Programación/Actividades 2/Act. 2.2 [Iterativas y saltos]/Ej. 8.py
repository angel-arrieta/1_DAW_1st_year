nume = int(input("Introduzca la altura del triángulo:\t"))
imp = ['1']
lon = len(imp)
x = 1
while lon <= nume:
    print(*imp, sep=' ')
    x += 2
    imp.append(x)
    lon = len(imp)
