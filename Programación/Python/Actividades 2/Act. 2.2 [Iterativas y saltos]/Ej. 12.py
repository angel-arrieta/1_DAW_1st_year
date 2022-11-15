print("Programa buscador de repetición de letra")
inicial = input("<frase>\n")
frase = inicial
letra = input("letra (solo una)>\t")
count = 0
if len(letra) > 1:
    print("Introduzca solo una letra")
    exit()
if len(letra) < 1:
    print("Introduzca una letra")
    exit()
pos = frase.find(letra)
while pos >= 0:
    count += 1
    Frase = list(frase)
    Frase.pop(pos)
    frase = "".join(Frase)
    pos = frase.find(letra)
else:
    print(f"en {inicial} hay {count} {letra}")
