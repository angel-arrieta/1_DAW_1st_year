print("Programa de eco/repetición, introduzca 'salir' para terminar")
put = input(">")
eco = []
while bool(put) is True:
    eco.append(put)
    put = input(">")
    if put == "salir":
        break
print(*eco, sep="\n")
