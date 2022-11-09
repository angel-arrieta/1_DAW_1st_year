import hashlib
import time
inicio = round(time.time(), 3)
conthashed = "e9c722cbefc2f055ae60b4e2cbe73a2d99537eab0c37f3bc2dd9e0854278b970"
incognitas = list('MmNnBbVvCcXxZzAaSsDdFfGgHhJjKkLlÑñPpOoIiUuYyTtRrEeWwQq1234567890+-*')
Force = ['', '', '', '', '', '']

force = "".join(Force)
forcebin = force.encode()
hashmash = hashlib.sha256(forcebin)
comp = hashmash.hexdigest()
print(f"[{force}]")

if comp == conthashed:
    fin1 = round(time.time(), 3)
    print(f"La contraseña es {force} y ha tardado {fin1 - inicio} segundos en ejecutarse")
    exit()

while True:
    for let in incognitas:
        Force[0] = let
        for let in incognitas:
            Force[1] = let
            for let in incognitas:
                Force[2] = let
                for let in incognitas:
                    Force[3] = let
                    for let in incognitas:
                        Force[4] = let
                        for let in incognitas:
                            Force[5] = let

                            force = "".join(Force)
                            forcebin = force.encode()
                            hashmash = hashlib.sha256(forcebin)
                            comp = hashmash.hexdigest()
                            print(f"[{force}]")
                            if comp == conthashed:
                                fin2 = round(time.time(), 3)
                                print(f"La contraseña es {force} y ha tardado {fin2 - inicio}segundos en ejecutarse")
                                exit()
                            else:
                                continue
    fin3 = round(time.time(), 3)
    print(f"Contraseña no encontrada, {fin3 - inicio} segundos malgastados")
    exit()
