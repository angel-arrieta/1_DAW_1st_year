import time
import threading
inicio = time.time()


def searcher():
    import hashlib
    crypted = "3a5b8990e60ffa74e15461d7547e0f62aa94d19de4e3de687bd31176f8b6d17b"
    arch = open("passwords.txt")
    conj = list(arch)
    file = ['']

    while True:
        for cont in conj:
            file[0] = cont

            match = "".join(file)
            matchbin = match.encode()
            matchhit = hashlib.sha256(matchbin)
            trycript = matchhit.hexdigest()

            if trycript == crypted:
                fin1 = time.time()
                print(f"La contraseña es {match} y ha tardado {round(fin1 - inicio, 3)} segundos en ejecutarse")
                exit()

            else:
                continue

    fin3 = time.time()
    print(f"Contraseña no encontrada, {round(fin3-inicio,3)} segundos malgastados")


lista = [threading.Thread(target=searcher) for _ in range(3)]
for i in lista:
    i.start()
