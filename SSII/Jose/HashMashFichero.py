import time
import hashlib
import threading


def searcher():
    crypted = "3a5b8990e60ffa74e15461d7547e0f62aa94d19de4e3de687bd31176f8b6d17b"
    with open("passwords.txt", "r", errors='ignore') as arch:
        passwords = arch.read()
        chunk = passwords.split()
        for match in chunk:
            matchbin = match.encode()
            matchhit = hashlib.sha256(matchbin)
            trycript = matchhit.hexdigest()
            if trycript != crypted:
                continue
            if trycript == crypted:
                arch.close()
                return print(match)


if __name__ == "__main__":
    inicio = time.time()
    Hilo1 = threading.Thread(target=searcher())
    Hilo1.start()
    fin = time.time()
    print(f"ha tardado {round(fin - inicio, 3)} segundos en encontrarse")

