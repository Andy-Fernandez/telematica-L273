const net = require('net');

const server = net.createServer(function (connection) {
    console.log('+ Cliente conectado');

    connection.on('data', function (data) {
        var request = data.toString();

        connection.write(request);

        console.log('Cliente: ' + request);

        if (request.toLowerCase() === 'adios') {
            console.log('Cliente dijo "adios". Cerrando la conexión.');
            connection.end();
            server.close();
        }
    });

    connection.on('end', function () {
        console.log('Cliente desconectado');
    });
});

server.listen(7778, function () {
    console.log('Servidor TCP escuchando en el puerto 7778');
});
