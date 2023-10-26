from socket import*

addr = ("localhost",7778)
sockClient = socket(AF_INET,SOCK_DGRAM)      #creando socket

mensaje = input(" Intro mensaje: ")         #leyendo mensaje o peticion

# 2 parametros
sockClient.sendto(mensaje.encode(), addr)   #enviando mensaje ( mensaje , direccionPuerto )

resp , addr= sockClient.recvfrom(512)       # recibiendo mensaje ( respuesta , direccion )
print(resp.decode())