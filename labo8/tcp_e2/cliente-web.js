const http = require('http');

// URL del servidor web al que deseas enviar la solicitud
const url = 'http://www.minip1.com';

// Enviar una solicitud GET al servidor web
const solicitud = http.get(url, (respuesta) => {
    // Imprimir los encabezados HTTP de la respuesta
    console.log('Encabezados HTTP:');
    console.log(respuesta.headers);

    // Inicializar una variable para almacenar el contenido de la página
    let contenido = '';

    // Escuchar el evento 'data' para recibir datos de la respuesta
    respuesta.on('data', (chunk) => {
        contenido += chunk;
    });

    // Escuchar el evento 'end' para manejar el final de la respuesta
    respuesta.on('end', () => {
        // Imprimir el contenido de la página web
        console.log('\nContenido de la página web:');
    });
        console.log(contenido);
    });

// Manejar errores de la solicitud
solicitud.on('error', (error) => {
    console.error('Error en la solicitud:', error);
});

// Manejar la finalización de la solicitud
solicitud.on('close', () => {
    console.log('Solicitud completada.');
});
