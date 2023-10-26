import socket

# Configuración del cliente
HOST = 'localhost'
PORT = 8081

# Función para enviar solicitud al servidor
def enviar_solicitud(apellido, hora, evento):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    solicitud = f"{apellido} {hora} {evento}"
    client.send(solicitud.encode())
    response = client.recv(1024).decode()

    print(response)
    client.close()

# Función principal del cliente
def main():
    apellido = input("Ingrese su apellido: ")
    hora = input("Ingrese la hora (HH:MM:SS): ")
    evento = input("¿Entrada o salida?: ").lower()

    if evento == "entrada" or evento == "salida":
        enviar_solicitud(apellido, hora, evento)
    else:
        print("Solicitud no válida. Use 'entrada' o 'salida'.")

if __name__ == "__main__":
    main()
