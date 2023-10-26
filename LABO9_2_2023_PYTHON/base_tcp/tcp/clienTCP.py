from socket import *

addr = ("localhost", 7777)

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)


while True:
    mensaje = input("> Intro mensaje:\t")
    sock.send(mensaje.encode())
    # aumentando un if  que compare 'adios' break
    if mensaje.lower() == "adios":  # Verifica si el mensaje es "adios" (ignora mayúsculas/minúsculas)
        break
    respuesta = sock.recv(512).decode()
    print(f"Mensaje del servidor:\t {respuesta}")
