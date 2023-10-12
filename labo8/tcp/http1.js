// Importamos el módulo 'http' para realizar solicitudes HTTP
const http = require('http');

// Definimos las opciones de la solicitud HTTP
const options = {
    host: 'http://www.minip1.com',  // La dirección del servidor al que nos conectaremos
    path: '/',                // La ruta a la que realizaremos la solicitud (en este caso, la raíz)
    port: 80,                 // El puerto del servidor HTTP (80 es el puerto estándar para HTTP)
    //method: 'GET'             // El método HTTP que usaremos (en este caso, GET)
    method: 'HEAD'             // El método HTTP que usaremos (en este caso, HEAD)
};

// Creamos un cliente HTTP para realizar la solicitud
const cliente = http.request(options, (peticion) => {
    // Cuando recibimos una respuesta del servidor, manejamos la respuesta aquí

    // Imprimimos el código de estado de la respuesta HTTP
    console.log("[+] Código de estado: " + peticion.statusCode);

    // Imprimimos las cabeceras de la respuesta HTTP
    console.log(peticion.headers);

    // Cuando recibimos datos del servidor, los mostramos en la consola
    peticion.on('data', (html) => {
        console.log(html.toString());
    });

    // Cuando la respuesta ha finalizado, mostramos "Desconectado"
    peticion.on('end', () => {
        console.log('Desconectado');
    });
});

// Enviamos la solicitud al servidor
cliente.end();
