if __name__ == "__main__":
    try:
        password = "password"
        contrasena = str(input("Introduce la contraseña\n>\t"))
        if contrasena != password:
            raise NameError
        else:
            print("Correct Password!")

    except NameError:
        print("Incorrect Password!")
