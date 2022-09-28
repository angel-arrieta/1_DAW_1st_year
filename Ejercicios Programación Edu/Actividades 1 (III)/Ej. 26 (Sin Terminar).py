print("Introduzca todos sus productos")
prods=str(input("Para finalizar introduzca: fin\n"))
listprods=[]
while prods!= "fin" :
    listprods.append(prods)
    prods = str(input())
    if prods == "fin" :
        print(*listprods,sep="\n")