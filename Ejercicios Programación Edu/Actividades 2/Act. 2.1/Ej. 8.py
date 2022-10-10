eva=float(input("Introducir Evaluación Anual\n"))
if eva == 0.0 :
    print ("Evaluación inaceptable, sin bonificación obtenida")
elif eva == 0.4 :
    print (f"Evaluación aceptable, bonificación de {0.4*2400} obtenida")
elif eva >= 0.6 :
    print (f"Evaluación meritoria obtenida, bonificación de {eva*2400}")
else:
    print ("Datos Introducidos ilegibles o incorrectos")