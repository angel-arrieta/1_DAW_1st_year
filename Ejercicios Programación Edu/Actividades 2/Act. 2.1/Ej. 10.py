veget = ["pimiento", "tofu"]
todo = ["pimiento", "tofu", "peperoni", "jamón", "salmón"]
print("Bienvenidos a la pizzeria Bella Napoli")
lis = input("¿Es usted vegetariano o no? (si/no)")
if lis == "si":
    print(veget)
    ingr = input("Escoja un ingrediente de los anteriores\n")
    print(f"Tu pizza vegetariana tiene {ingr}, queso y tomate")
elif lis == "no":
    print(todo)
    ingr = input("Escoja un ingrediente de los anteriores\n")
    print(f"Tu pizza tiene {ingr}, queso y tomate")
else:
    print("Aclaración mal introducida")
