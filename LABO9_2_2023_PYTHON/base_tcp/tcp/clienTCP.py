from socket import *

addr = ("localhost", 7777)

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)


while True:
    mensaje = input("> Intro mensaje:\t")
    sock.send(mensaje.encode())
    # aumentar un if  que compare 'adios' break
    respuesta = sock.recv(512).decode()
    print(f"Mensaje del servidor:\t {respuesta}")
