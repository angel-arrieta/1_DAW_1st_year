numero=str(input("Introduzca un número en formato prefijo-número-extension [+XX-(9X)-XX]\n"))
num=numero[:-2] #Quito los 2 ultimos al pasarlo a una array
num=num [-9:] #Excluyo lo que no sean los 9 ultimos del array
print(f"El número original es {num}")