cor = input("Introduzca su correo:\n")
sep = '@'
cor = cor.split(sep, 1)[0]
cor = cor + "@ceu.es"
print(cor)