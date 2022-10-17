print("Introduzca la contraseña")
con = str("contraseña")
user = input(">")
while user != con:
    print("Contraseña incorrecta. Vuelva a intentar")
    user = input(">")
print("Contraseña correcta. Bienvenido.")
