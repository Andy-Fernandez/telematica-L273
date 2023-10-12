const http = require('http');
const url = require('url');

// Crear un servidor HTTP
const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);

    // Verificar si la solicitud es una encuesta (ruta /encuesta)
    if (parsedUrl.pathname === '/encuesta' && req.method === 'GET') {
        // Recuperar los parámetros de la encuesta
        const params = parsedUrl.query;

        // Guardar los datos de la encuesta en tu base de datos o archivo
        // Aquí puedes implementar la lógica para guardar los datos donde prefieras

        // Enviar una respuesta al cliente
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('¡Gracias por completar la encuesta!\n');

        console.log('Datos de encuesta guardados:', params);
    } else {
        // Ruta no válida
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Ruta no válida\n');
    }
});

const port = 80;
server.listen(port, () => {
    console.log(`Servidor en ejecución en http://localhost:${port}`);
});
