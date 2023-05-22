from paramiko import SSHClient, AutoAddPolicy

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("172.26.1.194", username="usuario", password="usuario")


remote_path = "/ruta/al/log.log"  # Reemplaza "/ruta/al/log.log" por la ruta correcta del log en el servidor


sftp = ssh.open_sftp()

if __name__ == "__main__":
    with sftp.open(remote_path, "r") as log_file:
        lines = log_file.readlines()[-10:]

    with open("index.html", "w") as index_file:
        index_file.write("<html>\n")
        index_file.write("<body>\n")
        index_file.write("<pre>\n")
        index_file.writelines(lines)
        index_file.write("</pre>\n")
        index_file.write("</body>\n")
        index_file.write("</html>\n")

    print("Se ha creado el archivo index.html con las últimas líneas del log.")
    sftp.close()
    ssh.close()
