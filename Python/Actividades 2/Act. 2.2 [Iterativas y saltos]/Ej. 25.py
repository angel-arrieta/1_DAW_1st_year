def longitud(palabra):
    return len(palabra)


if __name__ == "__main__":
    frase = input("Introduzca una frase\n>\t")
    palabras = frase.split()
    palabras.sort(reverse=True, key=longitud)
    longitudes = []
    print(f"La palabra más larga es {palabras[0]} y hay {len(palabras)} palabras en total")
