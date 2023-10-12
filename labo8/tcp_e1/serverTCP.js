const net = require('net');

const server = net.createServer(function (connection) {
    console.log('+ Cliente conectado');
    connection.on('data', function (data) {
        const request = data.toString().toUpperCase();
        connection.write(request);
        console.log('Connection finished');
    });
});

server.listen(7777);
