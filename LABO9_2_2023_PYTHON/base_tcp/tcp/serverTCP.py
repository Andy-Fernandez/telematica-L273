from socket import *

addr = ("localhost", 7777)

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen()

while True:
    sock, addr = server.accept()

    while True:
        # recibiendo solicitud
        solicitud = sock.recv(512).decode()
        #solucionarsolicitud ************************************
        # aumentar un if  que compare 'adios'  break
        solicitud = solicitud.upper()
        # Enviar respuesta
        sock.send(solicitud.encode())






