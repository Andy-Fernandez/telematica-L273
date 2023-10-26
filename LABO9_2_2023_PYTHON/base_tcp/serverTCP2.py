from socket import *
import sys

puerto = int(sys.argv[1])

addr = ("localhost", puerto)

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen()
print(f"Servidor corriendo por el puerto: {puerto}")

sock, addr = server.accept()

# recibiendo solicitud
solicitud = sock.recv(512).decode()

#solucionarsolicitud ************************************
solicitud = solicitud.upper()

# Enviar respuesta
sock.send(solicitud.encode())






