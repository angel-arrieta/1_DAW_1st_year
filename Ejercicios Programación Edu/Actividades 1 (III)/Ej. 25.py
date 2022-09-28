date=str(input("Introduzca su fecha de nacimiento (formato dd/mm/aaaa)\n"))
dia=date[:-8]
mes=(int(date[:-5][-2:]))-1
ano=date[-4:]
listames=["enero", "febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
MES=listames[mes]
print(f"Usted nacio el {dia} de {MES} del año {ano}")