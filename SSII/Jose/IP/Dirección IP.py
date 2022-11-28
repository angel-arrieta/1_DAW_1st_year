def validator(value):
    parts = value.split(".", 3)
    for part in parts:
        if int(part) > 255:
            invalid = "La IP no es válida"
            return print(invalid), exit()
        else:
            return


def privacy(value):
    if int(value) >= 224:
        public = "La IP es pública"
        return print(public)
    else:
        return


def reserved(value):
    if value == 0 or 255:
        reservada = "La IP es reservada [broadcast]"
        return print(reservada)
    else:
        return


def IPtype(value):
    value = 0
    return value


if __name__ == "__main__":
    IP = input(">")
    octetos = IP.split(".", 3)
    # www.xxx.yyy.zzz   www=[0]   xxx=[1]   yyy=[2]   zzz=[3]
    validator(IP)
    privacy(octetos[0])
    reserved(octetos[3])
    IPtype()
