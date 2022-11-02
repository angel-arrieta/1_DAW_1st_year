print("Sumador de números enteros")
print("Introduzca 0 para terminar el programa")
num = int(input(">"))
count = 0
while num != 0:
    count = count + num
    num = int(input(">"))
else:
    print(f"La suma es {count}")
