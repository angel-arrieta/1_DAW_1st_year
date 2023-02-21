if __name__ == "__main__":
    while True:
        print("Cuenta atrás")
        try:
            inicio = int(input("Introduce un número desde donde empezar:\t"))
            cuenta = []
            while inicio != (-1):
                cuenta.append(inicio)
                inicio -= 1
            print(cuenta)
            break
        except ValueError:
            print("Introduce un valor númerico")