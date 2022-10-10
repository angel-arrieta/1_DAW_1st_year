veget = ["pimiento", "tofu"]
todo = ["pimiento", "tofu", "peperoni", "jamón", "salmón"]
print("Bienvenidos a la pizzeria Bella Napoli")
lis = input("¿Es usted vegetariano o no? (si/no)")
pizza = []
ingr = ""
if lis == "si":
    print(veget)
    while ingr != "fin":
        ingr = input("Escoja entre los ingredientes anteriores (Introduzca fin para terminar)\n")
        pizza. append(ingr)
    pizza.remove("fin")
    print(f"Tu pizza vegetariana tiene", pizza, sep=", " " queso y tomate")
if lis == "no":
    print(todo)
    while ingr != "fin":
        ingr = input("Escoja entre los ingredientes anteriores (Introduzca fin para terminar)\n")
        pizza. append(ingr)
    pizza. remove("fin")
    print(f"Tu pizza vegetariana tiene", pizza, sep=", " " queso y tomate")
