import time
import threading
inicio = time.time()
incognitas = list('qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
Force = ['', '', '', '', '', '']


def searcher():
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
                            print(f"[{force}]")


Hilo1 = threading.Thread(target=searcher)
Hilo2 = threading.Thread(target=searcher)
Hilo3 = threading.Thread(target=searcher)
Hilo1.start()
Hilo2.start()
Hilo3.start()


fin = time.time()
print(f"Ha tardado {round(fin-inicio, 3)} segundos en sacar todas las contraseñas")
