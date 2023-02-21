if __name__ == "__main__":
    try:
        edad = int(input("Introduce un número entero positivo:\t"))
        impar = []
        x = 1
        while x != (edad+1):
            if x % 2 == 0:
                x += 1
            else:
                impar.append(x)
                x += 1
        print(impar)

    except ValueError:
        print("Introduce un valor númerico")
