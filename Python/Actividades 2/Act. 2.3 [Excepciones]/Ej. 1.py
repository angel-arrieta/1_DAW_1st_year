if __name__ == "__main__":
    try:
        edad = int(input("Introduce tu edad:\t"))
        if edad > 0:
            cumple = 1
            while edad != 0:
                print(f"Cumpliste {cumple} año(s)")
                cumple += 1
                edad -= 1
        elif edad <= 0:
            raise Exception("Una edad no puede valer igual o menor que cero")
    except ValueError:
        print("Introduce tu edad en valor númerico")
