b=3.49
bay=float(input("Barras vendidas que no son del día:\t"))
dbay=b*0.6 #lo que se le descuenta a una barra de ayer
dubay=b-dbay #lo que vale una barra de ayer
tbay=bay*dubay #lo que valen todas las barras de ayer
rdbay=round(dbay,2)
rtbay=round(tbay,2)
print(f"Una barra del día vale {b}eur.")
print(f"A las barras que no son del día se les descuenta {rdbay}eur.")
print(f"Todas las barras que no son del día han generado {rtbay}eur.")
