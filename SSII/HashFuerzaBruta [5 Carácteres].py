import hashlib
import time
inicio = time.time()
conthashed = "80b164a062d120cf8544b4f8efbdcd4d2b0f1e89a5238a5a24f7b93918230378"
incognitas = list('ajsdfgohklñpiuytrewqzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890+-*')
Force = ['', '', '', '', '']

force = "".join(Force)
forcebin = force.encode()
hashmash = hashlib.sha256(forcebin)
comp = hashmash.hexdigest()
print(f"[{force}]")

if comp == conthashed:
    fin1 = round(time.time(),3)
    print(f"La contraseña es {force} y ha tardado {fin1-inicio} segundos en ejecutarse")
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

                        force = "".join(Force)
                        forcebin = force.encode()
                        hashmash = hashlib.sha256(forcebin)
                        comp = hashmash.hexdigest()
                        print(f"[{force}]")
                        if comp == conthashed:
                            fin2 = round(time.time(),3)
                            print(f"La contraseña es {force} y ha tardado {fin2-inicio}segundos en ejecutarse")
                            exit()
                        else:
                            continue
    fin3 = round(time.time(),3)
    print(f"Contraseña no encontrada, {fin3-inicio} segundos malgastados")
    exit()
