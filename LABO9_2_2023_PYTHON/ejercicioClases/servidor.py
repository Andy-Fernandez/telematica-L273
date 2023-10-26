import socket
import threading
import time
from datetime import datetime

# Configuración del servidor
HOST = 'localhost'
PORT = 8081
MAX_CONNECTIONS = 10

# Almacena las asistencias
asistencias = {}

# Función para registrar asistencia
def registrar_asistencia(apellido, hora, evento):
    if apellido not in asistencias:
        asistencias[apellido] = {'entrada': None, 'salida': None}

    asistencia = asistencias[apellido]
    if evento == 'entrada' and asistencia['entrada'] is None:
        asistencia['entrada'] = hora
    elif evento == 'salida' and asistencia['salida'] is None:
        asistencia['salida'] = hora

# Función para manejar las solicitudes de los clientes
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()

    apellido, hora, evento = request.split()
    #hora_actual = datetime.now().strftime("%H:%M:%S")
    hora_actual = hora
    if evento == "entrada" and "08:00:00" <= hora_actual <= "08:30:00":
        registrar_asistencia(apellido, hora_actual, evento)
        print(f"Entrada registrada para {apellido} a las {hora_actual}")
        response = f"¡Asistencia registrada! {hora_actual}"
    elif evento == "salida" and "12:00:00" <= hora_actual <= "12:30:00":
        registrar_asistencia(apellido, hora_actual, evento)
        print(f"Salida registrada para {apellido} a las {hora_actual}")
        response = f"¡Asistencia registrada! {hora_actual}"
    else:
        response = "Fuera de horario de asistencia."
  

    client_socket.send(response.encode())
    client_socket.close()

# Función principal del servidor
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(MAX_CONNECTIONS)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
