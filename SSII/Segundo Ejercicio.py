import re
introducir = input(">")
if len(introducir) > 20:
    print("Hay más caracteres de los admitidos")
    exit()

scan = re.findall("[A-Za-zÑñ]", introducir)
if scan:
    ordenado = ''.join(sorted(scan))
    print(ordenado)
else:
    print("Hay algún caracter repetido o no aceptado")
