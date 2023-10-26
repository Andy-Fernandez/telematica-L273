from socket import*							#importando el socket

addr = ("",7777)
serverSock = socket(AF_INET,SOCK_DGRAM) 	#creando socket
serverSock.bind(addr)                   	#vinculamos direccion y puerto con socket

while True:
	data , addr = serverSock.recvfrom(512)	#recibimos socketCliente y direccion cliente 
	mensaje = data.decode()	                #decodificamos
	
    # solucionamos solicitud
	resp = mensaje.upper()					#convertimos a mayusculas
	
    # enviamos respuesta
	serverSock.sendto(resp.encode() , addr)	#enviando respuesta codificada y direccion 