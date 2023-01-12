if __name__ == "__main__":
    print("Calculadora de gastos")
    gasto = 0
    while True:
        try:
            monto = int(input(">\t"))
            if monto == 0:
                break
            if monto < 0:
                print("Ingrese un monto positivo")
            gasto += monto
        except ValueError:
            print("Ingrese un número como monto")
    if gasto > 1000:
        print(f"Total a pagar {gasto-(gasto/10)}")
    else:
        print(f"Total a pagar {gasto}")
