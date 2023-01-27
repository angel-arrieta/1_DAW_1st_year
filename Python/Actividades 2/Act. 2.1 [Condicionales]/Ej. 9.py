print("Bienvenido a Fazbear Entertainment")
edad = int(input("Introduzca su edad:\t"))
if 0 < edad <= 4:
    print("¿A que esperas? ¡Entra adentro, chic@!")
elif 4 < edad < 18:
    print("¡Por 5 euros puedes entrar, chaval!")
elif 18 <= edad < 27:
    print("Por solo 10 euros puede entrar, jovencit@")
elif edad >= 27:
    print("Buenas señor/a debe pagar 10 euros por la entrada")
else:
    print("Perdona, pero no lo entendi bien")
