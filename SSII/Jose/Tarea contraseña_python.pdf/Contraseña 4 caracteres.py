import hashlib
guard = str("66dae38707b050d25bf0c43a21d94e046111c129f27e331d9dacc556a419ba11")
print("Introduzca la contrasena (máx 4 caracteres)")
con = str(input(">"))
conbin = con.encode()
safe = con.find("ñ")
SAFE = con.find("Ñ")
if safe >= 0 or SAFE >= 0:
    print("No se permite la ñ/Ñ")
    exit()
hashcon = hashlib.sha256()
hashcon.update(conbin)
if hashcon.hexdigest() == guard:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
