dinero = int(input("Introduce el capital a invertir\n"))
interes = int(input("Introduce el interes anual\n"))
anos = int(input("Duración de la inversión en años:\t"))
tiempo = 1
while tiempo <= anos:
    print(f"año {tiempo} : {dinero * (tiempo + interes / 100)}")
    tiempo = tiempo + 1
