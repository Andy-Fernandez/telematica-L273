from socket import *
import sys
####SOLO RESCIVE UN MENSAJE Y RESPONDE CON EL MISMO MENSAJE EN MAYUSCULAS ####
# Obtener el número de puerto de los argumentos de línea de comandos
puerto = int(sys.argv[1])

# Definir la dirección a la que se va a enlazar el servidor
addr = ("localhost", puerto)

# Crear un socket del servidor
server = socket(AF_INET, SOCK_STREAM)

# Enlazar el servidor a la dirección y puerto especificados
server.bind(addr)

# Escuchar por conexiones entrantes
server.listen()

# Imprimir un mensaje indicando que el servidor está en ejecución
print(f"Servidor corriendo por el puerto: {puerto}")

# Aceptar una conexión entrante y obtener un socket de cliente
sock, addr = server.accept()

# Recibir la solicitud del cliente
solicitud = sock.recv(512).decode()

# Convertir la solicitud a mayúsculas (en este caso, para simplificar)
solicitud = solicitud.upper()

# Enviar la respuesta al cliente
sock.send(solicitud.encode())
