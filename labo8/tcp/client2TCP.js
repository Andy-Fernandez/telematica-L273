const readline = require('readline');
const lector = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const net = require('net');
const puerto = 7778;
const servidorIP = 'localhost';

const socketClient = net.createConnection(puerto, servidorIP,function() {
  console.log('Cliente conectado al puerto ' + puerto);
});

lector.on('line', function(line) {
  console.log('Introduce una palabra: ');
  socketClient.write(line);
});

// recibimos datos del servidor
socketClient.on('data', function(data) {
  var respuesta = data.toString();
  console.log('Respuesta del servidor: ' + respuesta);
  date = new Date();
  console.log('Con la fecha y hora: ' + date);
});