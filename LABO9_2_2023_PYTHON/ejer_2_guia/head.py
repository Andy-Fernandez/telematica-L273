from socket import *

# Dirección del servidor Apache y el puerto (generalmente 80)
server_address = ('localhost', 80)

# Crear un socket TCP
client_socket = socket(AF_INET,SOCK_STREAM)

# Conectar al servidor
client_socket.connect(server_address)

# Construir la solicitud HEAD
request = "HEAD / HTTP/1.1\r\n" \
          "Host: localhost\r\n" \
          "Connection: close\r\n\r\n"

#HEAD / HTTP/1.1\r\nHost: {url}\r\n\r\n"

# Enviar la solicitud al servidor
client_socket.send(request.encode())

# Recibir la respuesta del servidor
response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

# Cerrar el socket
client_socket.close()

# Imprimir la respuesta del servidor
print(response.decode())
