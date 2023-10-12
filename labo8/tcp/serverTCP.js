//SERVIDOR TCP
const net = require('net');

const server = net.createServer( function(connection) { //connection es un socket y lo estamos creando
    console.log('+ Cliente conectado');
    connection.on('data', function(data) { //data es un buffer que recibe datos
        var peticion = data.toString();    //convertimos el buffer a string
        
        peticion = peticion.toUpperCase(); // Convertimos a mayúsculas la petición

        connection.write(peticion);        // Enviamos la petición al cliente

        console.log('Connection finished');
    });
});

server.listen(7778, function(){
    console.log('Servidor TCP escuchando en el puerto 7777');
}); // Escuchamos en el puerto 7777
