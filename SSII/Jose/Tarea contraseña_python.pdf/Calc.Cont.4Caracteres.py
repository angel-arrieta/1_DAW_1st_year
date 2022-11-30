import time
inicio = time.time()
incognitas = list('qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
Force = ['', '', '', '']
force = ""


def searcher():
    for let in incognitas:
        Force[0] = let
        for let in incognitas:
            Force[1] = let
            for let in incognitas:
                Force[2] = let
                for let in incognitas:
                    Force[3] = let
                    force = "".join(Force)
                    return force


if __name__ == "__main__":
    inicio = time.time()
    con = ""
    while con != "****":
        con = searcher()
        print(con)
    fin = time.time()
    print(f"Ha tardado {round(fin - inicio, 3)} segundos")
