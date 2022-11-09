import time
inicio = time.time()
incognitas = list('qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
Force = ['', '', '']
force = ""


for let in incognitas:
    Force[0] = let
    for let in incognitas:
        Force[1] = let
        for let in incognitas:
            Force[2] = let
            force = "".join(Force)
            print(f"[{force}]")

fin = time.time()
print(f"Ha tardado {round(fin-inicio, 3)} segundos en sacar todas las contraseñas")
