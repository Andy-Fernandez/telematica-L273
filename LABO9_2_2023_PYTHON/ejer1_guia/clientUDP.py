from socket import*

addr = ("localhost",7778)
sockClient = socket(AF_INET,SOCK_DGRAM)      #creando socket

numero = int(input(" Intro numero: "))
 
if (numero >= 0 and numero <=255):
    num = str(numero)
    sockClient.sendto(num.encode(), addr)

resp , addr= sockClient.recvfrom(512)       # recibiendo mensaje ( respuesta , direccion )
print(resp.decode())