print("Calcule sus ahorros por intereses en los proximos 3 años")
din=float(input("Ahorros actuales:\t"))
a=din*1.04
b=a*1.04
c=b*1.04
ra=round(a,2)
rb=round(b,2)
rc=round(c,2)
print("Ahorros de los proximos 3 años:")
print(f"1er año: {ra}")
print(f"2do año: {rb}")
print(f"3er año: {rc}")