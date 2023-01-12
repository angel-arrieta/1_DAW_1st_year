if __name__ == "__main__":
    while True:
        try:
            print("""
            1- comenzar programa
            2- imprimir listado
            3-finalizar programa
            """)
            opcion = int(input(">\t"))
            if opcion == int(1):
                print("""
                COMENZAR Programa-dolor sit amet, consectetur adipiscing elit.
                Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
                massa. Mauris ac magna vel lorem ultrices tincidunt.
                Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
                odio sodales, ultricies risus at, imperdiet quam.
                """)
            if opcion == int(2):
                print("""
                IMPRIMIR Listado-dolor sit amet, consectetur adipiscing elit.
                Maecenas justo mi, accumsan eu lorem at, ultricies rutrum
                massa. Mauris ac magna vel lorem ultrices tincidunt.
                Nullam vel sem orci. Nullam finibus ex orci. Nullam vitae
                odio sodales, ultricies risus at, imperdiet quam.
                """)
            if opcion == int(3):
                break
            if opcion < 1 or opcion > 3:
                print("Opción incorrecta, vuelva a intentar")
        except ValueError:
            print("Opción incorrecta, vuelva a intentar")
