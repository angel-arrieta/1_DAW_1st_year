import socket


def buscador(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sket:
        try:
            sket.connect((ip, 18))
            sket.sendall(b"School Test. Hola, Estas Ahi")
            sket.settimeout(30.0)
            data = sket.recv(1024)
            return f"Recibido:{data!r}"
        except TimeoutError:
            return "Tiempo de conexión agotado (30sec)"


if __name__ == "__main__":
    print("Introduce los 3 primeros octetos de una IP")
    IP = input(">\t")
    dire = str(IP+".255")
    print(buscador(dire))
