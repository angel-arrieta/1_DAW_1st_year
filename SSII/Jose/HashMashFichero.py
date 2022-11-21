import threading
import time

inicio = time.time()


def searcher():
    import hashlib
    crypted = "3a5b8990e60ffa74e15461d7547e0f62aa94d19de4e3de687bd31176f8b6d17b"
    with open("passwords.txt", "r") as arch:
        readable = arch.read()
        conj = list(readable)
        file = ['']

        match = "".join(file)
        matchbin = match.encode()
        matchhit = hashlib.sha256(matchbin)
        trycript = matchhit.hexdigest()

        while trycript != crypted:
            for cont in conj:
                file[0] = cont

                match = "".join(file)
                matchbin = match.encode()
                matchhit = hashlib.sha256(matchbin)
                trycript = matchhit.hexdigest()

                if trycript == crypted:
                    arch.close()
                    print(f"La contraseña es {file}")

                else:
                    continue


fin = time.time()
print(f"ha tardado {round(fin - inicio, 3)} segundos en encontrarse")


Hilo1 = threading.Thread(target=searcher)
Hilo2 = threading.Thread(target=searcher)
Hilo3 = threading.Thread(target=searcher)
Hilo1.start()
Hilo2.start()
Hilo3.start()
