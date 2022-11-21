import time
import threading
inicio = time.time()


def searcher():
    import hashlib
    conthashed = "80b164a062d120cf8544b4f8efbdcd4d2b0f1e89a5238a5a24f7b93918230378"
    incognitas = list('ñlkjhgfdsapoiuytrewqmnbvcxzQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
    Force = ['', '', '', '', '']

    force = "".join(Force)
    forcebin = force.encode()
    hashmash = hashlib.sha256(forcebin)
    comp = hashmash.hexdigest()
    print(f"[{force}]")

    if comp == conthashed:
        fin1 = time.time()
        print(f"La contraseña es {force} y ha tardado {round(fin1-inicio,3)} segundos en ejecutarse")
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
                                fin2 = time.time()
                                print(f"La contraseña es {force} y ha tardado {round(fin2-inicio,3)}segundos en ejecutarse")
                                exit()
                            else:
                                continue
    fin3 = time.time()
    print(f"Contraseña no encontrada, {round(fin3-inicio,3)} segundos malgastados")

Hilo1 = threading.Thread(target=searcher)
Hilo2 = threading.Thread(target=searcher)
Hilo3 = threading.Thread(target=searcher)
Hilo1.start()
Hilo2.start()
Hilo3.start()
