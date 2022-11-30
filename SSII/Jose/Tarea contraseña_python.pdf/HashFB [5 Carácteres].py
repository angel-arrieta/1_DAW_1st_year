import time
import threading
import hashlib


def searcher():
    conthashed = "80b164a062d120cf8544b4f8efbdcd4d2b0f1e89a5238a5a24f7b93918230378"
    incognitas = list('ñlkjhgfdsapoiuytrewqmnbvcxzQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
    Force = ['', '', '', '', '']
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
                        if comp == conthashed:
                            return force
                        else:
                            continue


if __name__ == "__main__":
    inicio = time.time()
    print(f"La contraseña es {searcher()}")
    fin = time.time()
    print(f"Ha tardado {round(fin - inicio, 3)} segundos")
