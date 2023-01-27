print("Sumador de números positivos")
print("Introduzca 0 para terminar el programa")
num = 1
count = 0
while num != 0:
    num = int(input(">"))
    if num > 0:
        count = count + num
    elif num < 0:
        continue
else:
    print(f"La suma de los números positivos es {count}")
