intr = str(input(">"))
twolast = intr[-2:]
exclast = intr[:-2]

palabra = intr.lower()
if palabra != intr:
    print("Incorrecto")

if twolast == "ba":
    if intr == twolast:
        print("Correcto")
    elif intr == "a" + twolast:
        print("Correcto")
    elif exclast.rfind("a") >= 1:
        print("Correcto")
else:
    print("Incorrecto")
