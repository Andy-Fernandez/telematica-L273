const net = require('net');
const puerto = 7777;

if (process.argv.length < 3) {
    console.log('Uso: node clientTCP.js mensaje');
    process.exit(1);
}

const message = process.argv[2];

const client = net.createConnection(puerto, function () {
    console.log('Cliente conectado al puerto ' + puerto);
    client.write(message);
});

client.on('data', function (data) {
    const respuesta = data.toString();
    console.log('Respuesta del servidor: ' + respuesta);
    client.end();
});
