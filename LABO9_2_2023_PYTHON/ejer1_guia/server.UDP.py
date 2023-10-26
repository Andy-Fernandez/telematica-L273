from socket import*							

addr = ("localhost",7778)
serverSock = socket(AF_INET,SOCK_DGRAM) 	
serverSock.bind(addr)                   	


def calcular(numero, base):
	resto = ""
	while numero!=0:
		x = numero%base
		numero = numero//base
		resto = str(x) + resto 
	return resto



data , addr = serverSock.recvfrom(512)	 
numero = int(data.decode())

resp16 = calcular(numero,16)
resp8 = calcular(numero,8)
resp2 = calcular(numero,2)

resp = f"HEXADECIMAL: {resp16}\nOCTAL: {resp8}\nbINARIO: {resp2}" 

# solucionamos solicitud

# enviamos respuesta
serverSock.sendto(resp.encode() , addr)	    