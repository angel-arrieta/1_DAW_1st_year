pre=float(input("Introduzca el precio de un producto:\t"))
Pre=int(pre//1)
prE=pre-Pre
prE=round(prE,2)
prE=int(prE*100)
print(f"el artículo vale {Pre} euros y {prE} centimos")