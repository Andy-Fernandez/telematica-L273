from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Clase que maneja las solicitudes del servidor
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Procesar los datos recibidos (nombre, apellido, celular, semestre y carrera)
        nombre = data.get('nombre', '')
        apellido = data.get('apellido', '')
        celular = data.get('celular', '')
        semestre = data.get('semestre', '')
        carrera = data.get('carrera', '')

        # Mostrar los datos recibidos en la respuesta
        response = f"Inscripción exitosa: {nombre} {apellido}, Celular: {celular}, Semestre: {semestre}, Carrera: {carrera}"
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor HTTP escuchando en el puerto {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
