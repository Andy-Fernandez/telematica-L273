const readline = require('readline');
const lector = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const net = require('net');
const puerto = 7778;
const servidorIP = 'localhost';

const socketClient = net.createConnection(puerto, servidorIP, function () {
    console.log('Cliente conectado al puerto ' + puerto);
    leerMensaje();
});

function leerMensaje() {
    lector.question('', function (line) {
        console.log('cliente: ' + line);
        socketClient.write(line);

        if (line.toLowerCase() === 'adios') {
            lector.close();
            socketClient.end();
        } else {
            leerMensaje();
        }
    });
}

socketClient.on('data', function (data) {
    var respuesta = data.toString();
    console.log('Servidor: ' + respuesta);
});
