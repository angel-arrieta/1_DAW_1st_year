if __name__ == "__main__":
    try:
        numero = input("Introduce un número entero:\t")
        if numero.count(",") != 0:
            raise ValueError

    except ValueError:
        print("La entrada no es correcta")
