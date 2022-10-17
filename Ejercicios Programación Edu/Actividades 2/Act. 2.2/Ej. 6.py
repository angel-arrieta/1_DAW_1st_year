ana = int(input("Introduzca la altura del triángulo:\t"))
imp = ['*']
lon = len(imp)
while lon <= ana:
    print(*imp, sep=' ')
    imp.append('*')
    lon = len(imp)
