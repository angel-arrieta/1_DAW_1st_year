wom = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
man = wom
man.append("n")
Name = str(input("Escribe tu nombre\t"))

if Name != str:
    print("Datos introducidos incorrectamente")
    quit()

name = Name.lower()
Sexo = str(input("¿Eres hombre o mujer?\t"))
sexo = Sexo.lower()
ini = name[0]

if sexo == "hombre":
    if ini in man:
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")
if sexo == "mujer":
    if ini in wom:
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")
if sexo != str:
    print("Datos introducidos incorrectamente")
else:
    print("Sexo no identificado")
