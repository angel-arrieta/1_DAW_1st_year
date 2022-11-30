import time
import threading
import hashlib


def searcher():
    conthashed = "e9c722cbefc2f055ae60b4e2cbe73a2d99537eab0c37f3bc2dd9e0854278b970"
    incognitas = list('MmNnBbVvCcXxZzAaSsDdFfGgHhJjKkLlÑñPpOoIiUuYyTtRrEeWwQq1234567890+-*')
    Force = ['', '', '', '', '', '']
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
                            if comp == conthashed:
                                return force
                            else:
                                continue


if __name__ == "__main__":
    inicio = time.time()
    print(f"La contraseña es {searcher()}")
    fin = time.time()
    print(f"Ha tardado {round(fin - inicio, 3)} segundos")
