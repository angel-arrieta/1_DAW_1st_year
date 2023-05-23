from paramiko import SSHClient, AutoAddPolicy
import time

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect("172.26.1.194", username="usuario", password="usuario")
sftp = ssh.open_sftp()

if __name__ == "__main__":
    while True:
        with sftp.open("/var/log/nginx/access.log", "r") as log_file:
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
        time.sleep(3)

    sftp.close()
    ssh.close()
