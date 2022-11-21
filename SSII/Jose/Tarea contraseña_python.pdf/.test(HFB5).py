import time
inicio = time.time()
conthashed = "80b164a062d120cf8544b4f8efbdcd4d2b0f1e89a5238a5a24f7b93918230378"
incognitas = list('ñlkjhgfdsapoiuytrewqmnbvcxzQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890+-*')
space = ['', '', '', '', '']
inv = ['', '', '', '', '']


def searcher():
    while comparer() != conthashed:
        searc = space
        for let in incognitas:
            searc[0] = let
            for let in incognitas:
                searc[1] = let
                for let in incognitas:
                    searc[2] = let
                    for let in incognitas:
                        searc[3] = let
                        for let in incognitas:
                            searc[4] = let
                            return searc


def comparer():
    import hashlib
    use = searcher()
    force = "".join(use)
    forcebin = force.encode()
    hashmash = hashlib.sha256(forcebin)
    comp = hashmash.hexdigest()
    return comp


def main():
    while True:
        if comparer() == conthashed:
            res = "".join(searc)
            return res
        else:
            continue


main()
