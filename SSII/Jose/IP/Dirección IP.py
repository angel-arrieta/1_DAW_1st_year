def ip_checker(value):
    octetos = value.split(".", 3)
    octetos[0] = int(octetos[0])
    octetos[1] = int(octetos[1])

    if 0 <= octetos[0] <= 127:
        tipo = "A (red grande)"
        if octetos[0] == 10:
            reach = "[privada]"
        else:
            reach = "[pública]"

    elif 128 <= octetos[0] <= 191:
        tipo = "B (red mediana)"
        if octetos[0] == 172 and 16 <= octetos[1] <= 31:
            reach = "[privada]"
        else:
            reach = "[pública]"

    elif 192 <= octetos[0] <= 223:
        tipo = "C (red pequeña)"
        if octetos[0] == 192 and octetos[1] == 168:
            reach = "[privada]"
        else:
            reach = "[pública]"
    check = f"IP tipo {tipo} {reach}"
    return check


def validator(value):
    parts = value.split(".", 3)
    for part in parts:
        part = int(part)

        if not 0 <= part <= 255:
            invalid = "La IP no es válida"
            return print(invalid), exit()
        else:
            return


def reserved(value):
    value = int(value)
    if value == 0 or 255:
        reservada = "La IP es reservada [broadcast]"
        return reservada
    else:
        return


def d_check(value):
    if int(value) >= 224:
        return True
    else:
        return False


if __name__ == "__main__":
    IP = input(">")
    octeto = IP.split(".", 3)
    validator(IP)
    print(reserved(octeto[3]))
    if d_check(octeto[0]) is True:
        print("IP tipo D [pública]")
    else:
        print(ip_checker(IP))
