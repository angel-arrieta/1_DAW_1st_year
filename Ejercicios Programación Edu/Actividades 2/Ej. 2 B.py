contrasena=input("Guarda tu contraseña:\n")
con=contrasena.lower()
print("Contraseña guardada")
introd=input("Introduzca la contraseña:\n")
int=introd.lower()
if con == int:
    print("Contraseña correcta")
else:
    print("Contraseña equivocada")
